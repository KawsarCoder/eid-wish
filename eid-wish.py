import turtle as t
import random as r 
from typing import Text

def star():
    t.left(90)
    t.forward(90)
    t.pencolor('#d4ad4c')
    t.begin_fill()
    for i in range(5):
        t.color('#d4ad4c')
        t.forward(51)
        t.left(144)
    t.end_fill()

t.pen(pensize=5, pencolor="#d4ad4c")
t.bgcolor("#000000")
t.up()
t.goto(-50, 15)
t.down()
t.begin_fill()
t.color("#d4ad4c")
t.circle(120)
t.end_fill()

t.up()
t.goto(-20, 20)
t.down()
t.begin_fill()
t.color("#000000")
t.circle(120)
t.end_fill()

star()

for i in range(20):
    l=r.randint(5,12)
    x=r.randint(-650,650)
    y=r.randint(-350, 350)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.color("#d4ad4c")
        t.forward(1)
        t.left(144)
def write(massage, pos, color):
    x,y = pos
    t.color(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    style = ("serif", 40, "italic")
    t.write(massage, font=style)
write("Eid", (80, 25), "#d4ad4c")
write("Mubarak", (25, -25), "#d4ad4c")
write("Md. Kawsar", (10, -100), "#d4ad4c")

t.done()
