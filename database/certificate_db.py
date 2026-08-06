from database.connection import get_connection
import os
import streamlit as st
@st.cache_data(ttl=60)

def get_all_certificates():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM certificates ORDER BY id DESC")

    certificates = cursor.fetchall()

    cursor.close()
    conn.close()

    return certificates


def delete_certificate(certificate_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Image path lo
    cursor.execute(
        "SELECT image FROM certificates WHERE id=%s",
        (certificate_id,)
    )

    certificate = cursor.fetchone()

    # File delete karo
    if certificate:

        image_path = certificate["image"]

        print("Image Path:", image_path)
        print("Exists:", os.path.exists(image_path))

        if image_path and os.path.exists(image_path):
            os.remove(image_path)

    # Database record delete karo
    cursor.execute(
        "DELETE FROM certificates WHERE id=%s",
        (certificate_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()