import streamlit as st
import os
import uuid
from database.connection import get_connection
if "edit_id" not in st.session_state:
    st.session_state.edit_id = None

# ---------------- DATABASE ---------------- #

def get_projects():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM projects ORDER BY id DESC")

    projects = cursor.fetchall()

    cursor.close()
    conn.close()

    return projects


# ---------------- PAGE ---------------- #

def project_page():

    st.title("📂 Project Management")

    if "show_add_form" not in st.session_state:
        st.session_state.show_add_form = False

    if st.button("➕ Add New Project", use_container_width=True):

        st.session_state.show_add_form = (
            not st.session_state.show_add_form
        )

    if st.session_state.show_add_form:

        add_project_form()

    st.divider()

    show_projects()

def add_project_form():

    with st.form("project_form"):

        title = st.text_input("Project Title")

        description = st.text_area("Description")

        technologies = st.text_area(
            "Technologies",
            placeholder="""Example

Python
SQL
Power BI
Streamlit"""
        )

        highlights = st.text_area(
            "Highlights",
            placeholder="""Example

Interactive Dashboard
EDA
Prediction"""
        )

        github = st.text_input("Github Link")

        demo = st.text_input("Live Demo")

        image = st.file_uploader(
    "Project Image",
    type=["png", "jpg", "jpeg"]
)

        save = st.form_submit_button("💾 Save Project")

    if save:
        image_path = ""

        if image is not None:

            if not os.path.exists("assets/images"):
                os.makedirs("assets/images")

            extension = image.name.split(".")[-1]

            filename = f"{uuid.uuid4()}.{extension}"

            image_path =  os.path.abspath(os.path.join(
                "assets/images",
                filename
            ))

            with open(image_path, "wb") as f:
                f.write(image.getbuffer())
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO projects
        (

        title,

        description,

        technologies,

        highlights,

        github,

        demo,

        image

        )

        VALUES

        (%s,%s,%s,%s,%s,%s,%s)

        """,

        (

        title,

        description,

        technologies,

        highlights,

        github,

        demo,

        image_path

        )

        )

        conn.commit()

        cursor.close()

        conn.close()

        st.success("Project Added Successfully 🎉")

        st.session_state.show_add_form = False

        st.rerun()

def show_projects():
    search = st.text_input(
    "🔍 Search Project",
    placeholder="Search by title..."
)
    projects = get_projects()

    if not projects:

        st.info("No Projects Added Yet")

        return

    # Filter projects based on search query
    if search:
        projects = [project for project in projects if search.lower() in project["title"].lower()]

    for project in projects:

        with st.container(border=True):

            st.subheader(project["title"])

            st.write(project["description"])

            st.markdown("### 🛠 Technologies")

            technologies = project.get("technologies") or ""

            for tech in technologies.split("\n"):

                if tech.strip():

                    st.markdown(f"✅ {tech}")

            st.markdown("### ⭐ Highlights")

            highlights = project.get("highlights") or ""

            for item in highlights.split("\n"):

                if item.strip():
                    st.markdown(f"⭐ {item}")

            col1,col2=st.columns(2)

            with col1:

                if st.button(
                    "✏ Edit",
                    key=f"edit_{project['id']}"
                ):
                    st.session_state.edit_id = project["id"]
                    st.rerun()

            with col2:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{project['id']}"
                ):

                    try:
                        # Delete image file from folder
                        if project["image"] and os.path.exists(project["image"]):
                            os.remove(project["image"])
                        conn = get_connection()
                        cursor = conn.cursor()

                        cursor.execute(
                            "DELETE FROM projects WHERE id=%s",
                            (project["id"],)
                        )

                        conn.commit()

                        st.success("✅ Project Deleted Successfully")

                        st.rerun()

                    except Exception as e:

                        st.error(f"❌ Error deleting project: {e}")

                    finally:
                        if'cursor' in locals():
                            cursor.close()
                        if'conn' in locals():
                            conn.close()          
                if st.session_state.get("edit_id") == project["id"]:

                    st.markdown("### ✏ Edit Project")

                    with st.form(f"edit_form_{project['id']}"):

                        title = st.text_input(
                            "Project Title",
                            value=project.get("title") or ""
                        )

                        description = st.text_area(
                            "Description",
                            value=project.get("description") or ""
                        )

                        technologies = st.text_area(
                            "Technologies",
                            value=project.get("technologies") or ""
                        )

                        highlights = st.text_area(
                            "Highlights",
                            value=project.get("highlights") or ""
                        )

                        github = st.text_input(
                            "Github",
                            value=project.get("github") or ""
                        )

                        demo = st.text_input(
                            "Demo",
                            value=project.get("demo") or ""
                        )

                        image_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png", "webp"]
)

                        update = st.form_submit_button("💾 Update")

                        if update:

                            new_image_path = project["image"]

                            if image_file is not None:

                                if not os.path.exists("assets/images"):
                                    os.makedirs("assets/images")

                                extension = image_file.name.split(".")[-1]
                                filename = f"{uuid.uuid4()}.{extension}"

                                new_image_path = os.path.abspath(
                                    os.path.join("assets/images", filename)
                                )

                                with open(new_image_path, "wb") as f:
                                    f.write(image_file.getbuffer())

                            try:

                                conn = get_connection()
                                cursor = conn.cursor()

                                query = """
                                UPDATE projects
                                SET
                                    title=%s,
                                    description=%s,
                                    technologies=%s,
                                    highlights=%s,
                                    github=%s,
                                    demo=%s,
                                    image=%s
                                WHERE id=%s
                                """

                                values = (
                                    title,
                                    description,
                                    technologies,
                                    highlights,
                                    github,
                                    demo,
                                    new_image_path,
                                    project["id"]
                                )

                                cursor.execute(query, values)
                                conn.commit()

                                st.success("✅ Project Updated Successfully")

                                st.session_state.edit_id = None

                                st.rerun()

                            except Exception as e:

                                st.error(f"❌ Update Error: {e}")

                            finally:

                                cursor.close()
                                conn.close()