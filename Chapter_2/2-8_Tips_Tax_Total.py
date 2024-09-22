price = float(input('Введите суммарную стоимость блюд: '))
tips = price * 0.18
tax = price * 0.07
total = price + tips + tax
print(f'Сумма после налогов с чаевыми составит {total} рублей.')