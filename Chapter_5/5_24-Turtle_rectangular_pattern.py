# Черепашья графика: прямоугольный узор. В программе напишите функцию
# drawPattern, которая использует библиотеку черепашьей графики, чтобы нарисовать
# прямоугольный узор (рис. 5.31). Функция drawPattern должна принимать два аргумента:
# один из них задает ширину узора, другой - его высоту. (Пример, приведенный на
# рис. 5.31, показывает, как узор будет выглядеть, когда ширина и высота одинаковые.)
# Когда программа выполняется, она должна запросить у пользователя ширину и высоту
# узора и затем передать эти значения в качестве аргументов в функцию drawPattern.

# Импорт библиотек:
import turtle

# Константы:
SPEED = 0
BASE_X = 0
BASE_Y = 0

# Функции:

def drawPattern(width,height):
    turtle.speed(SPEED)
    turtle.hideturtle()
    turtle.fillcolor('black')
    turtle.pendown()
    # Внешний прямоугольник
    turtle.goto(BASE_X,height)
    turtle.goto(width,height)
    turtle.goto(width,BASE_Y)
    turtle.goto(BASE_X,BASE_Y)
    # Диагональные линии
    turtle.goto(width,height)
    turtle.goto(BASE_X,height)
    turtle.goto(width,BASE_Y)
    turtle.goto(width/2,BASE_Y)
    turtle.goto(width/2,height)
    turtle.penup()
    turtle.goto(BASE_X,height/2)
    turtle.pendown()
    turtle.goto(width,height/2)
    turtle.penup()
    # Средний прямоугольник
    turtle.goto(width/8,height-height/8)
    turtle.pendown()
    turtle.goto(width-width/8,height-height/8)
    turtle.goto(width-width/8,height/8)
    turtle.goto(width/8,height/8)
    turtle.goto(width/8,height-height/8)
    turtle.penup()
    # Внутренний прямоугольник
    turtle.goto(width/4,height-height/4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(width-width/4,height-height/4)
    turtle.goto(width-width/4,height/4)
    turtle.goto(width/4,height/4)
    turtle.goto(width/4,height-height/4)
    turtle.end_fill()
    turtle.penup()

def main():
    width = float(input('Введите ширину фигуры: '))
    height = float(input('Введите высоту фигуры: '))
    drawPattern(width,height)
    turtle.done()
    
main()