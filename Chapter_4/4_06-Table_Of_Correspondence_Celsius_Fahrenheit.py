c_end = 20
print('Таблица соответствий температур\nC\tF')
print('-'*20)
for c in range(c_end+1):
    f = 9 / 5 * c + 32
    print(f'{c}\t{f:.1f}')