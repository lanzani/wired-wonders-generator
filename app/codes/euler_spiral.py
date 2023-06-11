import io
import math
import turtle
import random

from PIL import Image


def turtle_to_pil():
    """Convert turtle canvas to PIL image"""
    ps = turtle.getscreen().getcanvas().postscript()
    return Image.open(io.BytesIO(ps.encode('utf-8')))

def set_theme(canvas_width=1000, canvas_height=1000, canvas_color="#ffffff", pen_color="#000000", thickness=2, speed_value=0, tracer_value=False, hide_turtle=True):
    turtle.setup(canvas_width, canvas_height)
    turtle.bgcolor(canvas_color)
    turtle.width(thickness)
    turtle.color(pen_color)
    turtle.speed(speed_value)
    turtle.tracer(tracer_value)
    if hide_turtle:
        turtle.hideturtle()


def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for _ in range(n_steps):
        turtle.right(angle)
        turtle.forward(step_size)
        angle += angle_step


def render():
    set_theme()


    euler_curve(40, 1.00, 600)
    # euler_curve(2, 1.01, 100000)
    # euler_curve(3, 1.96, 100000)

    pil_image = turtle_to_pil()

    turtle.tracer(True)
    # turtle.done()
    # turtle.exitonclick()

    pil_image.save("euler_spiral.png")

    return pil_image

if __name__ == "__main__":




    render()



