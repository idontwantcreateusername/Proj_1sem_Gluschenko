def intinput(output=''):  # функция ввода с проверкой на инт
    print(output, end='')
    input1 = True
    v1 = 't'
    while input1:  # проверка условия

        try:
            v1 = int(input())  # ввод
        except ValueError:  # обработка исключения
            a = 0  # загушка, требовавшаяся для модификации
        if type(v1) == int and v1 > 0:  # проверка на инт + модификация для отбивания отрицательных
            input1 = False
        else:
            print('введите корректное значение\n')
    return v1


def notbiggerinput(txt, f, s=0):
    while True:
        w = intinput(txt)
        if w >= f or w <= s:
            print('введите корректное значение\n')
        else:
            return w


p = input('введите предложение\n')
k = notbiggerinput('введите К\n', 10, 0)
nstr = ''
for i in p:
    if i.isalpha():
        v = i
        i = chr(ord(i) + k)
        if ord(i) > 1071 > ord(v) or ord(i) > 1103 > ord(v):
            i = chr(ord(i) - 33)
    nstr += i
print(nstr)
