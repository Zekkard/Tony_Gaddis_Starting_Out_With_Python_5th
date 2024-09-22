points = int(input('Введите точку: '))
if points < 8 or points > 52:
    print(f'Недопустимые точки для {points}')
else:
    print(f'Точка {points} допустимая')