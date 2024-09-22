distance = float(input('Введите количество пройденного пути в километрах: '))
fuel_cons = float(input('Введите количество затраченного топлива в литрах: '))
cons_per_km = distance / fuel_cons
print(f'Расход топлива составил {cons_per_km:.2f} литров.')