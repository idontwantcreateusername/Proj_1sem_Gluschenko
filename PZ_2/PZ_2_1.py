q = 0  # для ачивки
input1 = True
input2 = True
input3 = True
input4 = True  # для проверки
v1 = 'something'
v2 = 'something'
t = 'something'
s = 'something'  # основные переменные
print('^y    --              --  ')
print('|    /0--0-         -0--0-')
print('┴────────────────────────>x')  # рисунок условия(физика из меня не искоренить

while input1:  # проверка условия

    try:
        v1 = int(input('введите скорость первой машины относительно оси x в км/ч \n'))  # ввод
    except ValueError:  # обработка исключения
        print('введите корректное значение\n')
        q += 1  # для заработки ачивки
        if q == 100:  # ачивка
            print('achievement unlocked "навиженiй"\n')
    if type(v1) == int:  # проверка на инт
        input1 = False

while input2:  # тут всё то же самое

    try:
        v2 = int(input('введите скорость второй машины относительно оси x в км/ч(для движеня навстречу введите'
                       ' отрицательной)\n'))
        # должен уточнить, что скорость движения навстречу относительно оси х будет отрицательной
    except ValueError:
        print('введите корректное значение\n')
        q += 1
        if q == 200:
            print('achievement unlocked "всё в порядке?\n"')
    if type(v2) == int:
        input2 = False

while input3:  # ввод времени

    try:
        t = int(input('введите время в часах\n'))
    except ValueError:
        print('введите корректное значение\n')
        q += 1
        if q == 300:
            print('achievement unlocked "стоит переосмыслить свою жизнь"\n')
    if type(t) == int:
        input3 = False

while input4:  # ввод расстояния

    try:
        s = int(input('введите исходное расстояние между машинами в км\n'))
    except ValueError:
        print('введите корректное значение')
        q += 1
        if q == 400:
            print('achievement unlocked "эх, мне бы столько времени"\n')
    if type(t) == int:
        input4 = False

print('Ответ: ' + str(abs(s - t * (v1 - v2))))  # вывод резульата
