pocket_chosen = int(input('Введите номер выбранного кармана (допустимые номера от 0 до 36 включительно): '))
if pocket_chosen < 0 or pocket_chosen > 36: #Вне диапазона номеров карманов
    print('ОШИБКА! Ввод некорректен, пожалуйста, выберите число от 0 до 36.')
elif pocket_chosen == 0: # 0
    pocket_color = 'Зелёный'
elif pocket_chosen % 2 == 0: # Чётные
    if pocket_chosen >= 1 and pocket_chosen < 11:
        pocket_color = 'Чёрный'
    elif pocket_chosen >= 11 and pocket_chosen < 19:
        pocket_color = 'Красный'
    elif pocket_chosen >= 19 and pocket_chosen < 29:
        pocket_color = 'Чёрный'
    elif pocket_chosen >= 29 and pocket_chosen < 37:
        pocket_color = 'Красный'
elif pocket_chosen % 2 == 1: # Нечётные
    if pocket_chosen >= 1 and pocket_chosen < 11:
        pocket_color = 'Красный'
    elif pocket_chosen >= 11 and pocket_chosen < 19:
        pocket_color = 'Чёрный'
    elif pocket_chosen >= 19 and pocket_chosen < 29:
        pocket_color = 'Красный'
    elif pocket_chosen >= 29 and pocket_chosen < 37:
        pocket_color = 'Чёрный'
print(f'Цвет выбранного кармана - {pocket_color}. ')

