import math
from turtle import *
from .utils import set_theme, turtle_to_pil
import random


def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for _ in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step


def render_image(step_size=40, angle_step=1.00, n_steps=600):

    # TODO context manager
    # set_theme(tracer_value=100, hide_turtle=False)
    set_theme()


    # euler_curve(40, 1.00, 600)
    # euler_curve(2, 1.01, 100000)
    # euler_curve(3, 1.96, 100000)
    euler_curve(step_size, angle_step, n_steps)

    tracer(True)

    # Get turtle sketchbook and convert it into an image
    pil_image = turtle_to_pil()

    # Save the image
    pil_image.save("app/imgs/euler_spiral.png")



if __name__ == "__main__":


    render_image()


