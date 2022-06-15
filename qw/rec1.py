def cnt(p, res):  # сумма в обычных списках
    res += p[0]
    if len(p) > 1:
        res = cnt(p[1:], res)
    return res


def jnt(p, res):  # сумма во вложенных списках
    res += cnt(p[0], 0) if type(p[0][0]) is int else jnt(p[0], 0)
    if len(p) > 1:
        res = jnt(p[1:], res)
    return res


def mnt(p, res):  # подсчёт отрицательных
    res += p[0] / abs(p[0]) - 1
    if len(p) > 1:
        res = cnt(p[1:], res)
    else:
        res /= -2
    return int(res)


def fib(p, res):
    if 2 < p:
        res.append(res[-1] + res[-2])
        res = fib(p - 1, res)
    return res


def rev(p, res):
    if p:
        res = res * 10 + p % 10
        res = rev(p // 10, res)
    return res


def dmf(res, p, d):
    if p > 1:
        res *= d
        res = dmf(res, p - 1, d)
    return res


def mcf(p, res):  # сумма в обычных списках
    res = p[0] if p[0] > res else res
    if len(p) > 1:
        res = mcf(p[1:], res)
    return res


def dtb(p, res):  # сумма в обычных списках
    res += p % 2 * 10
    if p == 1:
        res = cnt(p // 2, res)
    return res



qw = [9, 9, 9, 9]
print(cnt(qw, 0))
qw = [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
print(jnt(qw, 0))

qw = [[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
      [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]],
      [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]]
print(jnt(qw, 0))

qw = 12
print(fib(qw, [1, 1]))

qw = 234234
print(rev(qw, 0))

qw = 3
wq = 4
print(dmf(qw, wq, qw))

qw = [9, 3, 13, 2]
print(mcf(qw, 0))

qw = 123
print(dtb(qw))