def intinput(output, k):  # функция ввода с проверкой на инт + введите true для игнорирования отрицательных
    print(output, end='')
    input1 = True
    v1 = 't'
    while input1:  # проверка условия

        try:
            v1 = int(input())  # ввод
        except ValueError:  # обработка исключения
            a = 0  # загушка, требовавшаяся для модификации
        if type(v1) == int and (v1 > 0 or k):  # проверка на инт + модификация для отбивания отрицательных
            input1 = False
        else:
            print('введите корректное значение\n')
    return v1


dct = {}  # создание словаря
for i in range(intinput('введите количество ключей словаря\n', True)):  # ввод словаря
    dct[input('введите его ключ: \n')] = input('введите значение:\n')

if ('фрукт', 'яблоко') in dct.items():  # поиск яблок
    print("неизменённый: ", dct)
else:
    print('исходный:', dct)
    dct['фрукт'] = 'яблоко'  # добавление яблока
    print('изменённый:', dct)
