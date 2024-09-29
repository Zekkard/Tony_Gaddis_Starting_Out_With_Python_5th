years = int(input('Введите количество лет: '))
months = 0
total_rainfall = 0
for year in range(years):
    for month in range(12):
        months += 1
        rainfall = int(input(f'Введите количество мм осадков за месяц {month +1}, года {year + 1}: '))
        total_rainfall += rainfall
print(f'Всего осадков за {months} месяцев: {total_rainfall} мм. Средняя толщина осадков в месяц: {total_rainfall/months} мм.')