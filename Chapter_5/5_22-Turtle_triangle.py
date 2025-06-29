# Черепашья графика: функция рисования треугольника. Напишите функцию triangle,
# которая использует библиотеку черепашьей графики для рисования треугольника.
# Функция должна принимать в качестве аргументов координаты Х и У сторон треугольника
# и цвет, которым треугольник должен быть заполнен. Продемонстрируйте эту
# функцию в программе.

import turtle

def get_input():
    return int(input('Введите значение x1: ')),int(input('Введите значение y1: ')),int(input('Введите значение x2: ')),int(input('Введите значение y2: ')),int(input('Введите значение x3: ')),int(input('Введите значение y3: ')),str(input('Введите цвет заполнения треугольника: '))

def triangle(x1,y1,x2,y2,x3,y3,color):
    turtle.fillcolor(color)
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)
    turtle.end_fill()
    turtle.penup()
    turtle.done()

def main():
    turtle.hideturtle()
    turtle.speed(0)
    triangle(*get_input()) # Распаковка аргументов из возвращаемого кортежа значений. 
    turtle.done()

main()