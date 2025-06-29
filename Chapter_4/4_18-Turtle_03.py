import turtle
turtle.penup()
turtle.goto(110,155)
turtle.setheading(270)
turtle.speed(10)
turtle.pendown()
turtle.hideturtle()
for i in range (244,1,-5):
    turtle.forward(i)
    turtle.right(90)
turtle.done()