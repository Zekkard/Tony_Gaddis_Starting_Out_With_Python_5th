bun_amount = float(input('Сколько булочек Вы хотите приготовить? = '))
sugar = float(1.5) / 48
bread = float(1.0) / 48
flour = float(2.75) / 48
sugar_consumption = bun_amount * sugar
bread_consumption = bun_amount * bread
flour_consumption = bun_amount * flour
print(f'Вам понадобится  {sugar_consumption:.2f} стаканов сахара, {bread_consumption:.2f} стаканов масла и {flour_consumption:.2f} стаканов муки.')