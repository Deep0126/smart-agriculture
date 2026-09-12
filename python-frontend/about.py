import streamlit as st

def show_page():
    st.title("ℹ️ About AgriSmart Connect")
    
    st.write("""
    **AgriSmart Connect** is a professional portal designed to demonstrate the power of IoT, AI, and modern web technologies in agriculture.
    
    This platform helps farmers and agricultural administrators monitor critical farm data in real-time, enabling smart decision-making.
    
    #### 🎯 Core Features:
    - 🌱 **Soil & Crop Monitoring**
    - 🌡 **Temperature & Humidity Tracking**
    - ☀ **Weather Insights**
    - 💧 **Smart Irrigation Control**
    """)
    
    st.markdown("### 🛠 Project Technology Stack")
    st.write("""
    - **Programming Language:** Python
    - **Frontend/UI:** Streamlit (No separate HTML/CSS)
    - **Database:** MongoDB Atlas (PyMongo)
    - **Architecture:** Modular IoT-ready design
    - **Data Visualization:** Pandas & Streamlit Charts
    """)
    
    st.info("Built with 100% Python to demonstrate modern data-driven web applications.")
