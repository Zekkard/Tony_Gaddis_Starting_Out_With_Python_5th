# Математический тест. Напишите программу, которая позволяет проводить простые
# математические тесты. Она должна показать два случайных числа, которые должны
# быть просуммированы вот так:
# 247
# + 129
# Эта программа должна давать обучаемому возможность вводить ответ. Если ответ правильный,
# то должно быть показано поздравительное сообщение. Если ответ неправильный,
# то должно быть показано сообщение с правильным ответом.

# Библиотеки
import random

def main():
    num1=random.randint(1,999)
    num2=random.randint(1,999)
    correct_answer = num1 + num2
    display_test_question(num1,num2)
    user_answer = student_test()
    answer_check(correct_answer,user_answer)
    
def display_test_question(n1,n2):
    print(f"""Сколько будет
{n1}
+ {n2}?""")

def student_test():
    return int(input('Введите ответ: '))

def answer_check(correct,answer):
    if correct == answer:
        return print(f'{answer} это правильный ответ!')
    else:
        return print(f'Неверно, правильный ответ {correct}')
main()