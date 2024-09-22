mass = float(input('Введите массу в килограммах: '))
weight = mass * 9.8
if weight < 100:
    print('Тело слишком лёгкое.')
elif weight > 500: print('Тело слишком тяжёлое.')
else: 
    print(f'Вес тела в ньютонах составляет {weight:.2f}.')