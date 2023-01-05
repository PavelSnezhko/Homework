list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers = None
for index, objects in enumerate(list):
    try:
        numbers = int(objects)
    except ValueError:
        numbers = None
        pass
    if isinstance(numbers, int) == True:
        list[index] = ('"' + objects + '"')
print(list)