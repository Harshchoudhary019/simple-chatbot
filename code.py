import random

# Define some responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Feeling great, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure what you mean.", "Could you please clarify?"],
}

def chat():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print(random.choice(responses["bye"]))
            break
        response = responses.get(user_input, responses["default"])
        print(random.choice(response))

if __name__ == "__main__":
    chat()
