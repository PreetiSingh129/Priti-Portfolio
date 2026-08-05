import streamlit as st
from database.profile_db import get_profile
from database.message_db import save_message
def contact_section():
    profile = get_profile()
    st.markdown("""
    <h1 style='font-size:42px;font-weight:700;color:white;'>
    📞 Let's Connect
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
    display:inline-block;
    padding:10px 18px;
    background:linear-gradient(90deg,#22C55E,#16A34A);
    color:white;
    border-radius:999px;
    font-weight:600;
    margin-bottom:25px;
    box-shadow:0 8px 20px rgba(34,197,94,.30);
    ">
    🟢 Available for Internships & Full-Time Opportunities
    </div>
    """, unsafe_allow_html=True)


    left, right = st.columns([1,1])


    with left:

        st.markdown(f"""
        <div class="contact-card">

        <h3>📧 Email</h3>

        <a href="mailto:{profile["email"]}"
        style="color:#A855F7;text-decoration:none;font-size:17px;">
        {profile["email"]}
        </a>


        <h3>📱 Phone</h3>
        <p>{profile["phone"]}</p>


        <h3>📍 Location</h3>
        <p>{profile["location"]}</p>

        </div>
        """, unsafe_allow_html=True)



    with right:

        st.markdown("""
        <div class="contact-card">

        <h3>🌐 Connect With Me</h3>

        <p>
        I'm open to opportunities in 
        Data Analytics, Python Development,
        AI/ML and Software Development roles.
        </p>

        </div>
        """, unsafe_allow_html=True)



    st.link_button(
        "💼 LinkedIn",
        profile["linkedin"],
        use_container_width=True
    )


    st.link_button(
        "💻 GitHub",
        profile["github"],
        use_container_width=True
    )


    with open(profile["resume"], "rb") as pdf:
                    st.download_button(
                                "📄 Download Resume",
                                data=pdf,
                                file_name="Priti_Kumari_Resume.pdf",
                                mime="application/pdf",
                                use_container_width=True
                        )


    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()
    st.markdown("## 💬 Send Me a Message")

    with st.form("contact_form"):

        name = st.text_input("Your Name")

        email = st.text_input("Your Email")

        subject = st.text_input("Subject")

        message = st.text_area(
            "Message",
            height=150
        )

        send = st.form_submit_button("📨 Send Message")
    if send:

        if (
            name.strip() == "" or
            email.strip() == "" or
            message.strip() == ""
        ):

            st.error("⚠ Please fill all required fields.")

        else:

            save_message(
                name,
                email,
                subject,
                message
            )

            st.success(
                "✅ Thank you! Your message has been sent."
            )