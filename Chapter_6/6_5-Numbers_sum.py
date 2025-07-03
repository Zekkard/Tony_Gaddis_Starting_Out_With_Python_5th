# Сумма чисел. Допустим, что файл с рядом целых чисел называется numbers.txt и существует
# на диске компьютера. Напишите программу, которая читает все хранящиеся
# в файле числа и вычисляет их сумму.

# Файл numbers.txt взят из исходного кода учебника.

def main():
    infile = open('data/numbers.txt','r')
    sum = 0
    for line in infile:
        sum += int(line)
    infile.close()
    print(sum)
main()