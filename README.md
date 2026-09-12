# 🌱 AgriSmart Connect - Smart Agriculture Portal

AgriSmart Connect is a comprehensive, 100% Python-based Smart Agriculture portal designed to monitor IoT sensors, weather, and farm data. It features a modern UI built entirely with Streamlit.

## ✨ Features
*   **Secure Login System:** Session-state authentication.
*   **MongoDB Integration:** Stores users and data (via PyMongo).
*   **Farm Dashboard:** Real-time metrics and charts for Soil Moisture and Temperature.
*   **Sensor Monitoring:** Individual sensor hardware status and Water Pump controls.
*   **Weather Page:** Real-time weather forecasting.
*   **Modular Codebase:** Clean, multi-file Python structure.

## 🛠 Technologies
*   **Frontend & Logic:** Python, Streamlit
*   **Database:** MongoDB Atlas (PyMongo)
*   **Charts & Data:** Pandas

## 📁 Folder Structure
```
smart-agriculture/
│
├── python-frontend/        # Python Streamlit UI Project
│   ├── app.py              # Main Entry Point & Router
│   ├── auth.py             # Login & Logout Logic
│   ├── database.py         # MongoDB Connection & Queries
│   ├── home.py             # Landing Page
│   ├── dashboard.py        # Analytics & Charts
│   ├── sensor.py           # Hardware Status
│   ├── weather.py          # Weather Information
│   ├── about.py            # Project Info
│   ├── requirements.txt    # Python Dependencies
│   └── .python-version     # Render deployment config (3.11)
```

## 🚀 How to Run Locally

1. Navigate to the `python-frontend` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your MongoDB URI as an environment variable:
   ```bash
   # Windows
   set MONGO_URI=mongodb+srv://<user>:<pass>@cluster...
   # Mac/Linux
   export MONGO_URI="mongodb+srv://<user>:<pass>@cluster..."
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## 🔑 Demo Account
*   **Username:** `admin`
*   **Password:** `password123`
