budget = float(input('Введите сумму бюджета на месяц: '))
expenses = 0
spent = 1
while spent > 0 or spent < 0:
    spent = float(input('Введите сумму трат по отдельной статье расходов, 0 для отображения результатов: '))
    expenses += spent
balance = budget - expenses
print(f'Бюджет на месяц составляет {budget:.2f} рублей.')
print(f'Траты за месяц составили {expenses:.2f} рублей.')
if balance < budget:
    print(f'Ваш баланс: Перерасход = {balance} рублей')
elif balance > budget:
    print(f'Ваш баланс: Сэкономлено = {balance} рублей')
else:
    print(f'Ваш баланс: {balance} рублей. Вы уместились ровно в бюджет.')