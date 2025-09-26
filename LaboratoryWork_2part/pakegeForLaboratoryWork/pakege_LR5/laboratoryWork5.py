from .laboratoryWork5Module import *

n = int(input("Введите размерность матрицы: "))
matrix = rnd(n, n)
print("Сгенерированная последовательность:")
prnt(matrix)

max_odd, odd_count, even_count = find_max_odd_above_diagonal(matrix)

if odd_count > even_count:
    print(f"Максимальный нечетный элемент выше главной диагонали: {max_odd}")
    new_array = create_new_array(matrix, max_odd)
    print("Новый массив из элементов, меньших максимального нечетного:")
    print(new_array)
else:
    print("Количество четных элементов больше, чем нечетных.")

# Вариант 1
# Ввод размеров последовательности

'''
matrica = generate(n, m)
print("Сгенерированная последовательность:")
print_matr(matrica)'''


# Вариант 2
'''
matrix = generate_random_matrix(n, m)
print_matrix(matrix)
avg_positive, count_zeros = calculate_stats(matrix)
print(f"Среднее арифметическое положительных элементов: {avg_positive:.2f}")
print(f"Количество нулевых элементов: {count_zeros}")
'''
