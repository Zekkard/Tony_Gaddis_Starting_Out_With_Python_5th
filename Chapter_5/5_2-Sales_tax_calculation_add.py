def get_price():
    return float(input('Введите стоимость товара: '))

def get_fed_tax_rate():
    return float(input('Введите ставку федерального налога: '))

def get_reg_tax_rate():
    return float(input('Введите стоимость регионального налога: '))

def calc_fed_tax(price, fed_tax):
    return price * fed_tax

def calc_reg_tax(price, reg_tax):
    return price * reg_tax

def calc_total_tax(final_fed_tax, final_reg_tax):
    return final_fed_tax + final_reg_tax

def calc_total_cost(price, total_tax):
    price += total_tax
    return price

def print_result(price,fed_tax,reg_tax,total_tax,total_cost):
    print(f'Стоимость составляет {price:,.2f} Р.')
    print(f'Федеральный налог составляет {fed_tax:,.2f} Р.')
    print(f'Региональный налог составляет {reg_tax:,.2f} Р.')
    print(f'Суммарный налог составляет {total_tax:,.2f} Р.')
    print(f'Итоговая стоимость составляет {total_cost:,.2f} Р.')

def main():
    price = get_price()
    fed_tax = get_fed_tax_rate()
    reg_tax = get_reg_tax_rate()
    final_fed_tax = calc_fed_tax(price,fed_tax)
    final_reg_tax = calc_reg_tax(price,reg_tax)
    total_tax = calc_total_tax(final_fed_tax, final_reg_tax)
    total_cost = calc_total_cost(price,total_tax)
    print_result(price,fed_tax,reg_tax,total_tax,total_cost)

main()
# fed_tax =  0.05
# reg_tax = 0.025
# final_fed_tax = price * fed_tax
# final_reg_tax = price * reg_tax
# total_tax = final_fed_tax + final_reg_tax
# total_cost = price + total_tax
# print(f'Стоимость товара составляет {price:.2f} рублей.')
# print(f'Федеральный налог составляет {final_fed_tax:.2f} рублей.')
# print(f'Региональный налог составляет {final_reg_tax:.2f} рублей.')
# print(f'Общая стоимость составляет {total_cost:.2f} рублей.')