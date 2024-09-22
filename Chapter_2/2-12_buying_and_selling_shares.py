in_shares_amt = int(input('Введите количество приобретённых акций: '))
in_share_price = float(input('Введите стоимость одной акции: '))
in_final_cost = in_shares_amt * in_share_price
in_brokers_fee = in_final_cost * 0.03
in_total_cost = in_final_cost + in_brokers_fee
out_shares_amt = int(input('Введите количество проданных акций: '))
out_share_price = float(input('Введите продажную цену одной акции: '))
out_final_cost = out_shares_amt * out_share_price
out_brokers_fee = out_final_cost * 0.03
out_total_cost = out_final_cost + out_brokers_fee
print(f'Стоимость приобретения акций составила {in_final_cost:.2f} рублей.')
print(f'Комиссия при приобретении у брокера составила {in_brokers_fee:.2f} рублей.')
print(f'Стоимость продажи акций составила {out_final_cost:.2f} рублей.')
print(f'Комиссия при продаже у брокера составила {out_brokers_fee:.2f} рублей.')
print(f'Выгода составила {out_total_cost - in_total_cost:.2f} рублей.')
