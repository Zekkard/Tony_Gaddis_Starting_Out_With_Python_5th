price_1 = float(input('Введите стоимость Первого товара: '))
price_2 = float(input('Введите стоимость Второго товара: '))
price_3 = float(input('Введите стоимость Третьего товара: '))
price_4 = float(input('Введите стоимость Четвертого товара: '))
price_5 = float(input('Введите стоимость Пятого товара: '))
total_price = price_1+price_2+price_3+price_4+price_5
tax_rate = 0.07
final_tax = total_price * tax_rate
total_cost = total_price + final_tax
print(f'Стоимость товаров: {total_price:.2f} рублей.')
print(f'Налог составляет: {final_tax:.2f} рублей.')
print(f'Общая стоимость составляет {total_cost:.2f} рублей.')