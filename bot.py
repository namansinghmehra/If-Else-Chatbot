def get_response(user_input):
    """
    Generate a response based on user input using simple keyword matching.
    """
    user_input = user_input.lower()
    
    greetings = ['hello', 'hi', 'hey']
    if any(greet in user_input for greet in greetings):
        return "Hello! How can I help you?"
    
    if 'how are you' in user_input:
        return "I'm doing well, thank you!"
    
    if 'your name' in user_input:
        return "I am a friendly chatbot built using Python."
    
    if 'help' in user_input:
        return "I can respond to greetings and simple questions. Ask me anything!"
    
    return "Sorry, I didn't understand that. Can you rephrase?"

def chatbot():
    """
    Main chatbot function to interact with the user.
    """
    print("Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Chatbot: Please enter something.")
            continue
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
