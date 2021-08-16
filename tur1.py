import turtle as t
import time as ti
from itertools import cycle


def drawcircle(si, ang, fw):
    t.pencolor(next(li))
    t.circle(si)
    t.right(ang)
    t.forward(fw)
    drawcircle(si+5, ang+1, fw+5)


t.bgcolor("black")
t.speed("fast")
t.pensize(4)

li = cycle(["red", "dodger blue", "green", "orange", "purple", "grey", "white", "yellow"])

drawcircle(30, 0, 1)

ti.sleep(3)