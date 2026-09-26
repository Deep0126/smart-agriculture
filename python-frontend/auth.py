import streamlit as st
from database import validate_login, register_user

def show_login_page():
    # Reduced top spacing and smaller header to prevent scrolling
    st.markdown("<h2 style='text-align: center; color: #2e7d32; margin-top: 5vh;'>🌱 AgriSmart Connect</h2>", unsafe_allow_html=True)
    
    # Tighter columns for a smaller, more compact login box
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        tab1, tab2 = st.tabs(["🔒 Login", "📝 New Registration"])
        
        with tab1:
            with st.form("login_form"):
                st.markdown("<h3 style='text-align: center; color: #2e7d32; margin-bottom: 10px;'>Login</h3>", unsafe_allow_html=True)
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                submit = st.form_submit_button("Login", use_container_width=True)
                
                if submit:
                    if not username or not password:
                        st.error("Please fill in both fields.")
                    elif validate_login(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password!")
                        
        with tab2:
            with st.form("register_form"):
                st.markdown("<h3 style='text-align: center; color: #2e7d32; margin-bottom: 10px;'>Create Account</h3>", unsafe_allow_html=True)
                new_user = st.text_input("Choose Username")
                new_pass = st.text_input("Choose Password", type="password")
                confirm_pass = st.text_input("Confirm Password", type="password")
                
                reg_submit = st.form_submit_button("Register", use_container_width=True)
                
                if reg_submit:
                    if not new_user or not new_pass or not confirm_pass:
                        st.error("Please fill in all fields.")
                    elif new_pass != confirm_pass:
                        st.error("Passwords do not match!")
                    else:
                        success, message = register_user(new_user, new_pass)
                        if success:
                            st.success(message)
                        else:
                            st.error(message)

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()
