# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр
# целого положительного числа K, а также их сумму S (K — входной, C и S —
# выходные параметры целого типа). С помощью этой функции найти количество
# и сумму цифр для каждого из пяти данных целых чисел.

def digit_count_sum(k):  # functions names must be in lowercase
    q = len(str(k))  # фиксируем длину числа, которая будет выступать счётчиком
    s = 0  # объявление суммы
    while q:
        q -= 1  # счётчик
        s += int(str(k)[q])   # прибавлям к сумме цифру
    return len(str(k)), s  # возвращаем длину числа и сумму цифр


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


answ = digit_count_sum(abs(intinput('введите число\n')))  # вычисление
print('сумма цифр {}, колличество цифр {}'.format(answ[1], answ[0]))  # вывод
