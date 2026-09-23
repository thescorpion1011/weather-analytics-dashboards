import streamlit as st

API_KEY = st.secrets["OPENWEATHER_API_KEY"]
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API_KEY=", API_KEY)
