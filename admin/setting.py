import streamlit as st
from database.connection import get_connection


def settings_page():

    st.title("⚙️ Admin Settings")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM admin LIMIT 1")
    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    with st.form("change_credentials"):

        current_password = st.text_input(
            "Current Password",
            type="password"
        )

        new_username = st.text_input(
            "New Username",
            value=admin["username"]
        )

        new_password = st.text_input(
            "New Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        update = st.form_submit_button(
            "💾 Update Credentials"
        )

    if update:

        # Current password check
        if current_password != admin["password"]:

            st.error("❌ Current Password is incorrect.")
            return

        # Password match check
        if new_password != confirm_password:

            st.error("❌ New Password and Confirm Password do not match.")
            return

        # Empty password check
        if new_password.strip() == "":

            st.error("❌ Password cannot be empty.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE admin
            SET
            username=%s,
            password=%s
            WHERE id=%s
            """,
            (
                new_username,
                new_password,
                admin["id"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        st.success("✅ Credentials Updated Successfully")

        st.rerun()