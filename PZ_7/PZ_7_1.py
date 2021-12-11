# Дано целое число N(1 < N < 26). Вывести N последних строчных букв латинского алфавита в обратном порядке
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


def notbiggerinput(txt, f, s=0):   # функция, принимающая число в определенном промежутке
    while True:
        w = intinput(txt)
        if w >= f or w <= s:
            print('введите корректное значение\n')
        else:
            return w


for i in range(notbiggerinput('введите N\n', 26, 1)):
    print(chr(122 - i))  # вывод n-ной с конца буквы алфавита
