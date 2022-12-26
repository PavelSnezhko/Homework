#create list
list = []
for numbers in range (1, 1000):
    if numbers % 2:
        number = numbers ** 3
        list.append(number)
print(list)
#get sum
summary = 0
for number in list:
    while number > 0:
        sum = 0
        digit = number % 10
        sum = sum + digit
        number = number // 10
        if sum % 7:
            summary = summary + number
print(summary)
#change list
list = [number + 17 for number in list]
summary == 0
for number in list:
    while number > 0:
        sum = 0
        digit = number % 10
        sum = sum + digit
        number = number // 10
        if sum % 7:
            summary = summary + number
print(summary)