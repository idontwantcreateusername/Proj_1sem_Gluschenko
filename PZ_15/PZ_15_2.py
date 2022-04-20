# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import numpy as np
print('\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(0) if y % 2 == 1 else str(y), x))),
                         np.random.randint(0, 10, (int(input('введите количество строк: ')),
                                                   int(input('введите количество столбцов: '))))))))
