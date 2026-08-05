import streamlit as st
from database.project_db import get_all_projects
import os

def projects_section():

    st.markdown('<div class="fade-up">', unsafe_allow_html=True)

    st.markdown("""
    <h1 style="
    color:#F8FAFC;
    font-size:42px;
    font-weight:700;
    margin-bottom:30px;
    ">
    🚀 Projects
    </h1>
    """, unsafe_allow_html=True)

    projects = get_all_projects()

    for project in projects:

        left, right = st.columns([1,1.2], gap="large")

        with left:

            if os.path.exists(project["image"]):
                st.image(project["image"], use_container_width=True)

        with right:

            st.markdown(f"""
<div class="project-card">

<h2>{project["title"]}</h2>

<p>
{project["description"]}
</p>

</div>
""", unsafe_allow_html=True)

            st.markdown("#### 🛠 Technologies")

            technologies = (
                project.get("technologies") or ""
            ).split("\n")

            technologies = [tech.strip() for tech in technologies if tech.strip()]

            if technologies:

                cols = st.columns(len(technologies))

                for col, tech in zip(cols, technologies):

                    with col:

                        st.markdown(
                            f'<div class="tech-badge">{tech}</div>',
                            unsafe_allow_html=True
                        )

            st.write("")

            st.markdown("#### ⭐ Key Highlights")

            highlights = (
                project.get("highlights") or ""
            ).split("\n")

            for item in highlights:

                if item.strip():

                    st.markdown(f"✅ {item}")
            st.write("")

            c1, c2 = st.columns(2)

            with c1:
                st.link_button(
                    "💻 GitHub",
                    project["github"],
                    use_container_width=True
                )

            with c2:
                if project["demo"] != "":
                    st.link_button(
                        "🌐 Live Demo",
                        project["demo"],
                        use_container_width=True
                    )

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)