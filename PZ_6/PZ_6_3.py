# Дан список размера N. Обнулить все его локальные максимумы ( то есть числа, большие своих соседей)
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


q = []
w = intinput("введите длину списка\n", False)
for i in range(w):
    q.append(intinput('введите {}-ый элемент списка\n'.format(i + 1), True))

for i in range(1, len(q) - 1):
    if q[i] > q[i + 1] and q[i - 1] < q[i]:
        q[i] = 0
print(q)
