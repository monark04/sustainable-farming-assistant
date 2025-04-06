import pandas as pd
import ollama

def load_farmer_examples():
    df = pd.read_csv("farmer_advisor_dataset.csv")
    examples = []
    for _, row in df.sample(n=5).iterrows():  # sample random 5 rows
        query = (
            f"Soil pH: {row['Soil_pH']}, Moisture: {row['Soil_Moisture']}, Temp: {row['Temperature_C']}°C, "
            f"Rainfall: {row['Rainfall_mm']}mm, Fertilizer: {row['Fertilizer_Usage_kg']}kg, "
            f"Pesticide: {row['Pesticide_Usage_kg']}kg"
        )
        response = f"Recommended Crop: {row['Crop_Type']}, Yield: {row['Crop_Yield_ton']} tons, Sustainability: {row['Sustainability_Score']}/100"
        examples.append({"role": "user", "content": f"Q: {query}"})
        examples.append({"role": "assistant", "content": response})
    return examples

def load_market_examples():
    df = pd.read_csv("market_researcher_dataset.csv")
    examples = []
    for _, row in df.sample(n=5).iterrows():
        query = (
            f"Target Price: ₹{row['Market_Price_per_ton']}, Demand Index: {row['Demand_Index']}, "
            f"Supply Index: {row['Supply_Index']}, Competitor Price: ₹{row['Competitor_Price_per_ton']}, "
            f"Economic Indicator: {row['Economic_Indicator']}, Weather Impact: {row['Weather_Impact_Score']}, "
            f"Seasonal Factor: {row['Seasonal_Factor']}, Consumer Trend: {row['Consumer_Trend_Index']}"
        )
        response = f"Suggested Product: {row['Product']}, Avg Market Price: ₹{row['Market_Price_per_ton']}, Demand Index: {row['Demand_Index']}/100"
        examples.append({"role": "user", "content": f"Q: {query}"})
        examples.append({"role": "assistant", "content": response})
    return examples

def query_llm(prompt, examples):
    messages = [{"role": "system", "content": "You are a farming and market advisor expert."}] + examples
    messages.append({"role": "user", "content": f"Q: {prompt}"})
    response = ollama.chat(model="tinyllama", messages=messages)
    return response['message']['content']

def run_farmer_advisor():
    print("\n🌾 TinyLlama Farmer Advisor")
    ph = input("Enter Soil pH: ")
    moisture = input("Enter Soil Moisture: ")
    temp = input("Enter Temperature (°C): ")
    rain = input("Enter Rainfall (mm): ")
    fert = input("Enter Fertilizer Usage (kg): ")
    pest = input("Enter Pesticide Usage (kg): ")

    prompt = (
        f"Soil pH: {ph}, Moisture: {moisture}, Temp: {temp}°C, Rainfall: {rain}mm, "
        f"Fertilizer: {fert}kg, Pesticide: {pest}kg"
    )
    examples = load_farmer_examples()
    result = query_llm(prompt, examples)
    print(f"\n🧠 TinyLlama's Advice:\n{result}")

def run_market_researcher():
    print("\n📈 TinyLlama Market Researcher")
    target_price = input("Enter your target price per ton: ")
    demand = input("Enter estimated demand index (0-100): ")
    supply = input("Enter estimated supply index (0-100): ")
    comp_price = input("Enter competitor price per ton: ")
    econ = input("Enter economic indicator (0-100): ")
    weather = input("Enter weather impact score (0-100): ")
    seasonal = input("Enter seasonal factor (0-100): ")
    trend = input("Enter consumer trend index (0-100): ")

    prompt = (
        f"Target Price: ₹{target_price}, Demand Index: {demand}, Supply Index: {supply}, "
        f"Competitor Price: ₹{comp_price}, Economic Indicator: {econ}, Weather Impact: {weather}, "
        f"Seasonal Factor: {seasonal}, Consumer Trend: {trend}"
    )
    examples = load_market_examples()
    result = query_llm(prompt, examples)
    print(f"\n📊 TinyLlama's Market Advice:\n{result}")

if __name__ == "__main__":
    print("🤖 TinyLlama AI Advisor")
    print("1. 🌾 Farmer Advisor")
    print("2. 📈 Market Researcher")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_farmer_advisor()
    elif choice == "2":
        run_market_researcher()
    else:
        print("Invalid choice.")
