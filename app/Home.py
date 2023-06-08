import streamlit as st

st.set_page_config(
    page_title="Generative Art Generator",
    page_icon="app/img/favicon.ico",
    layout="wide",
)

from streamlit_utils import load_css

def app():
    st.title("Generative Art Generator")
    st.divider()

def main():
    load_css("app/style.css")

    app()


if __name__ == "__main__":

    main()