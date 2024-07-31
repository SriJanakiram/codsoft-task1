def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    # Asking about the chatbot's identity
    elif "who are you" in user_input or "what are you" in user_input:
        return "I am a simple rule-based chatbot. How can I assist you?"
    
    # Asking about the chatbot's capabilities
    elif "what can you do" in user_input or "help" in user_input:
        return "I can answer basic questions and have a simple conversation with you. Ask me anything!"
    
    # Asking for the time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    
    # Asking for the date
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    
    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Default response for unrecognized inputs
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chat loop to interact with the chatbot
print("Chatbot: Hello! Type 'bye' to exit the chat.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
