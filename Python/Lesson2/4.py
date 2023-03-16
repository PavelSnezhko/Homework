workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in workers:
    split = worker.split()
    print('Привет, ' + split[-1].title() + '!')