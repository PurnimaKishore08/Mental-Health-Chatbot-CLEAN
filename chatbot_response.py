def get_chatbot_reply(user_input):
    if "sad" in user_input.lower():
        return "I'm really sorry you're feeling this way. You're not alone. I'm here for you. 💙"
    elif "happy" in user_input.lower():
        return "That's wonderful! Keep shining. 😊"
    else:
        return "Thank you for sharing. I'm here for you. 🤗"
