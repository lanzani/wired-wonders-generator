import io
import os
import tkinter
from turtle import *

import random

from PIL import Image


def tiling(x, y, size, depth, mode="straight"):

    if depth == 0:

        if mode == "straight":

            if random.random() < 0.5:
                # vertical lines
                penup()
                goto(x, y-size)
                pendown()
                goto(x, y+size)

            else:
                # horizontal lines
                penup()
                goto(x-size, y)
                pendown()
                goto(x+size, y)

        elif mode == "diagonal":
            if random.random() < 0.5:
                # top left to bottom right
                penup()
                goto(x-size, y + size)
                pendown()
                goto(x+ size, y - size)

            else:
                # bottom left to top right
                penup()
                goto(x - size, y- size)
                pendown()
                goto(x + size, y+ size)


    else:
        size /= 2
        depth -= 1
        tiling(x-size, y+size, size, depth, mode)
        tiling(x+size, y+size, size, depth, mode)
        tiling(x-size, y-size, size, depth, mode)
        tiling(x+size, y-size, size, depth, mode)


def turtle_to_pil():
    """Convert turtle canvas to PIL image"""
    ps = getscreen().getcanvas().postscript()
    return Image.open(io.BytesIO(ps.encode('utf-8')))


def render():

    hideturtle()

    setup(1000, 1000)
    tracer(False)

    width(3)
    tiling(0, 0, 400, 3, "diagonal")

    tracer(True)


    # Get turtle canvas and convert it into an image
    pil_image = turtle_to_pil()


    # Save the image
    pil_image.save("tiling.png")


    # exitonclick()


    return pil_image

# def render():
#     main = tkinter.Tk()
#     main.withdraw()
#     canv = tkinter.Canvas(master=main)
#     turt = turtle.RawTurtle(canv)
#
#     turt.pendown()
#     turt.forward(100)
#
#
#
#     pil_image = turtle_to_pil()
#
#     pil_image.save("tiling1.png")



if __name__ == "__main__":
    render()


