software_bought_cnt = int(input('Введите количество купленных программ: '))
software_cost = 99.00
if software_bought_cnt < 0:
    print('Вы ввели неверное значение, количество купленных программ не может быть меньше 0.')
elif software_bought_cnt == 0:
    print('Вы не купили ни одной программы.')
else:
    discount = 0
    discount_message = '0%'
    if software_bought_cnt >= 10 and software_bought_cnt < 20:
        discount = 0.1
        discount_message = '10%'
    elif software_bought_cnt >= 20 and software_bought_cnt < 50:
        discount = 0.2
        discount_message = '20%'
    elif software_bought_cnt >= 50 and software_bought_cnt < 100:
        discount = 0.3
        discount_message = '30%'
    elif software_bought_cnt >= 100:
        discount = 0.4
        discount_message = '40%'
    purchase_price = software_bought_cnt * software_cost
    discount_sum = purchase_price * discount
    total_price_w_discount = purchase_price - discount_sum
    print(f"""Вы приобрели {software_bought_cnt} программ. 
          Стоимость товаров в корзине: {purchase_price:.2f} долларов.
          Скидочный коэффициент: {discount_message} . 
          Сумма скидки: {discount_sum:.2f} долларов.
          Итого с вас: {total_price_w_discount:.2f} долларов.""")