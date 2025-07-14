import streamlit as st
import json
from datetime import datetime
from chatbot_response import get_chatbot_reply
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load wellness tips from JSON
with open("data/wellness_tips.json", "r", encoding="utf-8") as f:
    tips = json.load(f)

analyzer = SentimentIntensityAnalyzer()

st.title("🧠 AI Mental Health Chatbot")
st.write("Hello! I'm here to listen and support you. Just type how you're feeling.")

user_input = st.text_input("📝 Your Message")

if user_input:
    sentiment_score = analyzer.polarity_scores(user_input)["compound"]
    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    st.write(f"Detected Emotion: {sentiment}")

    # Get response
    reply = get_chatbot_reply(user_input)

    st.markdown(f"**🤖 Chatbot:** {reply}")

    # Show a wellness tip
    if isinstance(tips, dict):
        tip = tips.get(sentiment.lower(), "Take a deep breath. You got this!")
        st.info(f"🌿 Wellness Tip:\n\n{tip}")
    elif isinstance(tips, list):
        st.info(f"🌿 Wellness Tip:\n\n{tips[0]}")  # fallback if list

    # Log conversation
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}\nUser: {user_input}\nBot: {reply}\n\n")
