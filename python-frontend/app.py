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

# Beautiful Custom CSS (Theme-friendly)
st.markdown("""
<style>
    /* Hide all header anchor links (the hover link icon) */
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
        display: none !important;
    }
    .stMarkdown a.header-anchor {
        display: none !important;
    }
    
    /* Metric Cards styling */
    [data-testid="metric-container"] {
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        border: 1px solid rgba(76, 175, 80, 0.2);
    }
    
    /* Forms / Login Box */
    [data-testid="stForm"] {
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
        border: 2px solid rgba(76, 175, 80, 0.3);
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
