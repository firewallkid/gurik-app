from .laboratoryWorkModule6 import *

try:
    a = float(input("Введите начало интервала: "))
    b = float(input("Введите конец интервала: "))
    if a >= b:
        raise ValueError("Ошибка: a должно быть меньше b")
    root = newton_method(a, b)

except Exception as e:
    print(f"Ошибка: {e}")