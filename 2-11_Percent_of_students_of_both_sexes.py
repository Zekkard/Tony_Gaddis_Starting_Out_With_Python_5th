male = int(input('Введите количество учащихся мужского пола: '))
female = int(input('Введите количество учащихся женского пола: '))
total_students = male + female
male_percent = (male / total_students) * 100
female_percent = (female / total_students) * 100
print(f'В классе {male_percent} % мальчиков и {female_percent} % девочек.')