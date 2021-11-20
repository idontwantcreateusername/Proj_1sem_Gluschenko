def intinput(output=''):  # функция ввода с проверкой на инт
    print(output, end='')
    input1 = True
    v1 = 't'
    while input1:  # проверка условия

        try:
            v1 = int(input())  # ввод
        except ValueError:  # обработка исключения
            print('введите корректное значение\n')
        if type(v1) == int:  # проверка на инт
            input1 = False
    return v1


q = intinput('введите цену конфет за 1 кг\n')  # ввод
# for i in range(12, 22, 2):
#    print('цена за {}кг: {}'.format(i / 10, q * i / 10))  # цикл с выводом
c = 12
while c < 22:
    print('цена за {}кг: {}'.format(c / 10, q * c / 10))
    c += 2
