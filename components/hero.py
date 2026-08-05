
from database.profile_db import get_visitor_count
import streamlit as st

from database.profile_db import get_profile, get_dashboard_counts
visitor_count = get_visitor_count()
def hero_section():
    profile = get_profile()

    projects, skills, certificates = get_dashboard_counts()
    st.markdown(
    '<div class="fade-up">',
    unsafe_allow_html=True
)
    left, right = st.columns([2,1])

    with left:

        st.markdown(
            """
<h3 style="color:#A855F7;">
👋 Hello, I'm
</h3>
""",
            unsafe_allow_html=True,
        )

        st.markdown(f"""
<h1 style="
font-size:58px;
font-weight:800;
margin-bottom:5px;
background:linear-gradient(90deg,#A855F7,#EC4899);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">
{profile["name"]}
</h1>
""", unsafe_allow_html=True)
        
        st.markdown(f"""
<h3 style="
color:#CBD5E1;
font-weight:500;
margin-top:-10px;
">
{profile["tagline"]}
""", unsafe_allow_html=True)

        st.markdown(f"""
<p style="
font-size:17px;
line-height:1.8;
color:#CBD5E1;
">
{profile["bio"]}
</p>
""",
unsafe_allow_html=True
)
        st.write("")

        col1, col2, col3, = st.columns(3)

        with col1:
            st.link_button(
        "💻 GitHub",
        profile["github"],
        use_container_width=True
    )

        with col2:
            st.link_button(
        "🔗 LinkedIn",
        profile["linkedin"],
        use_container_width=True
    )

        with col3:

            with open(profile["resume"], "rb") as pdf:

                 st.download_button(
                    "📄 Download Resume",
                    data=pdf,
                    file_name="Priti_Kumari_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        st.write("")

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        cards = [
    ("🚀", "Projects", f"{projects}+"),
    ("🛠", "Skills", f"{skills}+"),
    ("🏆", "Certificates", f"{certificates}+"),
    
]


        for col, (icon, title, value) in zip([c1, c2, c3], cards):

            with col:

                st.markdown(
            f"""
<div class="metric-card">

<div class="metric-icon">
{icon}
</div>

<div class="metric-value">
{value}
</div>

<div class="metric-title">
{title}
</div>

</div>
""",
            unsafe_allow_html=True,
        )
    with right:
        
        st.image(
        profile["profile_image"],
        use_container_width=True
    )

        st.markdown(f"""
    <h2 style="text-align:center;margin-top:18px;color:white;">
    {profile["name"]}
    </h2>

    <p style="text-align:center;color:#CBD5E1;">
    {profile["role"]}
    </p>
    """, unsafe_allow_html=True)