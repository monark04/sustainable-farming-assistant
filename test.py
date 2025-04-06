from ollama import chat

def get_response_from_ollama(user_query, expert_type):
    system_prompt = {
        "farmer": "You are an agricultural expert who gives short, practical, sustainable farming advice.",
        "market": "You are a market analyst who provides data-driven insights and pricing for crops and farming tools."
    }

    response = chat(model="tinyllama", messages=[
        {"role": "system", "content": system_prompt[expert_type]},
        {"role": "user", "content": user_query}
    ])
    return response['message']['content']

def main():
    print("Welcome to the Sustainable Farming Assistant!")
    print("Choose your expert:")
    print("1. 👨‍🌾 Farmer Advisor")
    print("2. 📊 Market Researcher")
    choice = input("Enter 1 or 2: ")

    expert = "farmer" if choice == "1" else "market"
    print(f"Selected: {expert.title()}")

    while True:
        user_query = input("\nAsk a question (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("👋 Exiting. Happy Farming!")
            break

        response = get_response_from_ollama(user_query, expert)
        print(f"\n🧠 Assistant: {response}")

if __name__ == "__main__":
    main()
