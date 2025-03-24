# Сидячие места на стадионе. На стадионе имеется три категории сидячих мест. Места
# класса А стоят 20 долларов, места класса В - 15 долларов, места класса С - 1 О долларов.
# Напишите программу, которая запрашивает, сколько билетов каждого класса было
# продано, и затем выводит сумму дохода, полученного от продажи билетов.

# Константы:
A_CL_PR = 20
B_CL_PR = 15
C_CL_PR = 10

def main():
    # Локальные переменные:
    a_tickets_sold = 0
    b_tickets_sold = 0
    c_tickets_sold = 0
    a_total_income = 0
    b_total_income = 0
    c_total_income = 0
    # Пользовательский ввод:
    a_tickets_sold = int(input('Введите количество проданных билетов категории A: '))
    b_tickets_sold = int(input('Введите количество проданных билетов категории B: '))
    c_tickets_sold = int(input('Введите количество проданных билетов категории C: '))
    a_total_income = a_tickets_sold * A_CL_PR
    b_total_income = b_tickets_sold * B_CL_PR
    c_total_income = c_tickets_sold * C_CL_PR
    total_tickets_income = a_total_income + b_total_income + c_total_income
    tickets_income_print(a_total_income,b_total_income,c_total_income, total_tickets_income)
    
def tickets_income_print(a_sold, b_sold, c_sold, total_sold):
    print(f"""Билетов категории A продано на {a_sold:,.2f} $.
Билетов категории B продано на {b_sold:,.2f} $.
Билетов категории C продано на {c_sold:,.2f} $.
Суммарный доход составил {total_sold:,.2f} $.
""")

main()