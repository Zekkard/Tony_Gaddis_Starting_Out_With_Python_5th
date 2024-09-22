amount_1 = int(input('Введите первое число: '))
amount_2 = int(input('Введите второе число: '))
if amount_1 > 10 and amount_2 < 100:
    if amount_1 > amount_2:
        print(amount_1)
    if amount_1 < amount_2:
        print(amount_2)
    else: print(f'Числа {amount_1} равны между собой.')