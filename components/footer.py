import streamlit as st


def footer():

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="footer">

<div class="footer-line"></div>

<h4>
💜 Thanks for visiting my portfolio!
</h4>

<p>
Designed & Developed by <b>Priti Kumari</b>
</p>

<p>
© 2026 All Rights Reserved
</p>

</div>
""",
        unsafe_allow_html=True
    )