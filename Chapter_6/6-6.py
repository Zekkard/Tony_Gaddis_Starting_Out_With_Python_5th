# Напишите программу, которая делает следующее: открывает выходной файл с именем
# number_list.txt, применяет цикл для записи в файл чисел с 1 по 100, а затем закрывает файл.

# Импорт библиотек
import os

def main():
    os.makedirs('data',exist_ok=True)
    outfile = open('data/number_list.txt','w')
    for i in range(1,101):
        outfile.write(f'{i}\n')
    outfile.close()
main()