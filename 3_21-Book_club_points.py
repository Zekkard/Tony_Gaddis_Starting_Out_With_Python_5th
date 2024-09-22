books_bought_cnt = int(input('Введите количество книг, которые вы купили в этом месяце: '))
if books_bought_cnt < 0:
    print('Введены некорректные данные. Количество книг не может быть меньше нуля.')
elif books_bought_cnt >= 8:
    book_points = 60
elif books_bought_cnt >= 6:
    book_points = 30
elif books_bought_cnt >= 4:
    book_points = 15
elif books_bought_cnt >=2:
    book_points = 5
elif books_bought_cnt < 2:
    book_points = 0
print(f'В этом месяце вы заработали {book_points} очков.')