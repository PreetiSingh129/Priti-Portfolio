import streamlit as st
from database.connection import get_connection
from admin.dashboard import dashboard

def login():

    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT * FROM admin
        WHERE username=%s AND password=%s
        """

        cursor.execute(query, (username, password))

        admin = cursor.fetchone()

        cursor.close()
        conn.close()

        if admin:
            st.session_state["logged_in"] = True
            st.session_state["is_admin"] = True   # 👈 ye line add karo

            st.success("✅ Login Successful")
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

    