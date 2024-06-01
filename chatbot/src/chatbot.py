import random

# Predefined intents and responses
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey"],
        "responses": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye! Have a great day!", "See you later!"]
    }
}

def recognize_intent(user_input):
    preprocessed_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in preprocessed_input:
                return intent
    return None

def generate_response(intent):
    if intent in intents:
        responses = intents[intent]["responses"]
        return random.choice(responses)
    return "Sorry, I didn't understand that."

