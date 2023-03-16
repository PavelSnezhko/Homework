from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes():
    '''
    1 choose noun
    2 choose adverb
    3 choose adjective
    :return:
    '''
    joke1 = choice(nouns)
    joke2 = choice(adverbs)
    joke3 = choice(adjectives)
    return joke1, joke2, joke3
#тест
print(get_jokes())
