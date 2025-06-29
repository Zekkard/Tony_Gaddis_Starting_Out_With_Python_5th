# Черепашья графика: модульный снеговик. Напишите программу, которая использует
# черепашью графику для изображения снеговика (рис. 5.30). 
# Помимо главной функции программа также должна иметь перечисленные ниже функции:
# • drawвase - ком внизу - функция должна нарисовать основу снеговика, т. е. большой снежный
# • drawMidSection - функция должна нарисовать средний снежный ком;
# • drawArms - функция должна нарисовать руки снеговика;
# • drawнead - функция должна нарисовать голову снеговика, глаза, рот и другие черты лица по вашему усмотрению;
# • drawHat - эта функция должна нарисовать шляпу снеговика.
import turtle
import random

# Константы
SCREEN_H = 400
SCREEN_W = 300

BASE_XCOR = 0
BASE_YCOR = -250
BASE_RADIUS = 100

MIDSEC_XCOR = 0
MIDSEC_YCOR = -50
MIDSEC_RADIUS = 70

RARM_XCOR = 60.62
RARM_YCOR = 55.00
LARM_XCOR = -60.62
LARM_YCOR = 55.00

HEAD_XCOR = 0
HEAD_YCOR = 90
HEAD_RADIUS = 40

def main():
    turtle.screensize(SCREEN_H,SCREEN_W)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    drawbase()
    drawMidSection()
    drawArms()
    drawhead()
    drawHat()
    turtle.done()

def drawbase():
    turtle.goto(BASE_XCOR,BASE_YCOR)
    turtle.pendown()
    turtle.circle(BASE_RADIUS)
    turtle.penup()
       

def drawMidSection():
    turtle.goto(MIDSEC_XCOR, MIDSEC_YCOR)
    turtle.pendown()
    turtle.circle(MIDSEC_RADIUS)
    turtle.penup()

def drawArms():
    #Левая рука
    turtle.goto(LARM_XCOR,LARM_YCOR)
    turtle.setheading(random.randint(120,220)) #lelbow_angle
    turtle.pendown()
    turtle.forward(50) #elbow_length
    turtle.setheading(random.randint(90,240)) #forearm_angle
    turtle.forward(40) #forearm_length
    turtle.left(30) #hand_angle_1
    turtle.forward(10) #hand_length
    turtle.backward(10)
    turtle.right(70) #hand_angle_2
    turtle.forward(10)
    turtle.backward(10)
    turtle.setheading(0)
    turtle.penup()
    #Правая рука
    turtle.goto(RARM_XCOR,RARM_YCOR)
    turtle.setheading(random.randint(-40,60))
    turtle.pendown()
    turtle.forward(50)
    turtle.setheading(random.randint(-60,90))
    turtle.forward(40)
    turtle.left(30)
    turtle.forward(10)
    turtle.backward(10)
    turtle.right(70)
    turtle.forward(10)
    turtle.backward(10)
    turtle.setheading(0)
    turtle.penup()
    

def drawhead():
    turtle.goto(HEAD_XCOR,HEAD_YCOR)
    turtle.pendown()
    turtle.circle(HEAD_RADIUS)
    turtle.penup()
    turtle.goto(-10,140) #eye_line
    turtle.pendown()
    turtle.circle(3)
    turtle.penup()
    turtle.goto(10,140) #eye_line
    turtle.pendown()
    turtle.circle(3)
    turtle.penup()
    turtle.goto(-20,120) #month_line
    turtle.pendown()
    turtle.goto(20,120) #month_line
    turtle.penup()
    
def drawHat():
    # нижний полог шляпы по координатам Х: -60 до 60, У: 150
    # итого ширина полога составляет 120
    # верхний полог по У: 170, т.е. высота полога составляет 20.
    # основание цилиндра x= -30 до 30, y = 170
    # верх цилиндра х = тот же, у = 210
    turtle.goto(-60,150) # стартовая координата нижнег левого края основания шляпы
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(-60,170) # координата верхнего левого края основания шляпы
    turtle.goto(-30,170) # координата левого угла основания цилиндра
    turtle.goto(-30,210) # координата верхнего левого края цилиндра
    turtle.goto(30,210) # координата верхнего правого края цилиндра
    turtle.goto(30,170) # координата правого угла основания цилиндра
    turtle.goto(60,170) # координата верхнего правого края основания шляпы
    turtle.goto(60,150) # координата нижнего правого края основания шляпы
    turtle.goto(-60,150) # возврат в начало для окончания заполнения.
    turtle.end_fill()
    turtle.penup

main()