import time

from .laboratoryWorkModule5 import *

R = float(input("Введите радиус вписанной окружности: "))
create_db()
start_time = time.time()
tabulate_S(R)
end_time = time.time()
calc_time = end_time - start_time
print(f"\nВремя выполнения программы: {calc_time:.6f} секунд")
example()
