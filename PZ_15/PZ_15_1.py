# В матрице элементы второго столбца возвести в квадрат
# Вариант 5
print('\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(int(y) ** 2) if x.index(y) == 1 else str(y), x)
                                                 )), list(
    map(lambda n: n.split(), input('введите матрицу разделяя строки" | "(в одну строку)\n').split('|')))))))
