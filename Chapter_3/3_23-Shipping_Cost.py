cargo_weight = int(input('Введите вес пакета в граммах: '))
if cargo_weight < 0:
    print('Введено неверное значение. Вес не может быть меньше нуля.')
elif cargo_weight == 0 :
    print('Вес не может быть равен нулю.')
else:
    if cargo_weight <= 200:
        cost_rate_100g = 150
    elif cargo_weight > 200 and cargo_weight <= 600:
        cost_rate_100g = 300
    elif cargo_weight > 600 and cargo_weight <= 1000:
        cost_rate_100g = 400
    elif cargo_weight > 1000:
        cost_rate_100g = 475
    cost_rate_1g = cost_rate_100g / 100
    total_price = cargo_weight * (cost_rate_1g)
    print(f"""
          Указанные вес посылки: {cargo_weight} грамм.
          Ценовая ставка: {cost_rate_100g} рублей за 100 грамм.
          Итоговая стоимость доставки: {total_price:.2f} рублей.""")