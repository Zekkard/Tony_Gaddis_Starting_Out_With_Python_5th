import turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(-2,0)
turtle.write('STOP')
turtle.speed(10)
turtle.setheading(45)
turtle.write(turtle.position())
turtle.pendown()
for i in range (8):
    turtle.forward(90)
    turtle.right(45)
turtle.done()