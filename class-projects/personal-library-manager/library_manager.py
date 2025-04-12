import streamlit as st
import json
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="wide"
)

data_storage = 'library.txt'

def load_library():
    if os.path.exists(data_storage):
        with open(data_storage, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_storage, 'w') as file:
        json.dump(library, file)

# Add this custom CSS at the top of your file after the imports
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    
    .sidebar-header {
        font-size: 24px !important;
        padding: 20px 0px;
        text-align: center;
        border-bottom: 2px solid #ffffff30;
        margin-bottom: 20px;
    }
    
    .sidebar-nav {
        padding: 10px;
        margin: 10px 0px;
        border-radius: 5px;
        background-color: #ffffff10;
    }
    
    .sidebar-footer {
        position: fixed;
        bottom: 0;
        padding: 20px;
        background: #1f1f1f;
        width: 100%;
        text-align: center;
        border-top: 1px solid #ffffff30;
    }
    
    .sidebar-stat {
        padding: 10px;
        margin: 10px 0px;
        border-radius: 5px;
        background-color: #ffffff10;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("📚 Personal Library Manager")
    st.sidebar.header("Navigation")
    
    # Initialize session state
    if 'library' not in st.session_state:
        st.session_state.library = load_library()

    # Enhanced Sidebar
    st.sidebar.markdown('<div class="sidebar-header">📚 Library Dashboard</div>', unsafe_allow_html=True)
    
    # Quick Stats in Sidebar
    with st.sidebar:
        total_books = len(st.session_state.library)
        read_books = len([book for book in st.session_state.library if book['read']])
        
        st.markdown('<div class="sidebar-stat">', unsafe_allow_html=True)
        st.markdown(f"📚 **Total Books:** {total_books}")
        st.markdown(f"✅ **Read:** {read_books}")
        st.markdown(f"📌 **Unread:** {total_books - read_books}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Navigation
    st.sidebar.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
    page = st.sidebar.radio(
        "Navigate to:",
        ["📖 View Library", "➕ Add Book", "🔍 Search Books", "📊 Statistics"],
        key="navigation"
    )
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    # Recent Activity
    if st.session_state.library:
        st.sidebar.markdown("### Recent Activity")
        st.sidebar.markdown('<div class="sidebar-stat">', unsafe_allow_html=True)
        recent_books = sorted(st.session_state.library, 
                            key=lambda x: x.get('added_date', ''), 
                            reverse=True)[:3]
        for book in recent_books:
            st.sidebar.markdown(f"📘 {book['title'][:20]}...")
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

    if page == "📖 View Library":
        st.header("Your Library")
        if not st.session_state.library:
            st.info("Your library is empty. Add some books!")
        else:
            # Create a dataframe for better display
            for book in st.session_state.library:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.subheader(book['title'])
                    st.write(f"By: {book['author']}")
                    st.write(f"Genre: {book['genre']} | Year: {book['year']}")
                with col2:
                    status = "✅ Read" if book['read'] else "📌 Unread"
                    st.write(status)
                with col3:
                    if st.button("Delete", key=f"del_{book['title']}"):
                        st.session_state.library.remove(book)
                        save_library(st.session_state.library)
                        st.experimental_rerun()
                st.divider()

    elif page == "➕ Add Book":
        st.header("Add New Book")
        with st.form("add_book_form"):
            title = st.text_input("Book Title")
            author = st.text_input("Author")
            col1, col2 = st.columns(2)
            with col1:
                year = st.text_input("Year")
            with col2:
                genre = st.text_input("Genre")
            read = st.checkbox("I have read this book")
            
            submitted = st.form_submit_button("Add Book")
            if submitted and title and author:
                new_book = {
                    "title": title,
                    "author": author,
                    "year": year,
                    "genre": genre,
                    "read": read,
                    "added_date": datetime.now().isoformat()  # Add timestamp
                }
                st.session_state.library.append(new_book)
                save_library(st.session_state.library)
                st.success(f"Book '{title}' added successfully!")
                st.balloons()

    elif page == "🔍 Search Books":
        st.header("Search Books")
        search_by = st.selectbox("Search by:", ["Title", "Author"])
        search_term = st.text_input(f"Enter {search_by}").lower()
        
        if search_term:
            results = [book for book in st.session_state.library 
                      if search_term in book[search_by.lower()].lower()]
            if results:
                st.subheader("Search Results")
                for book in results:
                    with st.container():
                        st.write(f"**{book['title']}** by {book['author']}")
                        st.write(f"Genre: {book['genre']} | Year: {book['year']}")
                        st.write("Status: " + ("✅ Read" if book['read'] else "📌 Unread"))
                        st.divider()
            else:
                st.info(f"No books found matching '{search_term}'")

    elif page == "📊 Statistics":
        st.header("Library Statistics")
        total_books = len(st.session_state.library)
        read_books = len([book for book in st.session_state.library if book['read']])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Books", total_books)
        with col2:
            st.metric("Read Books", read_books)
        with col3:
            percentage = (read_books / total_books * 100) if total_books > 0 else 0
            st.metric("Completion Rate", f"{percentage:.1f}%")

        # Genre Distribution
        if st.session_state.library:
            st.subheader("Genre Distribution")
            genres = {}
            for book in st.session_state.library:
                genres[book['genre']] = genres.get(book['genre'], 0) + 1
            st.bar_chart(genres)

if __name__ == '__main__':
    main()
    
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
