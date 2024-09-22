import turtle
turtle.setheading(int(input('Введите угол:')))
if turtle.heading() > 0 and turtle.heading() < 45:
    turtle.penup()
    print('Перо было поднято.')