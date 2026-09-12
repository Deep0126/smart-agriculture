import streamlit as st
from database import validate_login

def show_login_page():
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌱 AgriSmart Connect</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Smart Agriculture Portal</h4>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("Demo Account -> Username: **admin** | Password: **password123**")
        with st.form("login_form"):
            st.subheader("Login to your account")
            username = st.text_input("Username / Email")
            password = st.text_input("Password", type="password")
            remember = st.checkbox("Remember me")
            
            submit = st.form_submit_button("Login", use_container_width=True)
            
            if submit:
                if not username or not password:
                    st.error("Please fill in both fields.")
                elif validate_login(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login Successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("Invalid username or password!")

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()
