# Дан список А размера N  целые числа K и L(1 < K < L < N). Переставить в обратном порядке элементы списка,
# расположенные между К-нным и  N-ным элементами,включая эти элементы
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


q = []
for i in range(notbiggerinput("введите длину списка(должна быть не меньше 4)\n", 999999999, 3)):
    q.append(input('введите {}-ый элемент списка\n'.format(i + 1)))
k = notbiggerinput('введите К\n', len(q))
lv = notbiggerinput('введите L\n', len(q), k)
nwlst = q[k:lv + 1]
nwlst.reverse()
print(nwlst)
