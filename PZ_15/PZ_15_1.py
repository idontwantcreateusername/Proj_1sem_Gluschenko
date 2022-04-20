# В матрице элементы второго столбца возвести в квадрат
# Вариант 5
import numpy as np

print('\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(int(y) ** 2) if list(x).index(y) == 2 else str(y), x))),
                         np.random.randint(0, 100, (int(input('введите количество строк: ')),
                                                   int(input('введите количество столбцов: '))))))))
