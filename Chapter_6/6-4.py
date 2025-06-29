# Напишите программу, которая открывает файл вывода my_name.txt, пишет в него ваше имя и затем его закрывает.
# Импорт библиотек
import os

def main():
    os.makedirs('data',exist_ok=True) # Команда проверяет существование папки data, если папка отсутствует - создаёт её
    outfile = open('data/my_name.txt','w')
    my_name = input('Введите своё имя: ')
    outfile.write(f'{my_name}.')
    outfile.close()
main()