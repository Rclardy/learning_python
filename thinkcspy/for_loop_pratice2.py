import turtle
wm = turtle.Screen()
t = turtle.Turtle()
sides = int(input("How many sides do you want your polygon to be?"))
lng = int(input("How long to you want your sides to be?"))
tcolor = input("What color do you want your turtle to be?")
cfill = input("What color do you want the fill to be?")
t.color(tcolor)
t.pencolor(tcolor)
t.fillcolor(cfill)
t.begin_fill()


for _ in range(sides):
    t.forward(lng)
    t.left(360/sides)
t.end_fill()
wm.exitonclick()
