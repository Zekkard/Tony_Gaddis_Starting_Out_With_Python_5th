print('Программа берёт от вас два цвети и выводит на экран результат их смешивания. Смешать можно - красный, синий, желтый.')
color_1 = str(input('Введите первый цвет, допускаются только буквы без знаков препинания: '))
color_2 = str(input('Введите второй цвет, допускаются только буквы без знаков препинания: '))
print(color_1.lower(), color_2.lower())
if (color_1.lower() == 'жёлтый' or color_1.lower() == 'желтый' or color_1.lower() == 'красный' or color_1.lower() == 'синий') \
and \
(color_2.lower() == 'жёлтый' or color_2.lower() == 'желтый' or color_2.lower() == 'красный' or color_2.lower() == 'синий'):
    if (color_1.lower() == 'красный' and color_2.lower() == 'синий') \
    or (color_1.lower() == 'синий' and color_2.lower() == 'красный'):
        print(f'При смешении цветов {color_1} и {color_2} получится фиолетовый.')
    elif (color_1.lower() == 'красный' and (color_2.lower() == 'желтый' or color_2.lower() == 'жёлтый')) \
    or ((color_1.lower() == 'желтый' or color_1.lower() == 'жёлтый') and color_2.lower() == 'красный'):
        print(f'При смешении цветов {color_1} и {color_2} получится оранжевый.')
    elif (color_1.lower() == 'синий' and (color_2.lower() == 'желтый' or color_2.lower() == 'жёлтый')) \
    or ((color_1.lower() == 'желтый' or color_1.lower() == 'жёлтый') and color_2.lower() == 'синий'):
        print(f'При смешении цветов {color_1} и {color_2} получится зелёный.')
else:
    print('Ввод некорректен, допускаются только цвета желтый, красный или синий.')