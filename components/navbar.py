import streamlit as st
from streamlit_option_menu import option_menu


def navbar():

    selected = option_menu(
        menu_title=None,

        options=[
            "Home",
            "About",
            "Skills",
            "Projects",
            "Achievements & Leadership",
            "Certificates",
            "Contact",
            "Admin"          # NEW
        ],

        icons=[
            "house",
            "person",
            "code-slash",
            "folder",
            "trophy",
            "award",
            "telephone",
            "shield-lock"    # NEW
        ],

        orientation="horizontal",

        default_index=0,

        styles={

            "container":{
                "padding":"10px",
                "background-color":"#FFFFFF",
                "border-radius":"18px",
                "box-shadow":"0px 8px 25px rgba(0,0,0,.18)",
                "margin-bottom":"30px"
            },

            "nav-link":{
                "font-size":"17px",
                "font-weight":"600",
                "color":"#1E293B",
                "border-radius":"12px",
                "padding":"12px 18px",
                "--hover-color":"#F3F4F6",
            },

            "nav-link-selected":{
                "background":"linear-gradient(90deg,#7C3AED,#A855F7)",
                "color":"white",
                "border-radius":"12px",
                "font-weight":"700",
            }
        }
    )

    return selected