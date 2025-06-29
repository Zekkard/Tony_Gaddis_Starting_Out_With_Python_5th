# Напишите программу, которая делает следующее: открывает файл number_list.txt, созданный
# программой, которую вы написали в задаче 3, читает все числа из файла, выводит их на экран и затем закрывает файл.

def main():
    infile = open('data/number_list.txt','r')
    for i in infile:
        print(i.rstrip('\n'))
    infile.close()
main()