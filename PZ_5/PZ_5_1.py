def horizontal(q):  # функция проведения горизонтальной стороны рамки
    if q:  # проверка на нижнюю или верхнюю
        print('╔═══════════════════╗')
    else:
        print('╚═══════════════════╝')


def vertical():  # функия вывода вертикальных сторон
    print('║                   ║')


def worder(wrd):  # функция вывода слова в рамке
    print('║', end='')
    print(' ' * (9 - len(wrd) // 2), end='')
    print(wrd, end='')
    print(' ' * (9 - len(wrd) // 2 + 1 - len(wrd) % 2), end='')
    print('║')


w = input('введите слово короче 19 символов\n')
while len(w) > 19:  # проверка на правильную длину
    print('ваше слово длиннее 19 символов')
    w = input('введите слово короче 19 символов')
horizontal(True)
vertical()
vertical()


worder(w)

vertical()
vertical()
horizontal(False)  # вывод слова и рамки
