import streamlit as st
from database.connection import get_connection
@st.cache_data(ttl=60)
def get_all_projects():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM projects ORDER BY id DESC"

    cursor.execute(query)

    projects = cursor.fetchall()

    cursor.close()
    conn.close()

    return projects

def update_project(id, title, description, technologies, github, demo, image, highlights):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE projects

    SET

        title=%s,
        description=%s,
        technologies=%s,
        github=%s,
        demo=%s,
        image=%s
        highlights=%s
    WHERE id=%s
    """

    values = (
        title,
        description,
        technologies,
        github,
        demo,
        image,
        id,
        highlights
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

def delete_project(id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM projects
    WHERE id=%s
    """

    cursor.execute(query, (id,))

    conn.commit()

    cursor.close()
    conn.close()