import streamlit as st
import google.generativeai as genai
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="GenAI Curriculum Generator",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# GOOGLE AI STUDIO API KEY
# -----------------------------
# Replace with your actual API key
GOOGLE_API_KEY = "AIzaSyA1ZSB3-5WaI0hdtOzPK5zj-5sn1NimuNg"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# TITLE
# -----------------------------
st.title("🎓 GenAI Curriculum Generator")
st.markdown("Generate AI-powered academic curriculum instantly.")

# -----------------------------
# SIDEBAR INPUTS
# -----------------------------
st.sidebar.header("📌 Curriculum Inputs")

skill = st.sidebar.text_input("Skill / Domain", "Machine Learning")
education_level = st.sidebar.selectbox(
    "Education Level",
    ["Diploma", "BTech", "Masters", "Certification"]
)

num_semesters = st.sidebar.slider("Number of Semesters", 1, 8, 4)
weekly_hours = st.sidebar.slider("Weekly Hours", 10, 40, 20)