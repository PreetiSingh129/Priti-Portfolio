import streamlit as st
from database.about_db import get_about
def about_section():
    about=get_about()
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
🚀 About
</h1>
""", unsafe_allow_html=True)
    left, right = st.columns([2, 1])

    # ---------------- Left Column ----------------

    with left:

        st.markdown(
            f"""
<div style="
background:#1E293B;
padding:30px;
border-radius:20px;
border-left:6px solid  #8B5CF6;
box-shadow:0px 8px 20px rgba(0,0,0,0.35);
">

<h2 style="color:white;">
👋 Hello!
</h2>

<p style="
font-size:17px;
line-height:1.8;
color:#CBD5E1;
">

I'm <b>{about['name']}</b>

{about['description']}

</div>
""",
            unsafe_allow_html=True,
        )

    # ---------------- Right Column ----------------

    with right:

        st.markdown("### 🎓 Education")

        st.success(about["degree"])

        st.success(about["college"])

        st.success(
        f"Current SGPA : {about['current_sgpa']}"
        )

        st.success(
        f"Highest SGPA : {about['highest_sgpa']}"
        )

    st.write("")

    # ---------------- Interests ----------------

    st.markdown("## 💜 Interests")

    c1, c2 = st.columns(2)

    with c1:
        st.info(about["interest1"])

        st.info(about["interest2"])

    with c2:
        st.info(about["interest3"])

        st.info(about["interest4"])

    st.write("")

    # ---------------- Career Goal ----------------

    st.markdown("## 🎯 Career Goal")

    st.markdown(
        f"""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
border-left:6px solid #10B981;
box-shadow:0px 6px 18px rgba(0,0,0,0.3);
">

<p style="
font-size:17px;
line-height:1.8;
color:#F8FAFC;
margin:0;
">

{about['career_goal']}

</p>

</div>
""",
        unsafe_allow_html=True,
    )