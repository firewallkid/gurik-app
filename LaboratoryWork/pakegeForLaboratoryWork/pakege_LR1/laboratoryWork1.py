import math
x = float(input('Введите значение x '))
y = float(input('Введите значение y '))
if x == 0 or y == 0:
    print('Деление на ноль невозможно')
else:
    c = x * math.log10(x - 6) - math.sin(x * x) / y * x * x * x

k = int(c)
l = int(c)
m = math.ceil(c)
n = math.floor(c)

print('Значение c= ', '{0:.3f}'.format(c))
print('Целая часть результата (неявно) k=', k)
print('Целая часть результата (явно) l =', l)
print('Округление в большую сторону m =', m)
print('Округление в меньшую сторону n =', n)
#оператора инкрементации нет в python, поэтому расчет инкремента невозможен
print('Значение k после приращения =', k+1)
print('Значение l после приращения =', l+1)
exit()
