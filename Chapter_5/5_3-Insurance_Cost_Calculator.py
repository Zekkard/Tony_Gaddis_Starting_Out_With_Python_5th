# Глобальные константы
REPLACEMENT_RATE = 0.8
# Получение стоимости жилья 
def get_apartment_cost():
    return float(input('Введите стоимость замещения: '))
def calc_min_inc_rate(apartment_cost, ins_rate):
    print(f'Стоимость замещения составляет: {apartment_cost} рублей.')
    print(f'Минимальная сумма, подлежащая страхованию, составляет: {apartment_cost * ins_rate:,.2f} рублей.')
    print(f'Страхуемый процент: {int(ins_rate * 100)}%')
def main():
     apartment_cost = 0.0
     apartment_cost = get_apartment_cost()
     calc_min_inc_rate(apartment_cost,REPLACEMENT_RATE)
main()   
    