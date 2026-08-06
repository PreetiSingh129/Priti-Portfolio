from database.connection import get_connection
import streamlit as st
@st.cache_data(ttl=60)

def get_all_achievements():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM achievements ORDER BY id DESC"
    )

    achievements = cursor.fetchall()

    cursor.close()
    conn.close()

    return achievements


def delete_achievement(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM achievements WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()