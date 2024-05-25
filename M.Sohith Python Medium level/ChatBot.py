from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('SimpleBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Main function to interact with the chatbot
def main():
    print("Welcome to SimpleBot! (Type 'exit' to end the conversation)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("SimpleBot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("SimpleBot:", response)

if __name__ == "__main__":
    main()
