import streamlit as st
from model import analyze_sentiment

st.title("🧠 Sentiment Analyzer")
st.write("Enter some text and find out its sentiment!")

user_input = st.text_area("✍️ Enter Text", height=200)

if st.button("🔍 Analyze"):
    with st.spinner("Analyzing..."):
        result = analyze_sentiment(user_input)
        st.success(result)
