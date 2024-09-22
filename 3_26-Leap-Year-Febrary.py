year = int(input('Введите год: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    febrary = 29
else:
    febrary = 28
print(f'В {year} году в феврале {febrary} дней.')