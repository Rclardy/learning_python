import turtle
wm = turtle.Screen()
bb = turtle.Turtle()

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    bb.forward(100)
    bb.left(i)


print(bb.heading())
