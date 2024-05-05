from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r"hi|hey|hello", ["Hello! Welcome to Amazon services.", "Hey there! How can I assist you today?"]),
    (r"order status", ["Please provide your order ID, and I will check the status for you."]),
    (r"cancel order", ["To cancel an order, please contact our customer service at 1-800-AMAZON."]),
    (r"delivery|shipping", ["Our standard delivery time is 2-3 business days. Would you like to track your order?"]),
    (r"refund", ["For refunds, please initiate a return request from your account or contact us for assistance."]),
    (r"help", ["How can I assist you today?", "Sure, what do you need help with?"]),
    (r"quit", ["Thank you for using Amazon services. Have a great day!"]),
]

# Create chatbot instance
chatbot = Chat(patterns, reflections)

# Main function
def main():
    print("Welcome to Amazon Services Chatbot!")
    print("How can I assist you today?")
    print("Type 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Amazon Services Chatbot:", response)
        
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    main()
