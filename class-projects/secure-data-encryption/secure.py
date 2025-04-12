import streamlit as st
import os 
import hashlib
import json
import time
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

try:
    from cryptography.fernet import Fernet
except ImportError:
    st.error("❌ Required package 'cryptography' is not installed. Installing...")
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet

# Configuration Constants
DATA_FILE = 'secure_data.json'
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60
MAX_ATTEMPTS = 3

# Page Configuration
st.set_page_config(
    page_title="Secure Data Encryption",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 10px;
    }
    .main {
        padding: 2rem;
    }
    .css-1d391kg {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Utility Functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_key(passkey):
    key = pbkdf2_hmac("sha256", passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 100000).hex()

def encrypt_text(text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.encrypt(text.encode()).decode()
    except Exception as e:
        st.error(f"Encryption Error: {str(e)}")
        return None

def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

# Load stored data
stored_data = load_data()

# Sidebar Navigation
with st.sidebar:
    st.title("🔐 Navigation")
    choice = st.selectbox(
        "Choose an option",
        ["Home", "Register", "Login", "Stored Data", "Retrieve Data"],
        key="navigation"
    )
    
    if st.session_state.authenticated_user:
        st.success(f"Logged in as: {st.session_state.authenticated_user}")
        if st.button("Logout"):
            st.session_state.authenticated_user = None
            st.experimental_rerun()

# Main Content
if choice == "Home":
    st.title("🔐 Secure Data Encryption System")
    st.markdown("""
    ### Welcome to our secure data storage system!
    
    #### Features:
    - 🔒 End-to-end encryption
    - 👤 User authentication
    - 🔑 Unique passkey for each data entry
    - ⏳ Automatic lockout after multiple failed attempts
    - 💾 Secure local storage
    
    #### How to use:
    1. Register a new account
    2. Login with your credentials
    3. Store encrypted data with a unique passkey
    4. Retrieve and decrypt your data when needed
    """)

elif choice == "Register":
    st.title("📝 Register New User")
    with st.form("register_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        submit = st.form_submit_button("Register")
        if submit:
            if username and password and confirm_password:
                if password != confirm_password:
                    st.error("❌ Passwords don't match!")
                elif username in stored_data:
                    st.warning("⚠️ Username already exists!")
                else:
                    stored_data[username] = {
                        "password": hash_password(password),
                        "data": []
                    }
                    save_data(stored_data)
                    st.success("✅ Registration successful!")
            else:
                st.error("❌ All fields are required!")

elif choice == "Login":
    st.subheader("🔑 User Login")
    
    if time.time() < st.session_state.lockout_time:
        remaining_time = int(st.session_state.lockout_time - time.time())
        st.error(f"⚠ Too many failed attempts. Please wait {remaining_time} seconds.")
        st.stop()
        
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"Welcome {username}")
        else:
            st.session_state.failed_attempts += 1
            remaining_attempts = MAX_ATTEMPTS - st.session_state.failed_attempts
            st.error(f"❌ Invalid Credentials | Attempts left: {remaining_attempts}.")   
            
            if st.session_state.failed_attempts >= MAX_ATTEMPTS:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("⚠ Too many failed attempts. Please wait 60 seconds.")
                
elif choice == "Stored Data":
    if not st.session_state.authenticated_user:
        st.warning("Please login first.")
    else:
        st.subheader("Stored Encrypted Data")
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Enter passkey (passphrase)", type="password")
        
        if st.button("Encrypt And Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("✅ Data encrypted and saved successfully.")
            else:
                st.error("All fields are required to fill.")
                
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("Please login first.")
    else:
        st.subheader("Retrieve Encrypted Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])
        
        if not user_data:
            st.info("No Data Found.")
        else:
            st.write("Encrypted Data Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")
                
                encrypted_text = st.text_input("Enter Encrypted Text")
                passkey = st.text_input("Enter passkey To Decrypt", type="password")
                
                if st.button("Decrypt"):
                    result = decrypt_text(encrypted_text, passkey)
                    if result:
                        st.success(f"✅ Decrypted : {result}")
                    else:
                        st.error("❌ Incorrect passkey or corrupted data.")
                        
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 150px;
        width: 100%;
        text-align: center;
        color: #888;
        padding: 10px;
        text-color: #f1f1f1;
    }
    
    .pre {
        font-family: monospace;
        position: fixed;
        bottom: 0;
        left: 330px;
        width: max-content;
        text-align: center;
        color: #888;
        padding: 10px;
        background-color: #ffffff;
        z-index: 10;
        border: none;
        border-right: 1px solid #f1f1f1;
        border-top-right-radius: 10px;
    }
    
    .pre a {
        color: #000;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    
    <div class="footer">
        © 2025 Secure Data Encryption System | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)