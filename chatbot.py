from datetime import datetime
import random


# ==========================================
#           RULE-BASED CHATBOT
# ==========================================

print("===================================")
print("          Welcome to CodeBot!")
print("===================================")
print("I am a simple rule-based chatbot.")
print("Type 'menu' to see available topics.")
print("Type 'bye' or 'exit' to end the chat.\n")


# Function to generate chatbot responses
def get_response(user_input):

    # Convert user input to lowercase
    user_input = user_input.lower()

    # Greeting
    if any(word in user_input.split() for word in ["hello", "hi", "hey"]):
        greetings = [
            "Hello! Nice to meet you. How can I help you?",
            "Hi there! How can I help you?",
            "Hey! It's great to chat with you.",
            "Hello! What would you like to know?"
        ]
        return random.choice(greetings)

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Bot's name
    elif "your name" in user_input or "who are you" in user_input:
        return "My name is CodeBot. I am a rule-based chatbot."

    # What can you do
    elif "what can you do" in user_input:
        return "I can answer basic questions and have a simple conversation with you."

    # Available options
    elif "options" in user_input or "menu" in user_input:
        return "You can ask me about Python, AI, programming, the current date, the current time, or my name."

    # Python
    elif "what is python" in user_input:
        return "Python is a popular programming language known for its simple syntax."

    # Artificial Intelligence
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return "Artificial Intelligence is the ability of computers to perform tasks that normally require human intelligence."

    # Programming
    elif "what is programming" in user_input:
        return "Programming is the process of writing instructions that tell a computer what to do."

    # Current time
    elif "what time" in user_input or "current time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return "The current time is " + current_time + "."

    # Current date
    elif "what date" in user_input or "today's date" in user_input:
        current_date = datetime.now().strftime("%d %B %Y")
        return "Today's date is " + current_date + "."

    # Help
    elif "help" in user_input:
        return "You can ask me about Python, AI, programming, my name, date, time, or available options."

    # Thank you
    elif "thank" in user_input or "thanks" in user_input:
        return "You're welcome! I'm happy to help."

    # Creator
    elif "who created you" in user_input:
        return "I was created as a Python-based internship project."

    # Exit
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"

    # Unknown input
    else:
        return "Sorry, I don't understand that. Please try another question."


# ==========================================
#           MAIN CHATBOT LOOP
# ==========================================

while True:

    # Get user input
    user_input = input("You: ")

    # Generate response
    response = get_response(user_input)

    # Display response
    print("Bot:", response)

    # Exit chatbot
    if user_input.strip() in ["bye", "exit"]:
        break
        