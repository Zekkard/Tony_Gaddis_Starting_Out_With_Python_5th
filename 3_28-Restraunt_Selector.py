err_msg = 'Ввод некорректен, допускаются только ответы да\нет'
vegetrian = str(input('Будет ли на ужине вегетрианец? да\нет: ')).lower()
if vegetrian == 'да' or vegetrian == 'нет':    
    vegan = str(input('Будет ли на ужине веганец? да\нет: ')).lower()
    if vegan == 'да' or vegan == 'нет':
        gluten = str(input('Будет ли на ужине приверженец безглютеновой диеты? да\нет: ')).lower()
        if gluten == 'да' or gluten == 'нет':
            print('Вот ваши варианты ресторанов:')
            if vegetrian == 'нет' and vegan == 'нет' and gluten == 'нет':
                print('Изысканные гамбургеры от Джо.')
            if vegan == 'нет':
              print('Центральная пиццерия')
            if vegan == 'нет' and gluten == 'нет':
                print('Кухня итальянской мамы.')
            print('Кафе за углом.')
            print('Кухня шеф-повара.')
        else:
            print(err_msg)
    else:
        print(err_msg)
else:
    print(err_msg)
    print(err_msg)