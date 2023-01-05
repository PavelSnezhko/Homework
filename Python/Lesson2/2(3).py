list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers = None
for objects in list:
    try:
        numbers = int(objects)
    except ValueError:
        numbers = None
        pass
    if isinstance(numbers, int) == True:
        print('"', objects, '"')
    else:
        print(objects)