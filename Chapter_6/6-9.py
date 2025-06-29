# Напишите программу, которая открывает файл вывода number_list.txt, но не стирает содержимое файла, если он уже существует.

def main():
    outfile = open('data/number_list.txt','a')
    # outfile = open('data/number_list.txt', 'r')
    outfile.close()
main()