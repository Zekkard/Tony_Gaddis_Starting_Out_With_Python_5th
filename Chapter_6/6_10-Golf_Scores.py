# Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# • программу, которая читает записи из файла golf.txt и выводит их на экран.

import os

def golf_logger(player,score):
    os.makedirs('data',exist_ok=True)
    outfile = open('data/golf_log.txt','a')
    outfile.write(f'Игрок: {player}\nОчки: {score}\n\n')
    outfile.close()

def golf_get_log():
    inputfile = open('data/golf_log.txt','r')
    for line in inputfile:
        print(line.rstrip('\n'))
    inputfile.close()

def main():
    try:
        work_mode = int(input('Выберите режим работы:\n1 - Внести данные. \n2 - Прочитать данные.\n: '))
        if work_mode == 1:
            player = input('Введите имя игрока: ')
            score = int(input('Введите количество очков: '))
            golf_logger(player,score)
        elif work_mode == 2:
            golf_get_log()
        else:
            print('Введено некорректное значение.')
    except ValueError:
        print('Введено некорректное значение.')
    except IOError:
        print('Ошибка чтения файла.')

main()