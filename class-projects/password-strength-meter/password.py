import re
import random
import string
import streamlit as st
from streamlit.components.v1 import html

COMMON_PASSWORDS = [
    'password', '123456', '12345678', 'qwerty', 'abc123',
    'password123', '111111', 'letmein', 'admin', 'welcome'
]

from typing import Tuple

def check_password_strength(password: str) -> Tuple[str, int]:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if password.lower() not in COMMON_PASSWORDS:
        score += 1
    else:
        feedback.append("❌ Avoid common passwords like 'password123'.")

    if not re.search(r'(.)\1\1', password): 
        score += 1
    else:
        feedback.append("❌ Avoid repeating characters like 'aaa' or '111'.")

    if not re.search(r'(?=.*[a-z]{3})|(?=.*[0-9]{3})', password.lower()): 
        score += 1
    else:
        feedback.append("❌ Avoid sequential patterns like 'abc' or '123'.")

    if score >= 6:
        return "✅ Strong Password!", score
    elif score >= 4:
        return "⚠️ Moderate Password. Consider adding more security features.\n" + "\n".join(feedback), score
    else:
        return "❌ Weak Password. Improve it using the suggestions below.\n" + "\n".join(feedback), score

def generate_password(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for _ in range(length))

st.title('🔐 Password Strength Meter')
password = st.text_input('Enter your password:', type='password')
if password:
    strength_message, score = check_password_strength(password)
    st.markdown(strength_message)

    # Strength Bar
    strength_percentage = (score / 7) * 100
    html(f'''<div style="width: 100%; background-color: #ddd;">
        <div style="width: {strength_percentage}%; height: 25px; background-color: {'#4caf50' if score >= 6 else '#ff9800' if score >= 4 else '#f44336'};"></div>
        </div>''', height=35)

st.header('🔑 Generate a Strong Password')
length = st.slider('Select password length', min_value=8, max_value=20, value=12)
if st.button('Generate Password'):
    strong_password = generate_password(length)
    st.success(f'Generated Password: `{strong_password}`')

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
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
        left: 0;
        width: max-content;
        text-align: center;
        color: #888;
        padding: 10px;
        background-color: #ffffff;
        z-index: 0;
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
        © 2025 Password Strength Meter | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)