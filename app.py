import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timezone, timedelta
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import plotly.express as px

from weather import get_current_weather


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)


# -----------------------------
# Auto Refresh
# Refresh weather every 60 seconds
# -----------------------------
st_autorefresh(
    interval=60000,
    key="weather_refresh"
)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌦️ Weather Dashboard")
st.sidebar.markdown("---")


# India Time / IST
india_time = datetime.now(
    timezone(timedelta(hours=5, minutes=30))
)

current_time = india_time.strftime(
    "%d-%m-%Y\n\n%I:%M:%S %p"
)

st.sidebar.info(current_time)


city = st.sidebar.text_input(
    "Enter City",
    "Mumbai"
)


# -----------------------------
# Title
# -----------------------------
st.title("🌦️ Live Weather Dashboard")
st.markdown("---")


# -----------------------------
# Get Weather Data
# -----------------------------
try:

    raw_data = get_current_weather(city)

    # Check OpenWeather API response
    if raw_data.get("cod") != 200:

        st.error(
            f"Weather API Error: {raw_data.get('message', 'Unknown error')}"
        )

        st.stop()


    # -----------------------------
    # Extract Weather Information
    # -----------------------------

    temperature = raw_data["main"]["temp"]

    humidity = raw_data["main"]["humidity"]

    pressure = raw_data["main"]["pressure"]

    feels_like = raw_data["main"]["feels_like"]

    wind = raw_data["wind"]["speed"]

    condition = raw_data["weather"][0]["main"]

    description = raw_data["weather"][0]["description"]

    icon = raw_data["weather"][0]["icon"]

    sunrise_timestamp = raw_data["sys"]["sunrise"]

    sunset_timestamp = raw_data["sys"]["sunset"]

    # OpenWeather timezone offset for selected city
    city_timezone_offset = raw_data["timezone"]


    # -----------------------------
    # Top Metrics
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "🌡️ Temperature",
        f"{temperature} °C"
    )


    col2.metric(
        "💧 Humidity",
        f"{humidity} %"
    )


    col3.metric(
        "🌬️ Wind",
        f"{wind} m/s"
    )


    col4.metric(
        "📌 Pressure",
        f"{pressure} hPa"
    )


    st.markdown("---")


    # -----------------------------
    # Current Weather
    # -----------------------------

    left, right = st.columns([2, 1])


    with left:

        st.subheader("Current Weather")

        st.write(
            f"### Condition: {condition}"
        )

        st.write(
            f"Description: {description}"
        )

        st.write(
            f"Feels Like: {feels_like} °C"
        )


    with right:

        icon_url = (
            f"https://openweathermap.org/img/wn/"
            f"{icon}@4x.png"
        )

        st.image(icon_url)


    st.markdown("---")


    # -----------------------------
    # Temperature Gauge
    # -----------------------------

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=temperature,

            title={
                "text": "Temperature (°C)"
            },

            gauge={

                "axis": {
                    "range": [-10, 50]
                },

                "bar": {
                    "color": "red"
                },

                "steps": [

                    {
                        "range": [-10, 10],
                        "color": "lightblue"
                    },

                    {
                        "range": [10, 25],
                        "color": "lightgreen"
                    },

                    {
                        "range": [25, 50],
                        "color": "orange"
                    }

                ]

            }

        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------
    # Humidity Gauge
    # -----------------------------

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=humidity,

            title={
                "text": "Humidity (%)"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                }

            }

        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------
    # Wind Gauge
    # -----------------------------

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=wind,

            title={
                "text": "Wind Speed (m/s)"
            }

        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------
    # Temperature Trend
    # -----------------------------

    st.subheader("Today's Temperature Trend")


    hours = [
        "6 AM",
        "9 AM",
        "12 PM",
        "3 PM",
        "6 PM",
        "9 PM"
    ]


    # Sample values
    # Can be replaced with forecast API data later
    temp = [
        24,
        26,
        31,
        33,
        30,
        27
    ]


    df = pd.DataFrame({

        "Hour": hours,

        "Temperature": temp

    })


    fig = px.line(

        df,

        x="Hour",

        y="Temperature",

        markers=True,

        title="Today's Temperature Trend"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------
    # Sunrise & Sunset
    # -----------------------------

    col1, col2 = st.columns(2)


    # Convert OpenWeather timezone offset
    # into a timezone for the selected city
    city_tz = timezone(
        timedelta(seconds=city_timezone_offset)
    )


    # Sunrise
    sunrise = datetime.fromtimestamp(
        sunrise_timestamp,
        tz=city_tz
    ).strftime("%I:%M %p")


    # Sunset
    sunset = datetime.fromtimestamp(
        sunset_timestamp,
        tz=city_tz
    ).strftime("%I:%M %p")


    with col1:

        st.metric(
            "🌅 Sunrise",
            sunrise
        )


    with col2:

        st.metric(
            "🌇 Sunset",
            sunset
        )


except Exception as e:

    st.error(
        f"Unable to fetch weather data: {e}"
    )
