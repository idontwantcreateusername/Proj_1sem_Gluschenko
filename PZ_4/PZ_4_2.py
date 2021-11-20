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


q = int(abs(intinput('введите целое число \n')))
smm = 0  # сумма
zzzz = 0   # это для цикла(счётчик)
while zzzz != len(str(q)):  # злая версия того форового цикла
    smm += int(str(q)[zzzz])
    zzzz += 1

# for i in str(q):  # этот цикл был прекрасен, но вы запретили форы...
#  smm += int(i)
print('количество цифр: {}, сумма цифр: {}'.format(len(str(q)), smm))
