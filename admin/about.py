import streamlit as st
from database.about_db import get_about, update_about


def about_page():

    st.title("📝 About Management")


    about = get_about()


    name = st.text_input(
        "Name",
        about["name"]
    )


    description = st.text_area(
        "Description",
        about["description"]
    )


    degree = st.text_input(
        "Degree",
        about["degree"]
    )


    college = st.text_input(
        "College",
        about["college"]
    )


    current_sgpa = st.text_input(
        "Current SGPA",
        about["current_sgpa"]
    )


    highest_sgpa = st.text_input(
        "Highest SGPA",
        about["highest_sgpa"]
    )


    interest1 = st.text_input(
        "Interest 1",
        about["interest1"]
    )


    interest2 = st.text_input(
        "Interest 2",
        about["interest2"]
    )


    interest3 = st.text_input(
        "Interest 3",
        about["interest3"]
    )


    interest4 = st.text_input(
        "Interest 4",
        about["interest4"]
    )


    career_goal = st.text_area(
        "Career Goal",
        about["career_goal"]
    )



    if st.button("💾 Update About"):

        update_about(
            (
            name,
            description,
            degree,
            college,
            current_sgpa,
            highest_sgpa,
            interest1,
            interest2,
            interest3,
            interest4,
            career_goal
            )
        )

        st.success(
            "About Updated Successfully"
        )