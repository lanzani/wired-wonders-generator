import streamlit as st

st.set_page_config(
    page_title="Generative Art Generator",
    page_icon="app/img/favicon.ico",
    layout="wide",
)

from streamlit_utils import load_css
from codes.tiling import render


def get_settings():
    pass

def get_canvas():
    return render()

def app():

    st.title("Tile Patterns")
    st.divider()

    settings_col, canvas_col = st.columns(2)


    with settings_col:
        get_settings()

    img = get_canvas()

    with canvas_col:

        st.image(img)


def main():
    load_css("app/style.css")

    app()


if __name__ == "__main__":

    main()