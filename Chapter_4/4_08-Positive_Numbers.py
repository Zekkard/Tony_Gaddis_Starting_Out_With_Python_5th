num = 0
accumulator = 0
while num >= 0:
    accumulator += num
    num=int(input('Введите положительное число, либо отрицательное число для вывода результатов: '))
print(f'Сумма введённых чисел составляет: {accumulator}')