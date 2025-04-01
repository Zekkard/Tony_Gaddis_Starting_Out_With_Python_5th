# Средний балл и его уровень. Напишите программу, которая просит пользователя ввести
# пять экзаменационных оценок (баллов). Программа должна показать буквенный
# уровень для каждой оценки и средний балл. Предусмотрите в программе функции:
# • calc average - функция должна принимать в качестве аргументов пять балльных
# оценок и возвращать средний балл;
# • determine_grade - функция должна принимать в качестве аргумента балльную
# оценку и возвращать буквенный уровень оценки, опираясь на приведенную ниже классификацию:
# Баллы Уровень
# 90 и выше А
# 80-89 в
# 70-79 с
# 60-69 D
# Ниже 60 F

# Как же жалко, что списки и .append встречаются только в главе 7. Придётся люто графоманить.
# Просто напомню, что я пользуюсь строго тем инструментарием, который "должен знать" к моменту решения задачи по учебнику.
# В противном случае писал бы функции через циклы.

def main():
    val1,val2,val3,val4,val5 = get_input()
    avg = calc_average(val1,val2,val3,val4,val5)
    print_output(val1,val2,val3,val4,val5,avg)
    
def get_input():
    grade1 = int(input('Введите первую оценку: '))
    grade2 = int(input('Введите вторую оценку: '))
    grade3 = int(input('Введите третью оценку: '))
    grade4 = int(input('Введите четвертую оценку: '))
    grade5 = int(input('Введите пятую оценку: '))
    return grade1,grade2,grade3,grade4,grade5

def calc_average(v1,v2,v3,v4,v5):
    return (v1+v2+v3+v4+v5)/5

def determine_grade(val):
    if val >= 90:
        return('A')
    elif val >= 80 and val < 90:
        return('B')
    elif val >= 70 and val < 80:
        return('C')
    elif val >= 60 and val < 70:
        return('D')
    else:
        return ('F')

def print_output(sc1,sc2,sc3,sc4,sc5,avg):
    print('\n')
    print('='*20)
    print('Балл\t\tОценка')
    print('='*20)
    print(f'|{sc1}\t\t{determine_grade(sc1)}|')
    print(f'|{sc2}\t\t{determine_grade(sc2)}|')
    print(f'|{sc3}\t\t{determine_grade(sc3)}|')
    print(f'|{sc4}\t\t{determine_grade(sc4)}|')
    print(f'|{sc5}\t\t{determine_grade(sc5)}|')
    print('='*20)
    print('Средний балл')
    print('='*20)
    print(f'|{avg}\t\t{determine_grade(avg)}|')
    print('='*20)

main()
