q = 0  # показатель счётчика второго цикла
w = int(input())  # ввод
c = 1  # числа для вывода
pr = ' '
while c < w:
    for j in range(q):
        if c == w:  # это для пробелов
            pr = ''
        print(c, end=pr)  # выводим число, в конце оставляем pr
        c += 1
        if c > w:
            break
    print('')
    q += 1
