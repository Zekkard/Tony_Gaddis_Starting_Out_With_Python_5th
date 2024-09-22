# После превращения в недели и месяцы начинаются проблемы, поэтому калькулятор пишется менее серьёзный и строго по задаче.
# Калькулятор секунд в дни и минуты.
input_seconds = int(input('Введите количество секунд: '))
if input_seconds <=0:
    print('Ввод некорректен. Количество секунд в калькуляторе не может быть меньше, либо равно нулю')
else:
    if_days = input_seconds // 86400
    if_hours = input_seconds // 3600
    if_minutes = input_seconds // 60
    days = if_days % 86400
    hours = if_hours % 86400 % 24
    minutes = if_minutes % 3600 % 60
    seconds = input_seconds % 60
    if if_days > 0:
        print(f'Количество дней: {days}, количество часов: {hours}, количество минут: {minutes}, количество секунд: {seconds}.')
    elif if_hours > 0:
        print(f'Количество часов: {hours}, количество минут: {minutes}, количество секунд: {seconds}.')
    elif if_minutes > 0:
        print(f'Количество минут: {minutes}, количество секунд: {seconds}.')
    else:
        print(f'Количество секунд: {seconds}.')