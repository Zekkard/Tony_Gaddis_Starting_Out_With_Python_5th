import turtle
turtle.penup()
turtle.goto(350,-350)
turtle.speed(0)
turtle.pendown()
turtle.hideturtle()
for i in range(10,800,5):
    turtle.setheading(180)
    turtle.forward(i)
    turtle.setheading(90)
    turtle.forward(i)
    turtle.setheading(0)
    turtle.forward(i)
    turtle.setheading(270)
    turtle.forward(i)
turtle.done()