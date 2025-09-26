import math
from .calculationFormula import *
print("Выполнение лабораторной работы №2")

x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))
if x * y == 0:
    print("Ошибка: y не должно быть равно нулю.")
else:
    c = formula(x, y)
    print('Значение c= ', '{0:.3f}'.format(c))

k = int(c)
l = int(c)
m = math.ceil(c)
n = math.floor(c)

print('Целая часть результата (неявно) k=', k)
print('Целая часть результата (явно) l =', l)
print('Округление в большую сторону m =', m)
print('Округление в меньшую сторону n =', n)
#оператора инкрементации нет в python, поэтому расчет инкремента невозможен
print('Значение k после приращения =', k+1)
print('Значение l после приращения =', l+1)
exit()

