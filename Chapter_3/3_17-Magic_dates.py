day = int(input('Введите число месяца: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год в двухзначном формате, последние две цифры: '))

if day < 1 or day > 31 or month < 1 or month >12 or year < 0 or year > 99:
    print('Вы ввели некорректные данные')
else:
    ismagic_check = day * month
    if ismagic_check == year:
        print(f'Дата {day}.{month}.{year} является магической. Произведение дня на месяц получилось {ismagic_check}, что равно {year}.')
    else:
        print(f'Дата {day}.{month}.{year} не является магической. Произведение дня на месяц получилось {ismagic_check}, что не равно {year}.')
