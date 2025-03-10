import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🧊", layout="centered")

st.title("Number Guessing Game")
st.write("I have a number between 1 and 6 in mind. Can you guess it?")

random_number = random.randint(1, 6)
guess_number = st.number_input("Enter a number between 1 and 6", min_value=1, max_value=6)

if st.button("let Guess"):
    if guess_number == random_number:
        st.success("🎉Congratulations🎉! You have guessed the number correctly.")
    else:
        st.error(f"You Loose! The number was {random_number}. Try again.")

st.markdown(
    """
    <style>
    
    .stButton button {
        background-color: white;
        border: none;
        color: black;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
        border-radius: 12px;
        width: 100%;
        }
            
    .stButton button:hover {
        background-color: #f1f1f1;
        color: black;
       }
    
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
        © 2025 Number Guessing Game | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)