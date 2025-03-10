import streamlit as st

st.set_page_config(page_title='Simple Calculator', page_icon='🟰', layout='centered')

st.markdown("""
    <style>
    .stButton button {
        background-color: black;
        color: white;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        border-radius: 10px;
        transition-duration: 0.4s;
        cursor: pointer;
        width: 100%;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Simple Calculator 🧮")
st.write("A simple calculator with basic operations")

first_number = st.number_input("Enter your first number : ", format="%.2f")
second_number = st.number_input("Enter your second number : ", format="%.2f")

operation = st.selectbox("Select operation: ", ["Addition", "Subtraction", "Multiplication", "Divide"])

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
        © 2025 Simple Calculator | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)

result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = first_number + second_number
    elif operation == "Subtraction":
        result = first_number - second_number
    elif operation == "Multiplication":
        result = first_number * second_number
    elif operation == "Divide":
        if second_number != 0:
            result = first_number / second_number
        else:
            st.error("Cannot divide by zero")

    if result is not None:
        st.success(f"Result of {operation} between {first_number} and {second_number} is: {result:.2f}")