# Счетчик четных/нечетных чисел. В этой главе вы увидели пример написания алгоритма,
# который определяет четность или нечетность числа. Напишите программу, которая
# генерирует 100 случайных чисел и подсчитывает количество четных и нечетных
# случайных чисел.

# Импорт библиотек
import random

def main():
    # Локальные переменные
    gen_limit = 100
    odd_cnt = num_generator(gen_limit)
    even_cnt = gen_limit - odd_cnt
    print_result(gen_limit,odd_cnt,even_cnt)
    
def num_generator(limit):
    # Локальные переменные
    odd = 0
    for i in range(limit):
        num = random.randint(1,999)
        odd += odd_check(num)
    return odd

def odd_check(num):
    return num % 2

def print_result(limit,even_cnt,odd_cnt):
    print(f'\nБыло сгенерировано {limit} чисел.\nИз них чётных: {even_cnt}.\nИз них нечётных: {odd_cnt}.\n')

main()