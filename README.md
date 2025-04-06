🌱 Sustainable Farming Assistant
--------------------------------

A smart AI-driven assistant that helps farmers and market researchers make informed decisions. Powered by TinyLlama for natural language reasoning and trained on agricultural and market datasets.

💡 Features
-----------

- 👨‍🌾 Farmer Advisor
  Suggests optimal crops based on soil properties, weather conditions, and farm inputs.

- 📊 Market Researcher
  Recommends the most profitable product to grow based on economic trends, demand-supply indicators, and pricing.

- 🤖 TinyLlama AI Advisor
  A conversational assistant powered by TinyLlama (https://ollama.com/library/tinyllama), trained using example queries from real datasets.

🛠️ Installation & Setup
------------------------

1. Clone the Repository

    git clone https://github.com/your-username/sustainable-farming-assistant.git
    cd sustainable-farming-assistant

2. Set Up Virtual Environment

    python3 -m venv venv
    source venv/bin/activate  (On Windows use: venv\Scripts\activate)

3. Install Dependencies

    pip install -r requirements.txt

4. Prepare Datasets

Ensure the following CSV files exist inside a `data/` directory:

    - data/farmer_dataset.csv
    - data/market_dataset.csv

These should contain your historical farming and market data.

Sample Data Columns:

- Farmer dataset:
    Soil pH, moisture, temperature, rainfall, fertilizer, pesticide, crop type, yield

- Market dataset:
    Product, market price, demand/supply, competitor price, economic & trend indicators

🚀 Running the Project
----------------------

1. ML-Based Crop and Market Prediction

    python main.py

2. TinyLlama AI Assistant

    First, make sure Ollama is installed and running TinyLlama:

    ollama run tinyllama

    Then run:

    python llm_advisor.py

🗂️ Project Structure
---------------------

sustainable-farming-assistant/
│
├── data/
│   ├── farmer_dataset.csv
│   └── market_dataset.csv
│
├── llm_advisor.py          -> LLM-based AI assistant using TinyLlama
├── main.py                 -> ML-based expert prediction (farmer + market)
├── model_farmer.pkl        -> Trained model for farmer predictions
├── model_market.pkl        -> Trained model for market predictions
├── scaler_farmer.pkl       -> Scaler for farmer features
├── scaler_market.pkl       -> Scaler for market features
├── requirements.txt
└── Readme.txt

🤖 Technologies Used
---------------------

- Python 3.11+
- scikit-learn
- pandas
- joblib
- Ollama (https://ollama.com/)
- TinyLlama (LLM model)

📬 Contact
----------

Made with 💚 for sustainable agriculture and smart AI.

Have questions or ideas?  
Open an issue or start a discussion on GitHub.
