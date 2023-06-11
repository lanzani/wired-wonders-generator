import multiprocessing

import streamlit as st

st.set_page_config(
    page_title="Generative Art Generator",
    page_icon="app/img/favicon.ico",
    layout="wide",
)


from streamlit_utils import load_css
from codes.euler_spiral import render_image


def get_settings():
    step_size = st.number_input("Step size", min_value=1, max_value=100, value=2, step=1)
    angle_step = st.number_input("Angle step", min_value=0.01, max_value=360.0, value=1.01, step=0.01)
    n_steps = st.number_input("Number of steps", min_value=100, max_value=100000, value=100000, step=100)

    return step_size, angle_step, n_steps

# def get_canvas():
#     return render_image()

def app():

    st.title("Tile Patterns")
    st.divider()

    settings_col, canvas_col = st.columns(2)


    with settings_col:
        st.write("Settings")
        step_size, angle_step, n_steps = get_settings()

        btn = st.button("Refresh")

    t = multiprocessing.Process(target=render_image, args=(step_size, angle_step, n_steps))
    t.start()
    t.join()

    with canvas_col:
        st.image("app/imgs/euler_spiral.png", use_column_width=True)


def main():
    load_css("app/style.css")

    app()


if __name__ == "__main__":

    main()
