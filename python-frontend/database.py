import os
import pymongo
import streamlit as st
from datetime import datetime
import random

# Use environment variable for MongoDB (from Render or .env)
MONGO_URI = os.getenv("MONGO_URI", "")

@st.cache_resource
def init_connection():
    if not MONGO_URI:
        return None
    try:
        client = pymongo.MongoClient(MONGO_URI)
        # Test connection
        client.admin.command('ping')
        return client
    except Exception as e:
        print(f"MongoDB Connection Error: {e}")
        return None

def get_db():
    client = init_connection()
    if client:
        return client.agriSmartDB
    return None

def setup_demo_user():
    db = get_db()
    if db is not None:
        try:
            users = db.users
            if users.count_documents({"username": "admin"}) == 0:
                users.insert_one({"username": "admin", "password": "password123", "role": "farmer"})
        except Exception:
            pass # Failsafe if db throws error

def validate_login(username, password):
    # Universal fallback for BCA project demonstration
    if username == "admin" and password == "password123":
        return True
        
    db = get_db()
    if db is None:
        return False
    
    try:
        user = db.users.find_one({"username": username, "password": password})
        return user is not None
    except Exception:
        return False

def get_sensor_data():
    # In a real IoT setup, we would fetch db.sensor_data.find_one(sort=[('_id', -1)])
    # For robust demonstration, we provide smart simulated data.
    return {
        "soil_moisture": random.randint(40, 60),
        "temperature": random.randint(28, 35),
        "humidity": random.randint(55, 75),
        "light": random.randint(700, 950),
        "pump_status": random.choice(["ON", "OFF"]),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
