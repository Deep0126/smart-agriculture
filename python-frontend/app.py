import streamlit as st
from auth import show_login_page, logout
from database import setup_demo_user
import home
import dashboard
import sensor
import weather
import about

# Page Config MUST be the first Streamlit command
st.set_page_config(page_title="AgriSmart Connect", page_icon="🌱", layout="wide")

# Beautiful Custom CSS for Agriculture Theme
st.markdown("""
<style>
    /* Hide all header anchor links (the hover link icon) */
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
        display: none !important;
    }
    .stMarkdown a.header-anchor {
        display: none !important;
    }
    
    /* Main background */
    .stApp {
        background-color: #f7fcf7;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #e8f5e9;
        border-right: 1px solid #c8e6c9;
    }
    
    /* Global Text Colors (Forces light mode text on custom light backgrounds) */
    h1, h2, h3 {
        color: #2e7d32 !important;
    }
    p, label, .stCheckbox p {
        color: #333333 !important;
    }
    
    /* Input Fields (Fix for dark mode clash) */
    .stTextInput input, .stNumberInput input {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #c8e6c9 !important;
        border-radius: 6px !important;
    }
    
    /* Info/Alert Box (Demo Account msg) */
    [data-testid="stAlert"] {
        background-color: #e8f5e9 !important;
        color: #1b5e20 !important;
        border: 1px solid #c8e6c9 !important;
    }
    [data-testid="stAlert"] p {
        color: #1b5e20 !important;
    }
    
    /* Metric Cards */
    [data-testid="metric-container"] {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e8f5e9;
    }
    [data-testid="stMetricValue"] {
        color: #1b5e20 !important;
    }
    [data-testid="stMetricLabel"] p {
        color: #555555 !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #4caf50;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #388e3c;
        color: white !important;
        border-color: #388e3c;
    }
    
    /* Forms / Login Box */
    [data-testid="stForm"] {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.05);
        border: 2px solid #e8f5e9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Attempt to setup demo user in MongoDB quietly
setup_demo_user()

# Authentication Routing
if not st.session_state.logged_in:
    show_login_page()
else:
    # ---------------- HEADER ----------------
    col_logo, col_title, col_logout = st.columns([1, 8, 2])
    with col_logo:
        st.markdown("<h1 style='color: #2e7d32; margin-top: -15px;'>🌱</h1>", unsafe_allow_html=True)
    with col_title:
        st.markdown("<h2 style='color: #2e7d32; margin-top: -10px;'>AgriSmart Connect</h2>", unsafe_allow_html=True)
    with col_logout:
        st.write("") # spacing
        if st.button("Logout 🚪", use_container_width=True):
            logout()
            
    st.markdown("---")

    # ---------------- SIDEBAR NAVIGATION ----------------
    st.sidebar.markdown("## 🧭 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Sensor", "Weather", "About"])

    # ---------------- PAGE ROUTING ----------------
    if page == "Home":
        home.show_page()
    elif page == "Dashboard":
        dashboard.show_page()
    elif page == "Sensor":
        sensor.show_page()
    elif page == "Weather":
        weather.show_page()
    elif page == "About":
        about.show_page()
