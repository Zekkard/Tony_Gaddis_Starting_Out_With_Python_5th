# На диске существует файл students.txt. Он содержит несколько записей, и каждая запись имеет два поля: 
# имя студента и оценку студента за итоговый экзамен. 
# Напишите программу, которая удаляет запись с именем студента "Джон Перц".

# В этой задаче я хотел впервые обратится к файлу из исходного кода, прилагаемого к учебнику.
# Однако этого файла в репозитории учебника не оказалось. Класс. А значит придётся писать собственный.

# Импорт библиотек
import os
import random as r
def create_file():
    os.makedirs('data', exist_ok=True)
    outfile = open('data/students.txt','w')
    students_num = int(input('Какое количество студентов вы хотите добавить: '))
    # outfile.write('ФИ студента\nОценка за итоговый экзамен\n') 
    # Меня аж корёжит от вертикального хранения атрибутов с убогим заголовком.
    # Но в главе примеров с горизонтальным хранением не приводилось.
    for i in range(students_num):
        student_name = str(input('Введите имя и фамилию студента. Пример Вася Пупкин: '))
        score = r.randint(50,100)
        outfile.write(f'{student_name}\n{score}\n')
    student_name = 'Джон Перц'
    score = '20' # Извини Джон Перц, это тебе за отсутствие файла в репо, все вопросы к автору учебника.
    outfile.write(f'{student_name}\n{score}\n')
    student_name = 'Джулия Милан'
    score = '00' # Извини Джулия Милан, я в след. задаче снова обнаружил ссылку на несуществующего студента.
    outfile.write(f'{student_name}\n{score}\n')
    outfile.close()

def main():
    try: 
        infile = open('data/students.txt','r')
        temp_file = open('data/temp.txt','w')
        search = 'Джон Перц'
        found = False
        name = infile.readline()
        while name != '':
            score = infile.readline()
            name = name.rstrip('\n')
            if name != search:
                temp_file.write(f'{name}\n{score}') # в score уже содержится \n
            else:
                found = True
            name = infile.readline()
        infile.close()
        temp_file.close()
        os.remove('data/students.txt')
        os.rename('data/temp.txt','data/students.txt')
        if found:
            print('Задача завершена. Файл обновлён.')
        else:
            print('Такой студент отсутствует, файл перезаписан, но не обновлён.')

    except FileNotFoundError as err:
        print(f"""А прикол в том, что в репозитории учебника не было такого файла.
Поэтому лови '{err}'.
А сейчас ты попадёшь в программу, позволяющую создать нужный файл.""")
        create_file()
        print('Файл создан! Перезапустите программу.')
main()