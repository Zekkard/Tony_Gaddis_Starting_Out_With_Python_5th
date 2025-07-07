# Среднее количество шагов. Браслет для занятий спортом - это носимое устройство,
# которое отслеживает вашу физическую активность, количество сожженных калорий,
# сердечный ритм, модели сна и т. д. Одним из самых распространенных видов физический
# активности, который отслеживает большинство таких устройств, является количество
# шагов, которые вы делаете каждый день.
# Среди исходного кода главы 6 вы найдете файл steps.txt. Этот файл содержит количество
# шагов, которые человек делал каждый день в течение года. В файле 365 строк, и каждая
# строка содержит количество шагов, сделанных в течение дня. (Первая строка - это число
# шагов, сделанных 1 января, вторая строка- число шагов, сделанных 2 января, и т. д.)
# Напишите программу, которая читает файл и затем выводит среднее количество шагов,
# сделанных в течение каждого месяца. (Данные были записаны в год, который не был
# високосным, и поэтому февраль имеет 28 дней.)

# Импорт библиотек
import os

# Константы
JANUARY = 31
FEBRARY = 28
MARCH = 31
APRIL = 30
MAY = 31
JUNE = 30
JULY = 31
AUGUST = 31
SEPTEMBER = 30
OCTOBER = 31
NOVEMBER = 30
DECEMBER = 31

def steps_avg_calc(infile,days,month):
    sum_cnt = 0
    for day in range(days):
        sum_cnt += int(infile.readline())
    avg_steps = sum_cnt / days
    print(f'Среднее количество шагов за {month}: {avg_steps:,.2f} .')

def main():
    try:
        infile = open('data/steps.txt','r')
        steps_avg_calc(infile, JANUARY, 'январь')
        steps_avg_calc(infile, FEBRARY, 'февраль')
        steps_avg_calc(infile, MARCH, 'март')
        steps_avg_calc(infile, APRIL, 'апрель')
        steps_avg_calc(infile, MAY, 'май')
        steps_avg_calc(infile, JUNE, 'июнь')
        steps_avg_calc(infile, JULY, 'июль')
        steps_avg_calc(infile, AUGUST, 'август')
        steps_avg_calc(infile, SEPTEMBER, 'сентябрь')
        steps_avg_calc(infile, OCTOBER, 'октябрь')
        steps_avg_calc(infile, NOVEMBER, 'ноябрь')
        steps_avg_calc(infile, DECEMBER, 'декабрь')
        infile.close()
    except IOError:
        print('Ошибка чтения файлаю')
main()