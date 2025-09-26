from .laboratoryWork4Module import *

b = float(input("Введите конец отрезка: ")) # b = 0.7
a = -10 * b
h = b / 2
print('Начало отрезка (a) = ', a)
print('Шаг (h) = ', h)
create_db()
tabulate_y(a, b, h)
example()
