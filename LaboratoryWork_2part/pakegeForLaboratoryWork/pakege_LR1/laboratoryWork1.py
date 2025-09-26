from .laboratoryWork1Module import *

try:
    size = int(input('Введите размер массива: '))
    lower_bound = int(input('Введите минимальный возможный элемента массива: '))
    upper_bound = int(input('Введите максимальный возможный элемента массива: '))
    random_list = generation_random_list(size, lower_bound, upper_bound)
except Exception as e:
    print(f"Ошибка: {e}")

print("\nИсходный список:", random_list)
result_list(random_list)
