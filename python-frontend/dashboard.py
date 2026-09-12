import streamlit as st
import pandas as pd
from database import get_sensor_data

def show_page():
    st.title("📊 Farm Dashboard")
    st.write("Real-time insights and analytics from your farm.")
    
    # Fetch Data
    data = get_sensor_data()
    
    # Live Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌱 Soil Moisture", f"{data['soil_moisture']}%", "+2% (Good)")
    col2.metric("🌡 Temperature", f"{data['temperature']}°C", "-1°C")
    col3.metric("☁ Humidity", f"{data['humidity']}%", "Stable")
    col4.metric("☀ Light", f"{data['light']} Lux", "Sunny")
    
    st.markdown("---")
    
    # Charts
    st.subheader("📈 Live Sensor Trends")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.write("**Soil Moisture Trend (Past 5 hours)**")
        # Generates a dummy trend ending with the current live value
        moisture_df = pd.DataFrame(
            {"Moisture (%)": [42, 45, int(data['soil_moisture'])-2, 50, int(data['soil_moisture'])]}, 
            index=["8 AM", "9 AM", "10 AM", "11 AM", "Now"]
        )
        st.line_chart(moisture_df, color="#2e7d32")
        
    with chart_col2:
        st.write("**Temperature Trend (Past 5 hours)**")
        temp_df = pd.DataFrame(
            {"Temp (°C)": [26, 28, 30, int(data['temperature'])-1, int(data['temperature'])]}, 
            index=["8 AM", "9 AM", "10 AM", "11 AM", "Now"]
        )
        st.line_chart(temp_df, color="#ff9800")
