speed = int(input('Введите скорость в км/ч: '))
time = int(input('Введите количество часов в пути: '))
print('\nЧас\tПройденное расстояние в км')
print('-'*40)
for hour in range (1, time+1):
    distance = speed * hour
    print(f'{hour}\t\t{distance}')