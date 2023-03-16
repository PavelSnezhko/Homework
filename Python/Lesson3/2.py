def num_translate_adv(number):
    translations = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    translated = translations.get(number.lower())
    if number.istitle() and translated:
        return translated.capitalize()
    else:
        return translated

# Пример использования функции
print(num_translate_adv('one'))  # выведет 'один'
print(num_translate_adv('Five'))  # выведет 'Пять'
print(num_translate_adv('Ten'))  # выведет 'Десять'
print(num_translate_adv('Eleven'))  # выведет None
