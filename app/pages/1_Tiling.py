import multiprocessing

import streamlit as st

st.set_page_config(
    page_title="Generative Art Generator",
    page_icon="app/img/favicon.ico",
    layout="wide",
)

import os
os.environ['DISPLAY'] = '0.0'

from streamlit_utils import load_css
from codes.tiling import render


def get_settings():
    pass

def get_canvas():



    return render()

def app():
    t = multiprocessing.Process(target=get_canvas)

    st.title("Tile Patterns")
    st.divider()

    settings_col, canvas_col = st.columns(2)


    with settings_col:
        st.write("Settings")
        get_settings()

    t.start()

    with canvas_col:

        st.image("tiling.png", use_column_width=True)


def main():
    load_css("app/style.css")

    app()


if __name__ == "__main__":

    main()