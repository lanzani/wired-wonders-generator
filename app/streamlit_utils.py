import streamlit as st

def load_css(css_file: str):
    """Read css from file"""

    with open(css_file, "r") as txt_file:
        css_style = txt_file.read()

    style_inside_html = f"<style> {css_style} </style>"

    st.markdown(style_inside_html, unsafe_allow_html=True)