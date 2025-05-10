import streamlit as st
import io
import contextlib
from main import BankAccount

# Custom class to redirect print statements to Streamlit
class StreamlitPrintCapture:
    def __init__(self):
        self.buffer = io.StringIO()
    
    def __enter__(self):
        self.old_stdout = contextlib.redirect_stdout(self.buffer)
        self.old_stdout.__enter__()
        return self.buffer
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.old_stdout.__exit__(exc_type, exc_val, exc_tb)

def main():
    st.set_page_config(
        page_title="Bank Account System",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("💰 Bank Account Management System")
    st.markdown("---")
    
    # Sidebar for account creation
    with st.sidebar:
        st.header("Create Account")
        st.markdown("---")
        with st.form("create_account_form"):
            account_holder = st.text_input("Account Holder Name")
            initial_balance = st.number_input("Initial Balance", min_value=0.0, value=1000.0, format="%.2f")
            submit_button = st.form_submit_button("Create Account")
            
            if submit_button and account_holder:
                if 'accounts' not in st.session_state:
                    st.session_state.accounts = {}
                st.session_state.accounts[account_holder] = BankAccount(account_holder, initial_balance)
                st.success(f"Account for {account_holder} created successfully!")
        
        if 'accounts' in st.session_state and st.session_state.accounts:
            st.markdown("---")
            st.subheader("Existing Accounts")
            for acc_name in st.session_state.accounts:
                acc = st.session_state.accounts[acc_name]
                st.write(f"• {acc_name}: ₹{acc._BankAccount__balance:,.2f}")
    
    # Initialize session state
    if 'accounts' not in st.session_state:
        st.session_state.accounts = {}
    
    # Main area for account operations
    if st.session_state.accounts:
        st.header("Account Operations")
        
        # Select an account
        account_names = list(st.session_state.accounts.keys())
        selected_account = st.selectbox("Select Account", account_names)
        
        if selected_account:
            account = st.session_state.accounts[selected_account]
            
            # Display tabs for different operations
            tab1, tab2, tab3 = st.tabs(["💵 Deposit", "💸 Withdraw", "🔍 Check Balance"])
            
            with tab1:
                st.subheader("Deposit Money")
                with st.form("deposit_form"):
                    deposit_amount = st.number_input("Amount to Deposit", min_value=0.0, value=0.0, format="%.2f", key="deposit")
                    deposit_button = st.form_submit_button("Deposit")
                    
                    if deposit_button:
                        with StreamlitPrintCapture() as output:
                            account.deposit(deposit_amount)
                        result = output.getvalue()
                        if "New balance" in result:
                            st.success(result)
                        else:
                            st.error(result)
            
            with tab2:
                st.subheader("Withdraw Money")
                with st.form("withdraw_form"):
                    withdraw_amount = st.number_input("Amount to Withdraw", min_value=0.0, value=0.0, format="%.2f", key="withdraw")
                    withdraw_button = st.form_submit_button("Withdraw")
                    
                    if withdraw_button:
                        with StreamlitPrintCapture() as output:
                            account.withdraw(withdraw_amount)
                        result = output.getvalue()
                        if "New balance" in result:
                            st.success(result)
                        else:
                            st.error(result)
            
            with tab3:
                st.subheader("Check Balance")
                if st.button("Show Balance"):
                    with StreamlitPrintCapture() as output:
                        account.checkbalance()
                    st.info(output.getvalue())
                    
                # Show a nice balance card
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.metric(
                        label=f"{selected_account}'s Balance", 
                        value=f"₹{account._BankAccount__balance:,.2f}"
                    )
                with col2:
                    st.write("Account holder: ", selected_account)
                    st.progress(min(account._BankAccount__balance / 10000, 1.0))
                    if account._BankAccount__balance < 1000:
                        st.warning("Low balance!")
                    elif account._BankAccount__balance > 50000:
                        st.success("Excellent balance!")
    else:
        st.info("Please create an account using the sidebar.")
        
        # Show a demo image or instructions
        st.markdown("---")
        st.subheader("Welcome to the Bank Account Management System")
        st.write("""
        This application allows you to:
        1. Create a new bank account
        2. Deposit money into your account
        3. Withdraw money from your account
        4. Check your account balance
        
        Get started by creating an account using the form in the sidebar.
        """)
        
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
        © 2025 Bank Account System | All rights reserved.
    </div>
    
    <div class="pre">
        presented by <a href="https://www.linkedin.com/in/ali-askari-355257308//">Ali Askari</a>
    </div>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main() 