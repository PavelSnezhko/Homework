list = []
for number in range (0, 101):
    list.append(number)
print(list)
for number in list:
    last_number = 0
    if number >20:
        last_number = number % 10
    if number == 1 or last_number == 1:
        print(number, 'процент')
    elif 1 < number < 5 or 1 < last_number < 5:
        print(number, 'процента')
    else:
        print(number, 'процентов')
