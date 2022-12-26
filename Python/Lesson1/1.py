#asking user for time duration
dur = int(input('Введите продолжительность в секундах: '))
#Select days\hours\minutes\seconds
def convert_to_dd_hh_mm_ss(sec):
    sec = sec % (24 * 86400)
    days = sec // 86400
    sec %= 86400
    hours = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return '%02d:%02d:%02d:%02d' % (days, hours, min, sec)
#Return
print('Продолжительность: ', convert_to_dd_hh_mm_ss(dur))
