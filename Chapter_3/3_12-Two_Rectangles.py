a = int(input('Введите длину первого прямоугольника: '))
b = int(input('Введите высоту первого прямоугольника: '))
c = int(input('Введите длину второго прямоугольника: '))
d = int(input('Введите высоту второго прямоугольника: '))
area_rect1 = a * b
area_rect2 = c * d
if area_rect1 > area_rect2:
    print('Площадь первого прямоугольника больше.')
elif area_rect1 < area_rect2:
    print('Площадь второго прямоугольника больше.')
else:
    print('Площадь прямоугольников равны.')