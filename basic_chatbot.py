def chatbot():
    print("ChatBot: Hello! Type something to start a conversation. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("ChatBot: Hi!")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks!")
        elif user_input == "what's your name":
            print("ChatBot: I'm CodeAlphaBot!!!")
        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("ChatBot: Sorry, I didn't understand that???")

chatbot()
