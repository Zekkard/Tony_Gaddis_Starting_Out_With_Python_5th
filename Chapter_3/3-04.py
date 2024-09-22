score = int(input("Введите итоговый бал за экзамен: "))
A_score = 5
B_score = 4
C_score = 3
D_score = 2
if score >= A_score:
    print("Ваш уровень - A.")
if score >= B_score:
    print("Ваш уровень - B.")
if score >= C_score:
    print("Ваш уровень - C.")
if score >= D_score:
    print("Ваш уровень - D.")
else:
    print("Ваш уровень - F.")