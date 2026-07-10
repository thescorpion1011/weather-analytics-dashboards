# 🌦 Weather Analytics Dashboard

A full-stack Weather Analytics Dashboard built using **FastAPI** and **Streamlit**.

This application provides real-time weather information, weather forecasting, and interactive data visualization using the OpenWeather API.

---

## 🚀 Features

### Current Weather
- 🌡 Current Temperature
- 🤗 Feels Like Temperature
- 💧 Humidity
- 🌬 Wind Speed
- 📌 Pressure
- ☁ Weather Condition
- 📝 Weather Description
- 🌅 Sunrise Time
- 🌇 Sunset Time
- 🌤 Weather Icon

### Dashboard
- 📊 Interactive Plotly Charts
- 🌡 Temperature Gauge
- 💧 Humidity Gauge
- 🌬 Wind Gauge
- 📈 Temperature Trend Chart
- 🕒 Live Digital Clock
- 📍 City Search
- 🎨 Professional Streamlit UI

### Upcoming Features
- 📅 7-Day Weather Forecast
- 🕐 Hourly Forecast
- 🌍 Live GPS Location
- 🌫 Air Quality Index (AQI)
- ☀ UV Index
- 🗺 Weather Map
- 📄 PDF Weather Report
- 💾 Search History
- 🌙 Dark/Light Theme

## 📸 Screenshots

- Streamlit Dashboard
- FastAPI Swagger API
- Weather Charts

## 📄 Project Documentation

The complete project report is available in:

`docs/Weather_Dashboard_Report.pdf`

# 🛠 Tech Stack

## Backend
- FastAPI
- Uvicorn
- Requests
- Python Dotenv

## Frontend
- Streamlit
- Plotly
- Pandas

## API
- OpenWeatherMap API

---

# 📁 Project Structure

Weather Dashboard

├── Backend

│ ├── app.py

│ ├── weather.py

│ ├── config.py

│ ├── .env

│ └── requirements.txt

│

├── Frontend

│ ├── app.py

│ ├── style.css

│ └── requirements.txt

│

└── README.md

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
```

---

## Go to Project Folder

```bash
cd weather-dashboard
```

---

## Install Backend Packages

```bash
cd Backend

pip install -r requirements.txt
```

---

## Install Frontend Packages

```bash
cd ../Frontend

pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file inside the **Backend** folder.

```env
API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

## Run Backend

```bash
cd Backend

uvicorn app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd Frontend

streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📊 Dashboard Preview

✔ Current Weather

✔ Temperature Gauge

✔ Humidity Gauge

✔ Wind Gauge

✔ Temperature Trend

✔ Live Clock

✔ Weather Icon

✔ Sunrise & Sunset

---

# Future Improvements

- GPS Location Detection
- AQI Monitoring
- Weather Alerts
- 7-Day Forecast
- Hourly Forecast
- SQLite Database
- Docker Deployment
- Authentication
- CI/CD Pipeline

---

# Author

Ashish Yadav

Built with ❤️ using FastAPI and Streamlit.
