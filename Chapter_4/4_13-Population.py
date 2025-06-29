population = int(input('Введите численность особей: '))
while population <= 0:
    population = int(input('Ввод некорректен. Введите число больше нуля.\nВведите численность особей: '))
inc_factor = int(input('Введите прирост популяции в день в процентах, целым числом: ')) / 100
while inc_factor <= 0:
    inc_factor = int(input('Ввод некорректен. Введите число больше нуля.\nВведите прирост популяции в день в процентах, целым числом: ')) / 100
period = int(input('Введите количество дней '))
while period <= 0:
    period = int(input('Ввод некорректен. Введите число больше нуля.\nВведите количество дней: '))
print('День\tЧисленность популяции')
for day in range(1,period+1):
    print(f'{day}\t{population}')
    population += population * inc_factor