total_days = int(input('Введите количество дней: '))
salary = 0.01
salary_rate = 2
print('Таблица заработной платы за день\nдень\tзарплата')
for day in range(1,total_days+1):
    print(f'{day}\t{salary:.2f}')
    salary*=salary_rate
print(f'Всего за период в {total_days} заработано {salary / 100} рублей.')