import streamlit as st
from database.skills_db import get_all_skills
import streamlit as st

if "skill_edit_id" not in st.session_state:
    st.session_state.skill_edit_id = None
skills = get_all_skills()
icons = {
    "Python": "🐍",
    "Java (Basics)": "☕",
    "SQL": "🗄️",
    "Power BI": "📊",
    "Excel": "📈",
    "Pandas": "🐼",
    "NumPy": "🔢",
    "Scikit-learn": "🤖",
    "Git": "🌿",
    "GitHub": "🐙",
    "Streamlit": "🎈",
    "VS Code": "💻"
}

def skills_section():
    st.markdown(
    '<div class="fade-up">',
    unsafe_allow_html=True
)
    st.markdown("""
<h1 style="
color:#F8FAFC;
font-size:42px;
font-weight:700;
margin-bottom:25px;
">
💻 Skills
</h1>
""", unsafe_allow_html=True)


    skills = skills = get_all_skills()

    current_category = ""

    for skill in skills:

        if current_category != skill["category"]:

            current_category = skill["category"]

            st.markdown(
f"""
<div style="
background:#1E293B;
padding:18px 22px;
margin-top:30px;
margin-bottom:18px;
border:1px solid #334155;
border-left:6px solid #8B5CF6;
border-radius:16px;
box-shadow:0px 6px 18px rgba(0,0,0,0.25);
">

<h2 style="
margin:0;
color:#F8FAFC;
font-size:26px;
font-weight:700;
">
📂 {current_category}
</h2>

</div>
""",
unsafe_allow_html=True
)

        
        col1, col2 = st.columns([5,1])

        with col1:
            st.markdown(
                f"<span style='color:#F8FAFC;font-size:18px;font-weight:600;'>{icons.get(skill['name'],'✅')} {skill['name']}</span>",
        unsafe_allow_html=True,
    )

        with col2:
            st.markdown(
                f"<p style='text-align:right;color:#8B5CF6;font-weight:700;'>{skill['level']}%</p>",
        unsafe_allow_html=True,
    )
        st.progress(skill["level"] / 100)
        st.write("")
    st.markdown(
    "</div>",
    unsafe_allow_html=True
)