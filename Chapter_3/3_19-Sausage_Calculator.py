#Объявление переменных
participants_num = int(input('Введите количество участников пикника: '))
hotdogs_num = int(input('Введите количество хотдогов на участника: '))
hotdogs_total_cnt = participants_num * hotdogs_num
sausage_per_pack = 10
bun_per_pack = 8

# Проверка ввода.
if participants_num <= 0 and hotdogs_num <= 0:
    print('Ввод некорректен. Введите числа больше нуля.')

# Предрасчётные формулы
total_sausage_pack_needs = hotdogs_total_cnt // sausage_per_pack
sausages_left = hotdogs_total_cnt % sausage_per_pack
total_buns_pack_needs = hotdogs_total_cnt  // bun_per_pack
buns_left = hotdogs_total_cnt % bun_per_pack

# Расчёт итогового количества
if sausages_left != 0: # Когда результат положительный - результат усекается, когда отрицательный - округляется вверх по модулю числа.
    total_sausage_pack_needs = total_sausage_pack_needs + 1
    sausages_left = sausage_per_pack - (hotdogs_total_cnt % sausage_per_pack)
if buns_left != 0:
    total_buns_pack_needs = total_buns_pack_needs + 1
    buns_left = bun_per_pack - (hotdogs_total_cnt % bun_per_pack)

# Вывод
print(f"""Чтобы организовать {hotdogs_total_cnt} хотдогов для {participants_num} участника пикника (по {hotdogs_num} хотдогов на участника), Вам потребуется:
    * Упаковок сосисок: {total_sausage_pack_needs} шт.
    * Упаковок булок: {total_buns_pack_needs} шт.
    * У вас останется сосисок: {sausages_left} шт.
    * У вас останется булок: {buns_left} шт.""")