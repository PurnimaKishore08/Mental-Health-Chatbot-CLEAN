import streamlit as st
from sentiment import analyze_sentiment
from chatbot_response import get_chatbot_reply
from datetime import datetime
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Load wellness tips
with open('data/wellness_tips.json', 'r') as f:
    tips = json.load(f)

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("🧠 AI Mental Health Chatbot")
st.markdown("Hello! I'm here to listen and support you. Just type how you're feeling.")

# User input
user_input = st.text_area("📝 Your Message", placeholder="Type your thoughts here...")

if st.button("💬 Submit"):
    if user_input.strip():
        # Analyze sentiment
        sentiment = analyze_sentiment(user_input)
        st.write(f"**Detected Emotion:** {sentiment}")

        # Get chatbot reply
        reply = get_chatbot_reply(user_input, sentiment)
        st.markdown(f"🤖 **Chatbot:** {reply}")

        # Suggest tips if negative
        if sentiment in ["Negative", "Very Negative"]:
            st.markdown("🌿 **Wellness Tip:**")
            st.info(tips.get(sentiment.lower(), "Take a deep breath. You got this!"))

        # Save journaling
        with open("journal.txt", "a") as f:
            f.write(f"{datetime.now()}\nUser: {user_input}\nBot: {reply}\n\n")
    else:
        st.warning("Please enter something.")