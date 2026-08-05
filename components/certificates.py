import streamlit as st
from database.certificate_db import get_all_certificates
import base64
import os


def image_to_base64(path):

    if not path:
        return None

    if not os.path.exists(path):
        return None

    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def certificates_section():

    st.title("📜 Certificates")

    certificates = get_all_certificates()

    html = '<div class="certificate-gallery">'

    for certificate in certificates:

        img = image_to_base64(certificate.get("image"))

        html += '<div class="certificate-card">'

        if img:
            html += f'''
            <img src="data:image/png;base64,{img}">
            '''
        else:
            html += '''
            <div style="
                height:220px;
                display:flex;
                align-items:center;
                justify-content:center;
                background:#1f2937;
                color:white;
                border-radius:12px;
            ">
                No Image
            </div>
            '''

        html += f'''
        <div class="certificate-content">

            <div class="certificate-title">
                🏅 {certificate["title"]}
            </div>

            <div class="certificate-org">
                🏢 {certificate["issuer"]}
            </div>

        </div>

        </div>
        '''

    html += "</div>"

    st.html(html)