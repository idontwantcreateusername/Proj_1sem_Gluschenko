# Даны два числа: А и В. Проверить истинность высказывания : «Справедливы
# неравенства А > 0 или B < -2».

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


a = intinput('введите а \n')  # ввод
b = intinput('введите b \n')
if a > 0 or b < -2:  # проверка соответствию условия
    print('высказывание справедливо')
else:
    print('высказывание не справедливо')
