import streamlit as st
from model import generate_caption

# Set Streamlit page config
st.set_page_config(page_title="Social Media Caption Generator", layout="centered")

# App Title
st.title("📱 Social Media Caption Generator")
st.write("Generate engaging captions for your social media posts using AI!")

# Input widgets
platform = st.selectbox("📌 Select Platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("🎯 Select Tone", ["Professional", "Funny", "Inspirational", "Casual"])
keywords = st.text_input("📝 Enter keywords or product name")

# Button
generate = st.button("🚀 Generate Caption")

# Output
if generate and keywords:
    prompt = f"Generate a {tone} caption for {platform} post about: {keywords}"
    with st.spinner("Generating..."):
        result = generate_caption(prompt)
    st.success("✅ Here's your caption:")
    st.markdown(f"**{result}**")
elif generate and not keywords:
    st.warning("⚠️ Please enter some keywords to generate a caption.")
