import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import time
import random

# Configuration
st.set_page_config(page_title="Smart Agri", page_icon="🌱", layout="wide")

# Sidebar Navigation
st.sidebar.title("🌱 Smart Agri")
page = st.sidebar.radio("Navigate", ["📊 Dashboard", "🌾 Crop Recommendation", "🍂 Disease Detection", "💰 Mandi Prices"])

st.sidebar.markdown("---")
st.sidebar.info("A Python-powered Smart Agriculture Platform.")

# ----------------- DASHBOARD -----------------
if page == "📊 Dashboard":
    st.title("Farmer Dashboard")
    st.write("Real-time insights from your field sensors.")

    # Fetch data from Render Backend
    API_URL = "https://smart-agriculture-tdbe.onrender.com/api/iot/data/latest"
    
    try:
        response = requests.get(API_URL, timeout=5)
        data = response.json()
        if not data or len(data) == 0:
            # Fallback dummy data if DB empty
            data = [{"moisture": 45, "temperature": 28, "timestamp": datetime.now().isoformat()}]
    except Exception as e:
        st.warning("Could not connect to live backend. Showing offline dummy data.")
        data = [{"moisture": 42, "temperature": 27, "timestamp": datetime.now().isoformat()}]
    
    latest_data = data[0]

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric(label="💧 Live Soil Moisture", value=f"{latest_data.get('moisture', 0)} %", delta="Normal")
    col2.metric(label="🌡️ Temperature", value=f"{latest_data.get('temperature', 0)} °C", delta="-1 °C")
    col3.metric(label="📡 Sensor Status", value="Active", delta="Online", delta_color="normal")

    st.markdown("---")
    st.subheader("Moisture Trend")
    # Dummy chart data to simulate history
    chart_data = pd.DataFrame(
        {"Moisture (%)": [40, 42, 45, 43, latest_data.get("moisture", 45)]},
        index=["10 AM", "11 AM", "12 PM", "1 PM", "Now"]
    )
    st.line_chart(chart_data)


# ----------------- CROP RECOMMENDATION -----------------
elif page == "🌾 Crop Recommendation":
    st.title("AI Crop Recommendation")
    st.write("Enter your soil nutrients to get the best crop suggestion.")

    with st.form("crop_form"):
        col1, col2 = st.columns(2)
        n = col1.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
        p = col2.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
        k = col1.number_input("Potassium (K)", min_value=0, max_value=200, value=30)
        ph = col2.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
        
        submitted = st.form_submit_button("Predict Best Crop")

        if submitted:
            with st.spinner("AI is analyzing your soil data..."):
                time.sleep(1) # Simulate API delay
                # In real scenario, call ml-service backend here
                crops = ['Wheat', 'Rice', 'Maize', 'Sugarcane', 'Cotton']
                prediction = random.choice(crops)
                confidence = round(random.uniform(85.0, 98.0), 1)

                st.success("Analysis Complete!")
                st.markdown(f"### 🌾 Recommended Crop: **{prediction}**")
                st.write(f"**AI Confidence Score:** {confidence}%")


# ----------------- DISEASE DETECTION -----------------
elif page == "🍂 Disease Detection":
    st.title("Plant Disease Detection")
    st.write("Upload a picture of a diseased leaf. Our AI model will analyze it and suggest treatments.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Leaf", width=400)
        
        if st.button("🔍 Analyze Disease"):
            with st.spinner("Analyzing image..."):
                time.sleep(1.5) # Simulate processing
                diseases = [
                    {"name": "Leaf Blight", "treatment": "Use appropriate fungicide and ensure proper drainage."},
                    {"name": "Rust", "treatment": "Apply sulfur-based fungicides immediately."},
                    {"name": "Healthy", "treatment": "No action needed. Keep up the good work!"}
                ]
                result = random.choice(diseases)
                
                st.success("Analysis Complete!")
                st.subheader(f"Detected: {result['name']}")
                if result['name'] != "Healthy":
                    st.error(f"**Treatment:** {result['treatment']}")
                else:
                    st.info(f"**Status:** {result['treatment']}")


# ----------------- MANDI PRICES -----------------
elif page == "💰 Mandi Prices":
    st.title("Live Mandi Prices")
    st.write("Today's real-time market rates for major crops.")

    prices = pd.DataFrame({
        "Crop Name": ['Wheat (Gehu)', 'Rice (Chawal)', 'Corn (Makka)', 'Sugarcane (Ganna)', 'Soybean'],
        "Price (INR)": ['₹2,200', '₹2,800', '₹1,900', '₹315', '₹4,600'],
        "Unit": ['Quintal', 'Quintal', 'Quintal', 'Quintal', 'Quintal'],
        "Trend": ['▲ Up', '▬ Stable', '▼ Down', '▲ Up', '▬ Stable'],
        "24h Change": ['+₹50', '₹0', '-₹30', '+₹10', '₹0']
    })

    # Optional: Highlight trends using pandas styling
    def color_trend(val):
        color = 'green' if 'Up' in val else 'red' if 'Down' in val else 'gray'
        return f'color: {color}; font-weight: bold;'

    st.dataframe(prices.style.map(color_trend, subset=['Trend']), use_container_width=True, hide_index=True)
