from CheckValid import check
from random import shuffle

with open('words.txt', 'r') as f:
    words = f.read().split()
shuffle(words)

print('Давай сыграем в слова!')
print('Начинай!')

his = []
MyWord = ''
while True:
    word = input().lower()
    # if not(word in words):
    #     print('Не знаю такого слова')

    if word == '':
        continue

    if MyWord != '':
        MyW = MyWord[-2] if MyWord[-1] in ['ь', 'ы', 'ъ'] else MyWord[-1]
        if word[0] != MyW:
            print('Ты должен сказать слово на букву "' + MyW + '"')
            continue

    if word in his:
        print('Зто слово уже было')
        continue

    status = check(word)
    if status == -1:
        print('Этого слова нет ни в одном из популярных словарей, придумай другое')
        continue
    if status == 0:
        print('Можно использовать только существительные в инфинитиве')
        continue

    w = word[-2] if word[-1] in ['ь', 'ы', 'ъ'] else word[-1]

    MyWord = ''
    for el in words:
        if el[0] == w and not(el in his):
            print(el)
            his.append(word)
            his.append(el)
            words.pop(words.index(el))
            MyWord = el
            break

    if MyWord == '':
        print('Поздравляю! Ты победил, я больше не знаю слов на букву "' + w + '".')
        exit()

