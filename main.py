# Simple chatbot in Python

while True:
    user = input("You: ")
    if "hello" in user.lower():
        print("Bot: Hi there!")
    elif "bye" in user.lower():
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that.")