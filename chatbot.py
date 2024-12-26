from transformers import pipeline

# Load the chatbot pipeline
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Start chatting with the model
print("Chatbot: Hello! I am a chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    # Generate a response
    response = chatbot(user_input)
    print(f"Chatbot: {response[0]['generated_text']}")