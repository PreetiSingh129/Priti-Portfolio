import streamlit as st
from database.profile_db import get_visitor_count
from admin.projects import project_page
from admin.skills import skills_page
from admin.certificates import certificates_page
from admin.achievements import achievements_page
from admin.profile import profile_page
from admin.messages import messages_page
from database.profile_db import get_dashboard_stats
from admin.setting import settings_page
def dashboard():
    visitor_count = get_visitor_count()
    st.title("📊 Admin Panel")
   
    stats = get_dashboard_stats()

    st.success("Welcome Back 👋")

    c1, c2, c3, c4, c5,c6= st.columns(6)

    with c1:
        st.metric(
            "📂 Projects",
            stats["projects"]
        )

    with c2:
        st.metric(
            "🛠 Skills",
            stats["skills"]
        )

    with c3:
        st.metric(
            "🏆 Certificates",
            stats["certificates"]
        )

    with c4:
        st.metric(
            "🏅 Achievements",
            stats["achievements"]
        )

    with c5:
        st.metric(
            "📨 Messages",
            stats["messages"]
        )
    with c6:
        st.metric(
        "👁 Visitors",
        visitor_count
    )
    st.divider()
    
    menu = st.sidebar.radio(

        "Portfolio Manager",

        [

            "📂 Projects",
            "🛠 Skills",
            "🏆 Certificates",
            "🎯 Achievements",
            "👤 Profile",
            "📝 About",
            "📨 Messages",
            "⚙️ Settings",
            "🚪 Logout"

        ]

    )
    

    if menu == "📂 Projects":

        project_page()

    elif menu == "🛠 Skills":

        skills_page()

    elif menu == "🏆 Certificates":

        certificates_page()

    elif menu == "🎯 Achievements":

        achievements_page()

    elif menu == "👤 Profile":

        profile_page()
    elif menu == "📝 About":

        about_page()

    elif menu == "📨 Messages":

        messages_page()
    elif menu == "⚙️ Settings":

        settings_page()

    elif menu == "🚪 Logout":

        st.session_state["logged_in"] = False

        st.rerun()
