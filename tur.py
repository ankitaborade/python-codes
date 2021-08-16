import turtle as t
import time as ti

def rect(hori, ver, col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
             t.forward(hori)
             t.right(90)
             t.forward(ver)
             t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed(150)

t.bgcolor("dodger blue")  #background color
t.goto(-100, - 150)

rect(50, 20, "blue")  # foots
t.goto(-30, -150)
rect(50, 20, "blue")
t.goto(-25, -50)

rect(15, 100, "grey") #legs
t.goto(-70, -50)
rect(15, 100, "grey")
t.goto(-90, 100)

rect(100, 150, "red") # body
t.goto(-150, 70)

rect(60, 15, "grey") # arms
t.goto(-150, 110)
rect(15, 40, "grey")
t.goto(10, 70)
rect(60, 15, "grey")
t.goto(55, 110)
rect(15, 40, "grey")
t.goto(-50, 120)
rect(15, 20, "grey")
t.goto(-85, 170)

rect(80, 50, "red") #face
t.goto(-60, 160)

rect(30, 10, "white")  # eyes
t.goto(-55, 155)
rect(5, 5, "black")
t.goto(-40, 155)
rect(5, 5, "black")
t.goto(-65, 138)

rect(40, 5, "black")


t.goto(-155, 130) # right hand
rect(25, 25, "green")
t.goto(-147, 130)
rect(10, 15, "dodger blue")

t.goto(50, 130)   # left hand
rect(25, 25, "green")
t.goto(58, 130)
rect(10, 15, "dodger blue")

t.hideturtle()
ti.sleep(10)