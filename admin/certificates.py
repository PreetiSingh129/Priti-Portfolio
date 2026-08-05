import streamlit as st
import os
import uuid
from database.connection import get_connection
from database.certificate_db import (
    get_all_certificates,
    delete_certificate
)

def certificates_page():

    st.title("🏆 Certificate Management")

    if "show_certificate_form" not in st.session_state:
        st.session_state.show_certificate_form = False

    if st.button(
        "➕ Add Certificate",
        use_container_width=True
    ):
        st.session_state.show_certificate_form = (
            not st.session_state.show_certificate_form
        )

    if st.session_state.show_certificate_form:
        add_certificate_form()

    st.divider()

    show_certificates()
def add_certificate_form():

    with st.form("certificate_form"):

        title = st.text_input("Certificate Title *")

        issuer = st.text_input("Issued By *")

        image = st.file_uploader(
    "Certificate Image",
    type=["png", "jpg", "jpeg"],
    key="certificate_image"
)

        save = st.form_submit_button("💾 Save Certificate")

    if save:
        image_path = ""

        if image is not None:

            os.makedirs("assets/images", exist_ok=True)

            extension = image.name.split(".")[-1]

            filename = f"{uuid.uuid4()}.{extension}"

            image_path = os.path.abspath(os.path.join(
                "assets/certificates",
                filename
            ))

            with open(image_path, "wb") as f:
                f.write(image.getbuffer())

        if title.strip() == "" or issuer.strip() == "":

            st.error("⚠ Please fill all required fields.")

        else:

            try:

                conn = get_connection()
                cursor = conn.cursor()

                query = """
                INSERT INTO certificates
                (
                    title,
                    issuer,
                    image
                )
                VALUES
                (%s,%s,%s)
                """

                values = (
                    title,
                    issuer,
                    image_path
                )

                cursor.execute(query, values)

                conn.commit()

                st.success("✅ Certificate Added Successfully")

                st.session_state.show_certificate_form = False

                st.rerun()

            except Exception as e:

                st.error(f"❌ Database Error: {e}")

            finally:

                cursor.close()
                conn.close()
def show_certificates():
    search = st.text_input(
    "🔍 Search Certificate",
    placeholder="Search by certificate title..."
)
    certificates = get_all_certificates()
    
    if search:
        certificates = [certificate for certificate in certificates if search.lower() in certificate["title"].lower()]

    if not certificates:

        st.info("No Certificates Added Yet")

        return

    for certificate in certificates:

        with st.container(border=True):

            st.subheader(certificate["title"])

            st.write(f"🏢 Issued By : {certificate['issuer']}")

            st.write(f"🖼 Image : {certificate['image']}")

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "✏ Edit",
                    key=f"edit_certificate_{certificate['id']}"
                ):

                    st.session_state.certificate_edit_id = certificate["id"]

                    st.rerun()

            with col2:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_certificate_{certificate['id']}"
                ):

                    delete_certificate(certificate["id"])

                    st.success("✅ Certificate Deleted Successfully")

                    st.rerun()
            if st.session_state.get("certificate_edit_id") == certificate["id"]:
            
                edit_certificate_form(certificate)
def edit_certificate_form(certificate):

    st.markdown("### ✏ Edit Certificate")

    with st.form(f"edit_certificate_{certificate['id']}"):

        title = st.text_input(
            "Certificate Title",
            value=certificate["title"]
        )
        issuer = st.text_input(
    "Issued By",
    value=certificate["issuer"]
)

        st.write("Current Image")

        if certificate["image"]:
            st.image(
                certificate["image"],
                width=200
            )

        new_image = st.file_uploader(
            "Upload New Image",
            type=["png","jpg","jpeg"],
            key=f"edit_cert_{certificate['id']}"
        )
        image = st.text_input(
            "Image Path",
            value=certificate.get("image") or ""
        )

        col1, col2 = st.columns(2)

        with col1:
            update = st.form_submit_button("💾 Update")

        with col2:
            cancel = st.form_submit_button("❌ Cancel")

    if update:
        image_path = certificate["image"]

        if new_image is not None:

            os.makedirs("assets/images", exist_ok=True)

            extension = new_image.name.split(".")[-1]

            filename = f"{uuid.uuid4()}.{extension}"

            image_path = os.path.join(
                "assets/images",
                filename
            )

            with open(image_path,"wb") as f:
                f.write(new_image.getbuffer())
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE certificates

            SET

            title=%s,
            issuer=%s,
            image=%s

            WHERE id=%s
            """,

            (
                title,
                issuer,
                image_path,
                certificate["id"]
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        st.success("✅ Certificate Updated Successfully")

        st.session_state.certificate_edit_id = None

        st.rerun()

    if cancel:

        st.session_state.certificate_edit_id = None

        st.rerun()