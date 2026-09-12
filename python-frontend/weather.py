import streamlit as st
import random

def show_page():
    st.title("☀ Local Weather")
    st.write("Real-time weather data and farming recommendations.")
    
    # Mock Weather Data
    weather_condition = random.choice(["Sunny", "Partly Cloudy", "Clear Skies"])
    rain_prob = random.randint(0, 30)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Condition", weather_condition, "Optimal")
    col2.metric("Wind Speed", "12 km/h", "Breeze")
    col3.metric("Rain Probability", f"{rain_prob}%", "Low")
    
    st.markdown("---")
    
    col_sun1, col_sun2 = st.columns(2)
    with col_sun1:
        st.info("🌅 **Sunrise:** 06:15 AM")
    with col_sun2:
        st.warning("🌇 **Sunset:** 06:45 PM")
        
    st.markdown("### 💡 Farming Recommendation")
    if rain_prob > 50:
        st.error("⚠️ Rain expected. Do not irrigate the fields today.")
    else:
        st.success("✅ Weather is sunny and dry. It is highly suitable for irrigation today. No heavy rain expected in the next 48 hours.")
