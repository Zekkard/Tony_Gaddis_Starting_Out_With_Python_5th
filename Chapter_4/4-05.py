total = 0
second_val = 30
for i in range (1,31):
    iter_val = i / second_val
    total += iter_val
    second_val -= 1
print(total)