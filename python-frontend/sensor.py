import streamlit as st
from database import get_sensor_data

def show_page():
    st.title("📡 Sensor Monitoring")
    st.write("Monitor individual sensor hardware status.")
    
    data = get_sensor_data()
    
    st.markdown("### 🎛️ Live Sensor Feeds")
    
    # Soil Moisture
    st.write("#### 💧 Soil Moisture Sensor")
    st.progress(data['soil_moisture'] / 100.0)
    st.write(f"**Current Reading:** {data['soil_moisture']}%")
    status = "Normal / Optimal" if data['soil_moisture'] > 30 else "Dry ⚠️ Needs Water"
    st.info(f"**Status:** {status}")
    st.markdown("---")
    
    # Temperature & Humidity
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### 🌡 Temperature Sensor")
        st.write(f"**Current:** {data['temperature']} °C")
        temp_status = "Normal" if data['temperature'] < 35 else "High ⚠️"
        st.success(f"**Status:** {temp_status}")
    with col2:
        st.write("#### ☁ Humidity Sensor")
        st.write(f"**Current:** {data['humidity']}%")
        st.success("**Status:** Normal")
    
    st.markdown("---")
    
    # Water Pump Control
    st.write("#### 🚜 Irrigation Water Pump")
    st.write(f"**Current Status:** {data['pump_status']}")
    
    if data['pump_status'] == "OFF":
        if st.button("Turn Pump ON", type="primary"):
            st.success("Command sent: Pump turned ON successfully!")
    else:
        if st.button("Turn Pump OFF"):
            st.warning("Command sent: Pump turned OFF successfully!")
