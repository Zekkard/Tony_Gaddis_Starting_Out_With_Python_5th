factorial_i = int(input('Введите положительное число: '))
factorial = 1
for i in range(2,factorial_i+1):
    factorial *= i
print(f'Факториал числа {factorial_i} = {factorial}')