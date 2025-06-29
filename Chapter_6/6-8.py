# Измените программу, которую вы написали в задаче 4 таким образом, чтобы она суммировала
# все прочитанные из файла числа и выводила на экран их сумму.

def main():
    infile = open('data/number_list.txt','r')
    sum = 0
    for i in infile:
        sum += int(i)
    print(sum)
    infile.close()
main()