# Черепашья графика: шахматная доска. Напишите программу с использованием черепашьей
# графики, в которой применяется представленная в этой главе функция square
# вместе с циклом (или циклами) для создания показанного на рис . 5.32 шахматного узора.

# Библиотеки
import turtle

# Константы:
## Экран
S_HEIGHT = 500
S_WIDTH = 500
S_LEFT_EDGE = int(-(S_WIDTH / 2)) # экран шириной в 500 имеет сетку от -250 до +250.
S_TOP_EDGE = int(S_HEIGHT / 2) # тоже самое, но верх будет положительный
## Таблица
COLS_CNT = 5
ROWS_CNT = 5
## Константы для координат в функции square
SQ_WIDTH = int(S_WIDTH / COLS_CNT)
SQ_FIRST_Y = int(S_TOP_EDGE - SQ_WIDTH) # Нужен для итерации по столбцу. Оригинальная функция будет рисовать квадрат вверх.
SQ_LAST_Y = int(SQ_FIRST_Y - (ROWS_CNT * SQ_WIDTH)) # получение последней координаты по вертикали для функции square.
SQ_LAST_X = int(S_LEFT_EDGE + (COLS_CNT * SQ_WIDTH)) # получение последней координаты по горизонтали для функции square.
## Черепаха
T_SPEED = 0



def square(x, у, width, color) :
    turtle.penup()          # Поднять перо.
    turtle.goto(x, у)       # Переместить в указанное место.
    turtle.fillcolor(color) # Задать цвет заливки.
    turtle.pendown()        # Опустить перо.
    turtle.begin_fill()     # Начать заливку.
    for count in range(4):  # Нарисовать квадрат.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
# Завершить заливку.

def main():
    turtle.setup(S_WIDTH, S_HEIGHT)
    turtle.speed(T_SPEED)
    turtle.hideturtle()
    color = 'black'
    for y in range(SQ_FIRST_Y,SQ_LAST_Y,-SQ_WIDTH):
        for x in range(S_LEFT_EDGE,SQ_LAST_X,SQ_WIDTH):
            square(x,y,SQ_WIDTH,color)
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
    turtle.done()

main()



# Именованные константы
ANIMATION_SPEED = 0
SCREEN_WIDTH = 500                                          # сначала задаём ширину
SCREEN_HEIGHT = 500                                         # и высоту холста
NUM_SQUARES_IN_A_ROW = 5                                    # затем перечисляем число квадратов в строке
NUM_SQUARES_IN_A_COL = 5                                    # и в колонке.
SQUARE_WIDTH = int(SCREEN_WIDTH / NUM_SQUARES_IN_A_ROW)     # После вычисляем ширину такого квадрата путём деления ширины холста на количество квадратов
SCREEN_LEFT_EDGE_X = int(-(SCREEN_WIDTH / 2))               # вычисляем левую границу холста
SCREEN_TOP_EDGE_Y = int(SCREEN_HEIGHT / 2)                  # а так же верхнюю границу холста
FIRST_X = SCREEN_LEFT_EDGE_X                                # вычисляем первую, левую точку отсчёта для квадратов, крайняя левая координата нужна была для этого
LAST_X = FIRST_X + (NUM_SQUARES_IN_A_ROW * SQUARE_WIDTH)    # затем - последнюю справа, путём сложения крайней левой на ширину квадратов умноженную на число.
FIRST_Y = SCREEN_TOP_EDGE_Y - SQUARE_WIDTH                  # затем ищем первую строку по высоте, вычитая ширину (она же высота) квадрата от левой верхней границы
LAST_Y = FIRST_Y - (NUM_SQUARES_IN_A_COL * SQUARE_WIDTH)    # аналогично строке - вычисляем (опускаем) нижнюю Y координату путём вычитания результатов перемножения 
                                                            # количества квадратов в столбце на ширину