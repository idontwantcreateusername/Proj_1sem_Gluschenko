row = int(input('введите количество рядов: '))
column = int(input('введите количество столбцов(>2): '))
matrix = []
for i in range(column):  # вводим матрицу
    a = []
    for j in range(row):
        a.append(int(input('введите {} элемент {} столбца\n'.format(j + 1, i + 1))))
    matrix.append(a)

matrix[1] = list(i ** 2 for i in matrix[1])  # вычисляем

for i in range(row):  # выводим матрицу
    for j in range(column):
        print(matrix[j][i], end=" ")
    print()
