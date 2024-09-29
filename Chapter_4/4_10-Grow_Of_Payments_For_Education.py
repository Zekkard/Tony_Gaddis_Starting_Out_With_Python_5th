edu_cost = 145000
total_cost = 0
print('Год\tСтоимость курса')
print('-'*20)
for i in range (1,6):
    print(f'{i}\t{edu_cost:.2f}')
    total_cost += edu_cost
    edu_cost += edu_cost * 0.03
print(f'Всего за 5 лет стоимость обучения составит: {total_cost:.2f} рублей.')