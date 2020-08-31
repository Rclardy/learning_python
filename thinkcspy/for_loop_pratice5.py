# making a clock face with turtle

import turtle
wm = turtle.Screen()
bb = turtle.Turtle()

bb.color('blue')
wm.bgcolor('green')
bb.shape('turtle')
bb.stamp()
bb.pu()
for i in range(12):
    bb.fd(100)
    bb.pd()
    bb.fd(20)
    bb.pu()
    bb.fd(20)
    bb.stamp()
    bb.bk(140)
    bb.rt(30)

wm.exitonclick()
