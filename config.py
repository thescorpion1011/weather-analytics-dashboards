import streamlit as st

API_KEY = st.secrets[27a54483f23214c83ccb6665cdb1f7fb]
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API_KEY=", API_KEY)
