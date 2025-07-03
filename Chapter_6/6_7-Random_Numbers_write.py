# Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел. Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.

# Импорт библиотек
import os
import random as r

def main():
    os.makedirs('data',exist_ok=True)
    outfile = open('data/random_numbers.txt','w')
    numbers_cnt = int(input('Введите итоговое число случайных чисел: '))
    cnt = 0
    for i in range(numbers_cnt):
        outfile.write(f'{r.randint(1,500)}\n')
    outfile.close()
    print('Файл сгенерирован.')
main()