# Генератор персональной веб-страницы. Напишите программу, которая запрашивает
# у пользователя его имя и просит пользователя ввести предложение, которое его описывает.
# Вот пример экрана программы:
# Введите свое имя: Джулия Тейлор [ Enter]
# Опишите себя: Моя специализация - информатика, я являюсь членом джаз-клуба
# и надеюсь стать разработчиком мобильных приложений после того, как получу
# высшее образование. [ Enter 1
# После того как пользователь ввел требуемые входные данные, программа должна создать
# файл HTML и записать в него полученные входные данные для создания простой
# 364 Глава б. Файлы и исключения
# веб-страницы. Вот пример содержимого файла HTML с использованием ранее показанных
# входных данных:
# <html>
# <head>
# </head>
# <body>
# <center>
# <h1>Джулия Тейлор</h1>
# </center>
# <hr />
# Моя специализация - информатика, я являюсь членом джаз-клуба
# и надеюсь стать разработчиком мобильньх приложений после того,
# как получу высшее образование.
# <hr />
# </body>
# </html>

# Импорт библиотек
import os

def main():
    os.makedirs('data',exist_ok=True)
    name = input('Введите ваше имя: ')
    info = input('Расскажите о себе: ')
    outputfile = open('data/index.html','w')
    outputfile.write('<html>\n')
    outputfile.write('\t<head>\n')
    outputfile.write('\t\t<title>My Page</title>\n')
    outputfile.write('\t\t<meta charset ="utf-8">\n') # Вот только в учебнике не учитывается, что его будут читать в странах, где используют кириллицу.
    outputfile.write('\t</head>\n')
    outputfile.write('\t<body>\n')
    outputfile.write('\t\t<center>\n')
    outputfile.write(f'\t\t\t<center>\n')
    outputfile.write(f'\t\t\t<h1>{name}</h1>\n')
    outputfile.write(f'\t\t\t</center>\n')
    outputfile.write('\t\t<hr />\n')
    outputfile.write(f'\t\t{info}\n')
    outputfile.write('\t\t<hr />\n')
    outputfile.write('\t</body>\n')
    outputfile.write('</html>')
    outputfile.close()
    
main()