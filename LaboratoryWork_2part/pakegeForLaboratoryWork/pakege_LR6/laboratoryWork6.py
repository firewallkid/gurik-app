from .laboratoryWork6Module import *


n = int(input("Введите размерность матрицы: "))
matrix = rnd(n, n)
print("Сгенерированная последовательность:")
prnt(matrix)

max_odd, odd_count, even_count = find_max_odd_above_diagonal(matrix)
if odd_count > even_count:
    new_array = create_new_array(matrix, max_odd)
    print(f"\nМаксимальный нечетный элемент выше диагонали: {max_odd}")
    prnt(new_array, n=len(matrix))  # Передаем размерность исходной матрицы
    save_to_file(
        "file6.txt",
        matrix, max_odd, new_array)

    save_to_binary(
        "binary6.bin",
        matrix, max_odd, new_array)
    matrix, max_odd = load_from_binary(
        "binary6.bin")
    print("\nМаксимальное нечетное:", max_odd)
    print("Загруженные данные из бинарного файла:")
    print(matrix)

    save_to_shelve(
        "shelve6.db",
        matrix, max_odd)
    matrix, max_odd = load_from_shelve(
        "shelve6.db")
    print("Максимальное нечетное:", max_odd)
    print("Загруженные данные из shelve:")
    print(matrix)
else:
    print("Количество нечетных элементов меньше, чем четных.")

