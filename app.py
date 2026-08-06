import streamlit as st
from components.hero import hero_section
from components.navbar import navbar
from components.about import about_section
from components.skills import skills_section
from components.projects import projects_section
from components.achievements import achievements_section
from components.certificates import certificates_section
from components.contact import contact_section
from components.footer import footer
from admin.login import login
from admin.dashboard import dashboard
from database.profile_db import increase_visitor
# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="Priti Kumari | Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Count only normal visitors, not admin

if not st.session_state.get("is_admin", False):

    if "visitor_counted" not in st.session_state:

        increase_visitor()

        st.session_state.visitor_counted = True
def load_css():

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.markdown("<div style='margin-top:15px'></div>", unsafe_allow_html=True)

selected = navbar()

st.markdown("<div style='margin-bottom:30px'></div>", unsafe_allow_html=True)
if selected == "Home":
    hero_section()

elif selected == "About":
    about_section()

elif selected == "Skills":
    skills_section()

elif selected == "Projects":
    projects_section()

elif selected == "Achievements & Leadership":
    achievements_section()

elif selected == "Certificates":
    certificates_section()

elif selected == "Contact":
    contact_section()

elif selected == "Admin":

    if st.session_state.get("logged_in", False):
        dashboard()
    else:
        login()
footer()

