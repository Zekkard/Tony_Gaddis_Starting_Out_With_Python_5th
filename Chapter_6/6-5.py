# Напишите программу, которая открывает файл my_name.txt, созданный программой в задаче 1, читает ваше имя из файла, выводит имя на экран и затем закрывает файл.
# Исполнять после 6-4.py
# Меня тут немного понесло... Два режима + обработчик ошибок. Я намеренно не заморачиваюсь с ошибками для файла.
def main():
    infile = open('data/my_name.txt','r')
    try:
        read_mode = int(input('Читаем с помощью цикла while или for? 1 - для while: '))
    except ValueError as err:
        print(f"""Вообще подразумевалось, что вы введёте числовой ответ, 
но вы ввели нечто такое, что вызвало ошибку 
"{err}". 
А раз так - я буду считать, что должен запустить for.\n""")
        read_mode = 2
    finally:    
        if read_mode == 1:
            print('Окей, читаем через while.')
            line = infile.readline()
            while line != '' :
                print(line)
                line = infile.readline()
        else:
            print('Окей, читаем через for.')
            for i in infile:
                print(i)
        infile.close()
main()