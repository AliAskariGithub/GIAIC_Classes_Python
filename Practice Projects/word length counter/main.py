import streamlit as st

st.set_page_config(page_title="Lenght Counter", page_icon="📏", layout="centered")

st.title("Word Lenght Counter")
st.write("You can use this tool to count the number of characters, words, and sentences in your text or sentence.")

msg = st.text_input("Enter your text here:")
breakdown = msg.split()
count = breakdown.count(".")

if st.button("Analyze"):
    st.write(f"Number of characters: {len(msg)}")
    st.write(f"Number of words: {len(breakdown)}")

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
        © 2025 Word Length Counter | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)
