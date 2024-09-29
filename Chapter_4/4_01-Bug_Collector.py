bug_cnt = 0
for day in range(1,8):
    bug_cnt += int(input(f'Сколько ошибок было обнаружено в день {day}? '))
print(f'За {day} дней обнаружено {bug_cnt} ошибок.')