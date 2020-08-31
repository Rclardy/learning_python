# using turtle to pratice for loops.

import turtle
bob = turtle.Screen()
bob.bgcolor('blue')
bb = turtle.Turtle()

for _ in range(8):
    bb.forward(50)
    bb.left(360/8)

bob.exitonclick()
