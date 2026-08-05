import streamlit as st
from database.achievements_db import get_all_achievements

def achievements_section():
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
🏆 Achievements & Leadership
</h1>
""", unsafe_allow_html=True)

    achievements = get_all_achievements()

    for achievement in achievements:

        st.markdown(
    f"""
<div class="timeline-item">

<div class="timeline-title">
🏆 {achievement["title"]}
</div>

<div class="timeline-org">
{achievement["organization"]}
</div>
<div class="timeline-desc">
{achievement["year"]}
</div>

<div class="timeline-desc">
{achievement["description"]}
</div>

</div>
""",
    unsafe_allow_html=True
)