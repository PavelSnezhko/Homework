def thesaurus(*args):
    workers = {}
    for name in args:
        first_letter = name[0]
        if first_letter in workers:
            workers[first_letter].append(name)
        else:
            workers[first_letter] = [name]
    return workers
# Тест
names = ["Игорь", "Денис", "Илья", "Елена", "Мария", "Мария"]
print(thesaurus(*names))