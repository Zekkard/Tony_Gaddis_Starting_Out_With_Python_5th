# Черепашья графика: городской силуэт. Напишите программу с черепашьей графикой,
# которая рисует городской силуэт (рис. 5.33). Конечная задача программы состоит в том,
# чтобы нарисовать контуры нескольких городских зданий на фоне ночного неба. Подразделите
# программу на модули, написав функции, которые выполняют приведенные ниже
# задачи:
# • рисование контуров зданий;
# • рисование нескольких окон в зданиях;
# • использование случайно разбросанных звезд в виде точек (убедитесь, что звезды
# появляются на небе, а не на зданиях) .

# Импорт библиотек
import turtle as t # алиасы для сокращения кода. Мы их ещё не проходили, но эту главу я закрываю особенно долго. Решил облегчить себе задачу психологически.
import random as r

# Константы
S_HEIGHT = 600
S_WIDTH = 600
S_L_EDGE = int(-(S_WIDTH / 2))
S_R_EDGE = int(S_WIDTH / 2)
S_T_EDGE = int(S_HEIGHT / 2)
S_B_EDGE = int(-(S_HEIGHT / 2))
S_COLOR = 'black'
T_SPEED = 0
STARS_CNT = 200

def t_config(width,height,speed,bg_color):
    t.setup(width,height)
    t.Screen().bgcolor(bg_color)
    t.hideturtle()
    t.penup()
    t.speed(speed)
    
def draw_stars():
    for s in range(STARS_CNT):
        size = r.randint(1,2)
        x = r.randint(-300,300)
        y = r.randint(-100,300)
        t.goto(x,y)
        t.dot(size,'white')

def draw_buildings():
    t.goto(-300,-100)
    t.pendown()
    t.fillcolor('grey')
    t.begin_fill()
    
    # Первое здание
    t.goto(-225,-100)
    t.goto(-225,0)
    t.goto(-150,0)
    
    # Второе здание
    t.goto(-150, 200)
    t.goto(0,200)
    t.goto(0,-50)
    
    # Третье здание
    t.goto(75,-50)
    t.goto(75,100)
    t.goto(185,100)
    
    # Четвертое здание
    t.goto(185,-30)
    t.goto(225,-30)
    t.goto(225,-100)
    
    # Конец заливки
    t.goto(300,-100)
    t.goto(300,-300)
    t.goto(300,-300)
    t.goto(-300,-300)
    t.goto(-300,-100)
    t.end_fill()
    t.penup()
    
def square(x, у, width, color) :
    t.penup()          # Поднять перо.
    t.goto(x, у)       # Переместить в указанное место.
    t.fillcolor(color) # Задать цвет заливки.
    t.begin_fill()     # Начать заливку.
    for count in range(4):  # Нарисовать квадрат.
        t.forward(width)
        t.left(90)
    t.end_fill()
# Завершить заливку.

def draw_windows():
    square(-210, -40, 20, 'white')
    square(-135, 160, 20, 'white')
    square(-135, 130, 20, 'white')
    square(-35, 70, 20, 'white')
    square(-60, -130, 20, 'white')
    square(90, 60, 20, 'white')

def main():
    t_config(S_WIDTH,S_HEIGHT,T_SPEED,S_COLOR)
    draw_stars()
    draw_buildings()
    draw_windows()
    t.done()
    
main()



