import streamlit as st
from database.connection import get_connection
from database.profile_db import get_profile
import os



def profile_page():
    profile = get_profile()
    st.write("Current Profile Image")

    if profile["profile_image"]:
        st.image(
            profile["profile_image"],
            width=180
        )

    st.title("👤 Profile Management")

    

    with st.form("profile_form"):

        name = st.text_input(
            "Name",
            value=profile["name"]
        )

        role = st.text_input(
            "Role",
            value=profile["role"]
        )

        tagline = st.text_input(
            "Tagline",
            value=profile["tagline"]
        )

        bio = st.text_area(
            "Bio",
            value=profile["bio"]
        )

        github = st.text_input(
            "GitHub",
            value=profile["github"]
        )

        linkedin = st.text_input(
            "LinkedIn",
            value=profile["linkedin"]
        )

        resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

        profile_image = st.file_uploader(
    "Upload Profile Image",
    type=["png", "jpg", "jpeg"]
)
        email = st.text_input(
    "Email",
    profile["email"]
)

        phone = st.text_input(
    "Phone",
    profile["phone"]
)

        location = st.text_input(
    "Location",
    profile["location"]
)

        update = st.form_submit_button("💾 Update Profile")

    if update:
        image_path = profile["profile_image"]

        if profile_image is not None:

            profile_folder = "assets/profile"

            os.makedirs(profile_folder, exist_ok=True)


            # Remove old image
            for old_file in os.listdir(profile_folder):
                old_path = os.path.join(profile_folder, old_file)

                if os.path.isfile(old_path):
                    os.remove(old_path)


            extension = profile_image.name.split(".")[-1]

            filename = f"profile.{extension}"

            image_path = os.path.join(
                profile_folder,
                filename
            )


            with open(image_path, "wb") as f:
                f.write(profile_image.getbuffer())

        resume_path = profile["resume"]

        if resume is not None:

            resume_folder = "assets/resume"

            os.makedirs(resume_folder, exist_ok=True)


            # Delete old resume
            for old_file in os.listdir(resume_folder):
                old_path = os.path.join(resume_folder, old_file)

                if os.path.isfile(old_path):
                    os.remove(old_path)


            # Save new resume
            resume_path = os.path.join(
                resume_folder,
                "resume.pdf"
            )


            with open(resume_path, "wb") as f:
                f.write(resume.getbuffer())
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
    """
    UPDATE profile
    SET
    name=%s,
    role=%s,
    tagline=%s,
    bio=%s,
    github=%s,
    linkedin=%s,
    resume=%s,
    profile_image=%s,
    email=%s,
    phone=%s,
    location=%s
    WHERE id=%s
    """,
    (
        name,
        role,
        tagline,
        bio,
        github,
        linkedin,
        resume_path,
        image_path,
        email,
        phone,
        location,
        profile["id"]
    )
)

        conn.commit()
        st.cache_data.clear()
        cursor.close()

        conn.close()

        st.success("✅ Profile Updated Successfully")

        st.rerun()