import random, pickle, shelve

def rnd(n, m):
    """Создание двумерного списка"""
    a = []
    for i in range(n):
        a.append([random.randint(-10, 10) for _ in range(m)])
    return a

def prnt(a, n=None):
    """Универсальный вывод матриц и одномерных массивов"""
    if isinstance(a[0], list):  # Для матрицы
        print("Сгенерированная последовательность:")
        for row in a:
            print(" ".join(f"{num:5d}" for num in row))
    else:  # Для одномерного массива
        if n:  # Форматируем как квадратную матрицу
            print("\nНовый массив в виде квадратной матрицы:")
            for i in range(0, len(a), n):
                row = a[i:i+n] + [0]*(n - len(a[i:i+n]))
                print(" ".join(f"{num:5d}" for num in row))
        else:  # Обычный вывод в строку
            print(" ".join(f"{num:5d}" for num in a))

def find_max_odd_above_diagonal(matrix):
    """Нахождение максимального нечетного элемента списка над верхней диагональю"""
    max_odd = -11
    odd_count = even_count =  0
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):  # Элементы выше главной диагонали
            num = matrix[i][j]
            if num % 2 != 0:  # Проверка на нечетность
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

# Запись матрицы и результатов в текстовый файл (Блокнот)
def save_to_file(filename, a, max_odd, new_array):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Матрица:\n")
        for row in a:
            file.write(" ".join(f"{num:3d}" for num in row) + "\n")
        file.write(f"\n\nМаксимальный нечетный элемент выше главной диагонали: {max_odd}\n")
        file.write(f"\nНовый массив из элементов, меньших максимального нечетного: {new_array}\n")
        print("\nДанные сохранены в файл 'file.txt'.")

# Запись матрицы и результатов в бинарный файл
def save_to_binary(filename, a, max_odd, new_array):
    data = {
        "matrix": a,
        "max_odd": max_odd,
        "new_array": new_array,
    }
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print("Данные сохранены в файл 'binary.bin'.")

# Загрузка данных из бинарного файла
def load_from_binary(filename):
    with open(filename, "rb") as file:
        data = pickle.load(file)
    return data["matrix"], data["max_odd"]

# Сохранение с использованием метода shelve
def save_to_shelve(filename, a, max_odd):
    with shelve.open(filename) as db:
        db["matrix"] = a
        db["max_odd"] = max_odd
    print("\nДанные сохранены в файл 'shelve.db'.")

# Загрузка данных из shelve
def load_from_shelve(filename):
    with shelve.open(filename) as db:
        matrix = db.get("matrix", [])
        max_odd = db.get("max_odd", 0)
    return matrix, max_odd
