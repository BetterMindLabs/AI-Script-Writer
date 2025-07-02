import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["gemini_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎬✨ Advertisement & Reels Script Writer")
st.write("Generate catchy ad or reels scripts for your product or service in seconds! 🚀")

# Inputs
product_name = st.text_input("🛍️ Product or Service Name", placeholder="e.g., Organic Skincare Serum")
audience = st.text_input("🎯 Target Audience", placeholder="e.g., young women interested in natural beauty")
selling_points = st.text_area("⭐ Key Selling Points or Features", placeholder="e.g., 100% organic, no chemicals, quick results")
tone = st.selectbox("🎤 Desired Tone", ["Catchy & Fun", "Emotional & Heartfelt", "Luxury & Premium", "Bold & Confident", "Simple & Friendly"])

if st.button("✨ Generate Script"):
    prompt = f"""
You are a creative copywriter specializing in short-form ads and Instagram reels. Write a short, catchy script for the following:

- Product or service name: {product_name}
- Target audience: {audience}
- Key selling points: {selling_points}
- Tone: {tone}

Make it engaging, easy to read aloud, and include call-to-action if possible. Keep it short and impactful. Give only one version of the script
"""

    response = model.generate_content(prompt)
    st.subheader("🎬 Your Ad/Reels Script")
    st.write(response.text)

st.markdown("---")
st.markdown("💡 **Tip**: You can copy this script directly into your video or post captions!")
