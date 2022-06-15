def cnt(p, res=0):  # сумма в обычных списках
    return cnt(p[1:], res + p[0]) if len(p) else res


def jnt(p, res=0):  # сумма во вложенных списках
    res += cnt(p[0], 0) if type(p[0][0]) is int else jnt(p[0], 0)
    return jnt(p[1:], res) if len(p) > 1 else res


def mnt(p, res=0):  # подсчёт отрицательных
    return int(mnt(p[1:], res + p[0] / abs(p[0]) - 1) if len(p) else res / -2)


def fib(p, res=[1, 1]):  # возврат фиибоначи до определённого элемента
    if 2 < p:
        res.append(res[-1] + res[-2])
        res = fib(p - 1, res)
    return res


def rev(p, res=0):  # реверсирование числа
    return rev(p // 10, res * 10 + p % 10) if p else res


def dmf(res, p, d):  # возведение в степень
    return dmf(res * d, p - 1, d) if p > 1 else res


def mcf(p, res=-999999):  # максимальный элемент в списках
    return mcf(p[1:], p[0] if p[0] > res else res) if len(p) > 0 else res


def dtb(p, res=''):  # перевод в двоичную систему
    return dtb(p // 2, str(p % 2) + str(res)) if p > 1 else int('1' + str(res))


qw = [9, 9, 9, 9]
print('сумма во обычных списках:', cnt(qw))

qw = [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
print('сумма во вложенных списках:', jnt(qw))

qw = [[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
      [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
      [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]]
print('сумма во вложенных списках(трехмерный):', jnt(qw))

qw = [-9, 9, -9, -9]
print('подсчёт отрицательных:', mnt(qw))

qw = 12
print('Фиббоначи:', fib(qw))

qw = 234234
print('реверсирование числа:', rev(qw))

qw = 3
wq = 4
print('возведение в степень:', dmf(qw, wq, qw))

qw = [9, 3, 13, 25]
print('максимальный элемент в списках:', mcf(qw))

qw = 2022
print('перевод в двоичную систему:', dtb(qw))
