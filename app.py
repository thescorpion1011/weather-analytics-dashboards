import streamlit as st
import requests
import plotly.graph_objects as go
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦",
    layout="wide"
)

# Auto refresh every second
st_autorefresh(interval=1000, key="clock")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌦 Weather Dashboard")
st.sidebar.markdown("---")

current_time = datetime.now().strftime("%d-%m-%Y\n\n%I:%M:%S %p")
st.sidebar.info(current_time)

city = st.sidebar.text_input("Enter City", "Mumbai")

# -----------------------------
# Title
# -----------------------------
st.title("🌦 Live Weather Dashboard")
st.markdown("---")

# -----------------------------
# Backend URL
# -----------------------------
BASE_URL = "http://127.0.0.1:8000"

try:

    response = requests.get(f"{BASE_URL}/weather/{city}")

    data = response.json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🌡 Temperature", f"{data['temperature']} °C")

    col2.metric("💧 Humidity", f"{data['humidity']} %")

    col3.metric("🌬 Wind", f"{data['wind']} m/s")

    col4.metric("📌 Pressure", f"{data['pressure']} hPa")

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Current Weather")

        st.write("### Condition :", data["condition"])

        st.write("Description :", data["description"])

        st.write("Feels Like :", data["feels_like"], "°C")

    with right:

        icon = data["icon"]

        icon_url = f"https://openweathermap.org/img/wn/{icon}@4x.png"

        st.image(icon_url)

except Exception as e:

    st.error(e)

import plotly.graph_objects as go

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=data["temperature"],

    title={"text":"Temperature (°C)"},

    gauge={

        "axis":{"range":[-10,50]},

        "bar":{"color":"red"},

        "steps":[

            {"range":[-10,10],"color":"lightblue"},

            {"range":[10,25],"color":"lightgreen"},

            {"range":[25,50],"color":"orange"}

        ]

    }

))

st.plotly_chart(fig,
use_container_width=True)

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=data["humidity"],

    title={"text":"Humidity (%)"},

    gauge={

        "axis":{"range":[0,100]}

    }

))

st.plotly_chart(fig,
use_container_width=True)

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=data["wind"],

    title={"text":"Wind Speed"}

))

st.plotly_chart(fig,
use_container_width=True)

import pandas as pd
import plotly.express as px

hours=[
"6 AM",
"9 AM",
"12 PM",
"3 PM",
"6 PM",
"9 PM"
]

temp=[
24,
26,
31,
33,
30,
27
]

df=pd.DataFrame({

"Hour":hours,

"Temperature":temp

})

fig=px.line(

df,

x="Hour",

y="Temperature",

markers=True,

title="Today's Temperature Trend"

)

st.plotly_chart(fig,
use_container_width=True)

from datetime import datetime

col1,col2=st.columns(2)

with col1:

    sunrise=datetime.fromtimestamp(
        data["sunrise"]
    ).strftime("%I:%M %p")

    st.metric("🌅 Sunrise",
              sunrise)

with col2:

    sunset=datetime.fromtimestamp(
        data["sunset"]
    ).strftime("%I:%M %p")

    st.metric("🌇 Sunset",
              sunset)