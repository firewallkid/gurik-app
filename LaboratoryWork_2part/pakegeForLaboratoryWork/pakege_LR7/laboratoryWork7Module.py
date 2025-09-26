import random, openpyxl, sqlite3
from docx import Document

def rnd(n, m):
    """Создание двумерного списка"""
    a = []
    for i in range(n):
        a.append([random.randint(-10, 10) for _ in range(m)])
    return a

def prnt(a):
    """Универсальный вывод матриц и одномерных массивов"""
    if isinstance(a[0], list):  # Для матрицы
        print("Сгенерированная последовательность:")
        for row in a:
            print(" ".join(f"{num:5d}" for num in row))
    else:  # Для одномерного массива
        print("\nНовый массив в виде списка:")
        print(f"[{', '.join(map(str, a))}]")  # Форматируем как список

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

def save_to_file(filename, a, max_odd, new_array):
    """Сохранение матрицы и результатов в текстовый файл"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Матрица:\n")
        for row in a:
            file.write(" ".join(f"{num:3d}" for num in row) + "\n")
        file.write(f"\n\nМаксимальный нечетный элемент выше главной диагонали: {max_odd}\n")
        file.write(f"\nНовый массив из элементов, меньших максимального нечетного: {new_array}\n")
        print("\nДанные сохранены в файл 'file.txt'.")

def save_to_excel(filename, matrix, max_odd):
    """Сохранение матрицы и результатов в Excel"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matrix"

    for i in range(len(matrix)):  # Индексы строк
        for j in range(len(matrix[i])):  # Индексы столбцов
            ws.cell(row=i + 1, column=j + 1, value=matrix[i][j])

    ws.cell(row=len(matrix) + 2, column=1, value="Максимальный нечетный элемент выше главной диагонали:")
    ws.cell(row=len(matrix) + 2, column=2, value=max_odd)

    wb.save(filename)
    print("Данные сохранены в файл 'file.xlsx'.")

def save_to_word(filename, matrix, max_odd, new_array):
    """Сохранение матрицы и результатов в документ Word"""
    doc = Document()

    # Заголовок для матрицы
    doc.add_heading("Матрица", level=1)

    # Добавление матрицы в документ
    for row in matrix:
        doc.add_paragraph(" ".join(f"{num:5d}" for num in row))

    # Добавление максимального нечетного элемента
    doc.add_heading("Результаты", level=1)
    doc.add_paragraph(f"Максимальный нечетный элемент выше главной диагонали: {max_odd}")

    # Добавление нового массива
    doc.add_paragraph(f"Новый массив из элементов, меньших максимального нечетного: {new_array}")

    # Сохранение документа
    doc.save(filename)
    print(f"Данные сохранены в файл 'file.docx'.")

def save_to_sqlite(db_name, a, max_odd):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Создание таблицы "matrix"
    cursor.execute("DROP TABLE IF EXISTS matrix")
    cursor.execute("CREATE TABLE matrix (row_idx INTEGER, col_idx INTEGER, value INTEGER)")
    for i in range(len(a)):
        for j in range(len(a[i])):
            cursor.execute("INSERT INTO matrix (row_idx, col_idx, value) VALUES (?, ?, ?)", (i, j, a[i][j]))

    # Создание таблицы "results"
    cursor.execute("DROP TABLE IF EXISTS results")
    cursor.execute("CREATE TABLE results (max_odd INTEGER)")
    cursor.execute("INSERT INTO results (max_odd) VALUES (?)", (max_odd,))

    conn.commit()
    conn.close()
    print(f"Данные сохранены в файл 'file.db'.")
