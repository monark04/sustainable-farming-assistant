import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load datasets
farmer_df = pd.read_csv("farmer_advisor_dataset.csv")
market_df = pd.read_csv("market_researcher_dataset.csv")

def farmer_advisor():
    print("\n👨‍🌾 Welcome to Farmer Advisor")
    soil_ph = float(input("Enter Soil pH: "))
    soil_moisture = float(input("Enter Soil Moisture: "))
    temperature = float(input("Enter Temperature (°C): "))
    rainfall = float(input("Enter Rainfall (mm): "))
    fertilizer = float(input("Enter Fertilizer Usage (kg): "))
    pesticide = float(input("Enter Pesticide Usage (kg): "))

    # Select relevant features
    features = ['Soil_pH', 'Soil_Moisture', 'Temperature_C', 'Rainfall_mm', 'Fertilizer_Usage_kg', 'Pesticide_Usage_kg']
    X = farmer_df[features]

    # Scale input and dataset
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=features)
    input_data = pd.DataFrame([[soil_ph, soil_moisture, temperature, rainfall, fertilizer, pesticide]], columns=features)
    input_scaled = pd.DataFrame(scaler.transform(input_data), columns=features)

    # Fit KMeans
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    farmer_df["Cluster"] = kmeans.fit_predict(X_scaled)
    input_cluster = kmeans.predict(input_scaled)[0]

    cluster_data = farmer_df[farmer_df["Cluster"] == input_cluster]
    recommended_crop = cluster_data["Crop_Type"].mode()[0]
    avg_yield = cluster_data["Crop_Yield_ton"].mean()
    sustainability_score = cluster_data["Sustainability_Score"].mean()

    print(f"\n✅ Recommended Crop: {recommended_crop}")
    print(f"📈 Average Yield (similar farms): {avg_yield:.2f} tons")
    print(f"🌱 Sustainability Score (avg): {sustainability_score:.2f}/100")


def market_researcher():
    print("\n📊 Welcome to Market Researcher")

    # Map strings to numbers if present (you might need to adjust based on actual data)
    mapping_dict = {
        "Low": 30,
        "Medium": 60,
        "High": 90
    }

    df = market_df.copy()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].replace(mapping_dict).infer_objects(copy=False)

    target_price = float(input("Enter your target price per ton: "))
    demand_index = float(input("Enter estimated demand index (0-100): "))
    supply_index = float(input("Enter estimated supply index (0-100): "))
    competitor_price = float(input("Enter competitor price per ton: "))
    economic_index = float(input("Enter economic indicator (0-100): "))
    weather_impact = float(input("Enter weather impact score (0-100): "))
    seasonal_factor = float(input("Enter seasonal factor (0-100): "))
    consumer_trend = float(input("Enter consumer trend index (0-100): "))

    features = ['Market_Price_per_ton', 'Demand_Index', 'Supply_Index',
                'Competitor_Price_per_ton', 'Economic_Indicator',
                'Weather_Impact_Score', 'Seasonal_Factor', 'Consumer_Trend_Index']

    X = df[features]
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=features)

    input_data = pd.DataFrame([[
        target_price, demand_index, supply_index,
        competitor_price, economic_index,
        weather_impact, seasonal_factor, consumer_trend
    ]], columns=features)
    input_scaled = pd.DataFrame(scaler.transform(input_data), columns=features)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)
    input_cluster = kmeans.predict(input_scaled)[0]

    cluster_data = df[df["Cluster"] == input_cluster]
    suggested_crop = cluster_data["Product"].mode()[0]
    avg_price = cluster_data["Market_Price_per_ton"].mean()
    avg_demand = cluster_data["Demand_Index"].mean()

    print(f"\n✅ Suggested Product: {suggested_crop}")
    print(f"💰 Avg Market Price: ₹{avg_price:.2f}/ton")
    print(f"🔥 Avg Demand Index: {avg_demand:.2f}/100")


# Entry point
print("Welcome to the Sustainable Farming Assistant!")
print("Choose your expert:")
print("1. 👨‍🌾 Farmer Advisor")
print("2. 📊 Market Researcher")

choice = input("Enter 1 or 2: ").strip()
if choice == "1":
    farmer_advisor()
elif choice == "2":
    market_researcher()
else:
    print("Invalid choice. Please enter 1 or 2.")
