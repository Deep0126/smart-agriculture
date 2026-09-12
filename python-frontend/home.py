import streamlit as st

def show_page():
    st.title("Welcome to AgriSmart Connect 🌾")
    st.subheader("Smart Farming, Smarter Future")
    st.write("""
    AgriSmart Connect is a comprehensive platform designed to empower farmers with real-time data 
    and IoT-driven insights. By monitoring soil, weather, and crops, we help you maximize yield and minimize resource wastage.
    """)
    
    st.markdown("### 🌟 Quick Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("#### 🌱 Soil Monitoring\nTrack moisture and nutrients in real-time.")
        st.success("#### ☀ Weather Tracking\nGet accurate rain and temperature forecasts.")
        
    with col2:
        st.warning("#### 💧 Smart Irrigation\nAutomated pump controls based on soil data.")
        st.error("#### 📊 Farm Analytics\nVisualize your farm's performance daily.")
        
    with col3:
        st.info("#### 🌡 Temp & Humidity\nProtect crops from extreme weather.")
        st.success("#### 🚜 Smart Farming\nEmbrace the future of agriculture.")
        
    st.markdown("---")
    st.write("👈 **Use the sidebar navigation menu on the left to access different modules.**")
