import time
from turtle import*
bgcolor("black")
Trtl = [Turtle(), Turtle()]
x=6
ht()
for index, k in enumerate(Trtl):
    k.color("black")
    k.shape("circle")
    k.shapesize(0.3)
    k.width(3)
    k.pu()
    k.seth(90)
    k.fd(350)
    k.seth(-180)

Trtl[0].pu()
delay(0)
speed(150)
colors=["red"]
for k in colors:
    color(k)
    for k in range(360):
        Trtl[0].fd(x)
        Trtl[0].lt(1)
        pu()
        goto(Trtl[0].pos())
        pd()
        Trtl[1].fd(2 * x)
        Trtl[1].lt(2)
        goto(Trtl[1].pos())
time.sleep(2)
