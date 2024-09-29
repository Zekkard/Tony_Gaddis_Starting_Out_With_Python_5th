ocean_level = 0.0
print('Год\tУровень океана')
print('-'*20)
for i in range(1,26):
    ocean_level += 1.6
    print(f'{i}\t{ocean_level:.2f}')