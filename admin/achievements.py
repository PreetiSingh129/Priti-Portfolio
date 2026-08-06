import streamlit as st
from database.connection import get_connection
from database.achievements_db import (
    get_all_achievements,
    delete_achievement
)

if "achievement_edit_id" not in st.session_state:
    st.session_state["achievement_edit_id"] = None

if "show_achievement_form" not in st.session_state:
    st.session_state["show_achievement_form"] = False


def achievements_page():

    st.title("🏅 Achievement Management")

    if st.button(
        "➕ Add Achievement",
        use_container_width=True
    ):
        st.session_state["show_achievement_form"] = (
            not st.session_state.get("show_achievement_form", False)
)

    if st.session_state.get("show_achievement_form", False):
        add_achievement_form()

    st.divider()

    show_achievements()
def add_achievement_form():

    with st.form("achievement_form"):

        title = st.text_input("Achievement Title")

        organization = st.text_input("Organization")

        year = st.text_input("Year")

        description = st.text_area("Description")

        save = st.form_submit_button("💾 Save")

    if save:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO achievements
            (
                title,
                organization,
                year,
                description
            )

            VALUES
            (%s,%s,%s,%s)
            """,

            (
                title,
                organization,
                year,
                description
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        st.success("Achievement Added Successfully 🎉")

        st.session_state["show_achievement_form"] = False

        st.rerun()
def show_achievements():
    search = st.text_input(
    "🔍 Search Achievement",
    placeholder="Search by title..."
)
    achievements = get_all_achievements()
    
    if search:
        achievements = [achievement for achievement in achievements if search.lower() in achievement["title"].lower()]

    if not achievements:

        st.info("No Achievements Added Yet")
        return

    for achievement in achievements:

        with st.container(border=True):

            st.subheader(achievement["title"])

            st.write(f"🏢 Organization : {achievement['organization']}")

            st.write(f"📅 Year : {achievement['year']}")

            st.write(achievement["description"])

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "✏ Edit",
                    key=f"edit_achievement_{achievement['id']}"
                ):

                    st.session_state["achievement_edit_id"] = achievement["id"]

                    st.rerun()

            with col2:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_achievement_{achievement['id']}"
                ):

                    delete_achievement(achievement["id"])

                    st.success("Achievement Deleted Successfully")

                    st.rerun()

            if st.session_state.get("achievement_edit_id") == achievement["id"]:

                edit_achievement_form(achievement)
def edit_achievement_form(achievement):

    st.markdown("### ✏ Edit Achievement")

    with st.form(f"edit_form_{achievement['id']}"):

        title = st.text_input(
            "Title",
            value=achievement["title"]
        )

        organization = st.text_input(
            "Organization",
            value=achievement["organization"]
        )

        year = st.text_input(
            "Year",
            value=achievement["year"]
        )

        description = st.text_area(
            "Description",
            value=achievement["description"]
        )

        col1, col2 = st.columns(2)

        with col1:

            update = st.form_submit_button("💾 Update")

        with col2:

            cancel = st.form_submit_button("❌ Cancel")

    if update:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE achievements

            SET

            title=%s,
            organization=%s,
            year=%s,
            description=%s

            WHERE id=%s
            """,

            (

                title,
                organization,
                year,
                description,
                achievement["id"]

            )
        )

        conn.commit()

        cursor.close()

        conn.close()

        st.success("Achievement Updated Successfully 🎉")

        st.session_state.get("achievement_edit_id") = None

        st.rerun()

    if cancel:

        st.session_state.get("achievement_edit_id") = None

        st.rerun()