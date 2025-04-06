import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def farmer_advisor():
    print("\n👨‍🌾 Welcome to Farmer Advisor")
    # Load dataset
    df = pd.read_csv("farmer_advisor_dataset.csv")

    # Collect input
    input_data = {
        'Soil_pH': get_numeric_input("Enter Soil pH: "),
        'Soil_Moisture': get_numeric_input("Enter Soil Moisture: "),
        'Temperature_C': get_numeric_input("Enter Temperature (°C): "),
        'Rainfall_mm': get_numeric_input("Enter Rainfall (mm): "),
        'Fertilizer_Usage_kg': get_numeric_input("Enter Fertilizer Usage (kg): "),
        'Pesticide_Usage_kg': get_numeric_input("Enter Pesticide Usage (kg): ")
    }

    # Process
    features = ['Soil_pH', 'Soil_Moisture', 'Temperature_C', 'Rainfall_mm',
                'Fertilizer_Usage_kg', 'Pesticide_Usage_kg']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    input_scaled = scaler.transform([list(input_data.values())])

    knn = NearestNeighbors(n_neighbors=3)
    knn.fit(X)
    distances, indices = knn.kneighbors(input_scaled)

    # Gather results
    similar_rows = df.iloc[indices[0]]
    top_crop = similar_rows['Crop_Type'].mode().iloc[0]
    avg_yield = similar_rows['Crop_Yield_ton'].mean()
    avg_score = similar_rows['Sustainability_Score'].mean()

    print(f"\n✅ Recommended Crop: {top_crop}")
    print(f"📈 Average Yield (similar farms): {avg_yield:.2f} tons")
    print(f"🌱 Sustainability Score (avg): {avg_score:.2f}/100")

def market_researcher():
    print("\n📊 Welcome to Market Researcher")
    df = pd.read_csv("market_researcher_dataset.csv")

    # Convert non-numeric columns to numeric if necessary
    mapping = {'Low': 30, 'Medium': 60, 'High': 90}
    for col in ['Economic_Indicator', 'Demand_Index', 'Supply_Index', 
                'Weather_Impact_Score', 'Seasonal_Factor', 'Consumer_Trend_Index']:
        df[col] = df[col].replace(mapping)

    # Check for missing values after mapping
    df = df.dropna(subset=['Market_Price_per_ton', 'Demand_Index', 'Supply_Index',
                           'Competitor_Price_per_ton', 'Economic_Indicator',
                           'Weather_Impact_Score', 'Seasonal_Factor', 'Consumer_Trend_Index'])

    input_data = {
        'Market_Price_per_ton': get_numeric_input("Enter your target price per ton: "),
        'Demand_Index': get_numeric_input("Enter estimated demand index (0-100): "),
        'Supply_Index': get_numeric_input("Enter estimated supply index (0-100): "),
        'Competitor_Price_per_ton': get_numeric_input("Enter competitor price per ton: "),
        'Economic_Indicator': get_numeric_input("Enter economic indicator (0-100): "),
        'Weather_Impact_Score': get_numeric_input("Enter weather impact score (0-100): "),
        'Seasonal_Factor': get_numeric_input("Enter seasonal factor (0-100): "),
        'Consumer_Trend_Index': get_numeric_input("Enter consumer trend index (0-100): ")
    }

    features = ['Market_Price_per_ton', 'Demand_Index', 'Supply_Index',
                'Competitor_Price_per_ton', 'Economic_Indicator', 'Weather_Impact_Score',
                'Seasonal_Factor', 'Consumer_Trend_Index']

    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    input_scaled = scaler.transform([list(input_data.values())])

    knn = NearestNeighbors(n_neighbors=3)
    knn.fit(X)
    distances, indices = knn.kneighbors(input_scaled)

    similar_rows = df.iloc[indices[0]]
    top_product = similar_rows['Product'].mode().iloc[0]
    avg_market_price = similar_rows['Market_Price_per_ton'].mean()
    avg_demand = similar_rows['Demand_Index'].mean()

    print(f"\n✅ Suggested Product: {top_product}")
    print(f"💰 Avg Market Price: ₹{avg_market_price:.2f}/ton")
    print(f"🔥 Avg Demand Index: {avg_demand:.2f}/100")


if __name__ == "__main__":
    print("Welcome to the Sustainable Farming Assistant!")
    print("Choose your expert:")
    print("1. 👨‍🌾 Farmer Advisor")
    print("2. 📊 Market Researcher")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        farmer_advisor()
    elif choice == '2':
        market_researcher()
    else:
        print("Invalid choice. Please enter 1 or 2.")
