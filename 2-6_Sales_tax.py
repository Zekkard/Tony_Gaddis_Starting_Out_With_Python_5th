price=float(input('Введите стоимость покупки: '))
fed_tax =  0.05
reg_tax = 0.025
final_fed_tax = price * fed_tax
final_reg_tax = price * reg_tax
total_tax = final_fed_tax + final_reg_tax
total_cost = price + total_tax
print(f'Стоимость товара составляет {price:.2f} рублей.')
print(f'Федеральный налог составляет {final_fed_tax:.2f} рублей.')
print(f'Региональный налог составляет {final_reg_tax:.2f} рублей.')
print(f'Общая стоимость составляет {total_cost:.2f} рублей.')