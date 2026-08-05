import streamlit as st
from database.message_db import (
    get_all_messages,
    delete_message
)

def messages_page():
    search = st.text_input(
    "🔍 Search Message",
    placeholder="Search by sender name..."
)
    st.title("📨 Messages")

    messages = get_all_messages()

    if search:
        messages = [msg for msg in messages if search.lower() in msg["name"].lower()]

    if not messages:

        st.info("No Messages Yet")
        return

    for msg in messages:

        with st.container(border=True):

            st.subheader(msg["name"])

            st.write(f"📧 {msg['email']}")

            if msg["subject"]:
                st.write(f"📌 Subject : {msg['subject']}")

            st.write(msg["message"])

            st.caption(f"🕒 {msg['created_at']}")

            if st.button(
                "🗑 Delete",
                key=f"delete_msg_{msg['id']}"
            ):

                delete_message(msg["id"])

                st.success("Message Deleted Successfully")

                st.rerun()