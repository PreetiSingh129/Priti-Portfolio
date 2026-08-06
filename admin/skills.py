import streamlit as st
from database.connection import get_connection
from database.skills_db import get_all_skills, delete_skill

# Initialize Session State
if "skill_edit_id" not in st.session_state:
    st.session_state["skill_edit_id"] = None

if "show_skill_form" not in st.session_state:
    st.session_state["show_skill_form"] = False
def skills_page():

    st.title("🛠 Skills Management")

    if "show_skill_form" not in st.session_state:
        st.session_state.show_skill_form = False

    if st.button("➕ Add Skill", use_container_width=True):
        st.session_state.show_skill_form = not st.session_state.show_skill_form

    if st.session_state.show_skill_form:
        add_skill_form()

    st.divider()

    show_skills()
def add_skill_form():

    with st.form("skill_form"):

        name = st.text_input("Skill Name *")

        category = st.selectbox(
            "Category",
            [
                "Programming",
                "Database",
                "Data Analysis",
                "Visualization",
                "Machine Learning",
                "Tools",
                "Web Development",
                "Other"
            ]
        )

        level = st.slider(
            "Skill Level",
            min_value=1,
            max_value=100,
            value=80
        )

        save = st.form_submit_button("💾 Save Skill")

    if save:

        if name.strip() == "":
            st.error("⚠ Skill name is required.")
            return

        try:

            conn = get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO skills
            (
                name,
                category,
                level
            )
            VALUES
            (%s,%s,%s)
            """

            values = (
                name,
                category,
                level
            )

            cursor.execute(query, values)
            conn.commit()

            st.success("✅ Skill Added Successfully")

            st.session_state.show_skill_form = False
            st.rerun()

        except Exception as e:

            st.error(f"❌ Database Error: {e}")

        finally:

            cursor.close()
            conn.close()

def show_skills():
    search = st.text_input(
    "🔍 Search Skill",
    placeholder="Search by skill name..."
)
    skills = get_all_skills()
    if search:

        skills = [

            skill

            for skill in skills

            if search.lower() in skill["name"].lower()

        ]
    if not skills:
        st.info("No Skills Added Yet")
        return

    for skill in skills:

        with st.container(border=True):

            st.subheader(skill["name"])

            st.write(f"📂 Category : {skill['category']}")

            st.progress(skill["level"])

            st.write(f"Level : {skill['level']}%")

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "✏ Edit",
                    key=f"edit_skill_{skill['id']}"
                ):

                    st.session_state["skill_edit_id"] = skill["id"]
                    st.rerun()

            with col2:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_skill_{skill['id']}"
                ):

                    delete_skill(skill["id"])

                    st.success("✅ Skill Deleted")

                    st.rerun()

            if st.session_state.get("skill_edit_id") == skill["id"]:
                edit_skill_form(skill)
def edit_skill_form(skill):

    st.markdown("### ✏ Edit Skill")

    with st.form(f"edit_skill_form_{skill['id']}"):

        name = st.text_input(
            "Skill Name",
            value=skill["name"]
        )

        category = st.selectbox(
            "Category",
            [
                "Programming",
                "Database",
                "Data Analysis",
                "Visualization",
                "Machine Learning",
                "Tools",
                "Web Development",
                "Other"
            ],
            index=[
                "Programming",
                "Database",
                "Data Analysis",
                "Visualization",
                "Machine Learning",
                "Tools",
                "Web Development",
                "Other"
            ].index(skill["category"])
            if skill["category"] in [
                "Programming",
                "Database",
                "Data Analysis",
                "Visualization",
                "Machine Learning",
                "Tools",
                "Web Development",
                "Other"
            ]
            else 0
        )

        level = st.slider(
            "Skill Level",
            1,
            100,
            value=skill["level"]
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
            UPDATE skills

            SET

            name=%s,
            category=%s,
            level=%s

            WHERE id=%s
            """,

            (
                name,
                category,
                level,
                skill["id"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        st.success("✅ Skill Updated Successfully")

        st.session_state["skill_edit_id"] = None

        st.rerun()

    if cancel:

        st.session_state["skill_edit_id"] = None

        st.rerun()