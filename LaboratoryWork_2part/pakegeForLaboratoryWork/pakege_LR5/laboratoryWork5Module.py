import random

def rnd(n, m):
    """Создание двумерного списка"""
    a = []
    for i in range(n):
        a.append([random.randint(-10, 10) for _ in range(m)])
    return a

def prnt(a):
    """Вывод двумерного списка"""
    for row in a:
        print(" ".join(f"{num:5d}" for num in row))

def find_max_odd_above_diagonal(matrix):
    """Нахождение максимального нечетного элемента списка над верхней диагональю"""
    max_odd = -11
    odd_count = even_count =  0
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):  # Элементы выше главной диагонали
            num = matrix[i][j]
            if num % 2 != 0:
                odd_count += 1
                if num > max_odd:
                    max_odd = num
            else:
                even_count += 1

    return max_odd, odd_count, even_count

def create_new_array(matrix, max_odd):
    """Создание результирующего одномерного массива,
    содержащего элементы двумерного массива,
    значения которых меньше максимального нечетного элемента"""
    new_array = []
    for row in matrix:
        for num in row:
            if num < max_odd:
                new_array.append(num)
    return new_array


# Вариант 2
def generate_random_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:3d}" for num in row))
    print()

# Вариант 3
def generate(n, m):
    return [[i + j for j in random.sample(range(35), m)] for i in random.sample(range(45), n)]

def print_matr(matrica):
    for row in matrica:
        for num in row:
            print(f"{num:3d}", end=" ")
        print()