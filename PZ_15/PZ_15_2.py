# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
row = int(input('введите количество рядов: '))
column = int(input('введите количество столбцов(>2): '))
matrix = []


def genpz(w):  # генератор
    w = 0 if w % 2 != 0 else w
    yield w


for i in range(column):  # вводим матрицу
    a = []
    for j in range(row):
        a.append(int(input('введите {} элемент {} столбца\n'.format(j + 1, i + 1))))
    matrix.append(a)

matrix = list(list(next(genpz(j)) for j in q) for q in matrix)  # вычисляем

for i in range(row):  # выводим матрицу
    for j in range(column):
        print(str(matrix[j][i]), end=" ")
    print()
