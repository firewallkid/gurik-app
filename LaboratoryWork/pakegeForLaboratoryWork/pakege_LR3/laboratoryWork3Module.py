from math import *


def main(a, x, y):
    if -2 < x + y < 2:
        print('Выполнение первой ветви...')
        return first(a, x, y)
    elif x + y <= -2:
        print('Выполнение второй ветви...')
        return second()
    else:
        print('Выполнение третьей ветви...')
        return third(a, x, y)


def first(a, x, y):
    min1 = (sin(a * x)) ** 2
    if cos(y) ** 2 < min1:
        min1 = cos(y) ** 2
    if y + x < min1:
        min1 = y + x
    l = min1
    return l


def second():
    return 1


def third(a, x, y):
    max1 = y
    if max1 < sqrt(abs(a + x)):
        max1 = sqrt(abs(a + x))
    if max1 < log(abs(y * x)):
        max1 = log(fabs(y * x))
    l = max1
    return l
