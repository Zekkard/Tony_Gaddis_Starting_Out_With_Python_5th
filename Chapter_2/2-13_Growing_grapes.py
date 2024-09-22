ridge_len = float(input('Укажите длину гряды: '))
end_support_space = float(input('Укажите размер пространства концевых опор: '))
distance_between_vines = float(input('Укажите расстояние между лозами в метрах: '))
vines_num = (ridge_len - 2 * end_support_space) / distance_between_vines
print(f'В гряде поместится {vines_num:.2f} виноградных лоз.')