# Счетчик значений. Допустим, что файл с серией имен (в виде строковых значений)
# называется names.txt и существует на диске компьютера. 
# Напишите программу, которая показывает количество хранящихся в файле имен. (Подсказка: откройте файл и прочитайте
# каждую хранящуюся в нем строку. Используйте переменную для подсчета количества прочитанных из файла значений.)

# Файл names.txt взят из исходного кода учебника.

def main():
    infile = open('data/names.txt','r')
    work_mode = int(input('Если читаем через цикл For введите 1. While введите 2 : '))
    rows_cnt = 0
    if  work_mode == 1:
        print('Читаем через For')
        for line in infile:
            rows_cnt += 1
    else:
        print('Читаем через While')
        line = infile.readline()
        while line != '':
            line = infile.readline()
            rows_cnt += 1
    infile.close()
    print(rows_cnt)
main()