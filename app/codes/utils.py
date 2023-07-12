import turtle
from PIL import Image
import io


def turtle_to_pil():
    """Convert turtle sketchbook to PIL image"""
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