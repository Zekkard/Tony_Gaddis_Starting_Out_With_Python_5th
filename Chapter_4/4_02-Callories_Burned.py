burned_callories = 0
bpm_factor = 4.2 #burn per minute
for minutes in range(10,31,5):
    burned_callories += minutes * bpm_factor
    print(f'За {minutes} минут было сожжено {burned_callories} каллорий.')
print(f'Всего за {minutes} минут было сожжено {burned_callories} каллорий.')