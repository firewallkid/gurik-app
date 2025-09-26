import math
from cgitb import reset
from math import *
from openpyxl import Workbook
from docx import Document
import sqlite3


def create_db():
    # Создает базу данных и таблицу для хранения значений n, R и S
    conn = sqlite3.connect('C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.db')
    cursor = conn.cursor()
    # Создание таблицы, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculate_S_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            n REAL NOT NULL,            
            R REAL NOT NULL,
            S REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert_into_db(n, R, S):
    """
    Вставляет данные в базу данных.
    :param n: Количество углов в многоугольнике.
    :param R: Значение R.
    :param S: Значение S.
    """
    conn = sqlite3.connect('C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.db')
    cursor = conn.cursor()
    # Вставка значения n, R и S
    cursor.execute("INSERT INTO calculate_S_table (n, R, S) VALUES (?, ?, ?)", (n, R, S))
    conn.commit()
    conn.close()


def tabulate_S(R):
    """
    Табулирует заданную функцию и записывает результаты в текстовый файл и Excel.
    :param R: Радиус окружности.
    """
    # Вывод в консоль

    # Сохранение в текстовый файл
    with open("C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.txt", "w") as txt_file:
        result10 = calculate_polygon_area(10, R)
        result50 = calculate_polygon_area(50, R)
        result100 = calculate_polygon_area(100, R)
        # Вывод в консоль
        print(f"{'n':>4} | {'R':>3} | {'S':>4}")
        print("-" * 19)
        print(f"{'10':>4} | {R} | {result10:.4f}")
        print(f"{'50':>4} | {R} | {result50:.4f}")
        print(f"{'100':>4} | {R} | {result100:.4f}")
        print("-" * 19)

        txt_file.write(f"{'n':>4} | {'R':>3} | {'S':>4}\n")
        txt_file.write("-" * 19)
        # Запись в текстовый файл
        txt_file.write(f"\n{'10':>4} | {R} | {result10:.4f}\n")
        txt_file.write(f"{'50':>4} | {R} | {result50:.4f}\n")
        txt_file.write(f"{'100':>4} | {R} | {result100:.4f}\n")
        txt_file.write("_" * 19 + "\n")

        # Сохранение в Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "calculate_S_table"
        ws.append(["n", "R", "S"])
        # Запись в Excel
        ws.append([10, R, result10])
        ws.append([50, R, result50])
        ws.append([100, R, result100])
        # Сохранение файлов
        wb.save("C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.xlsx")

        # Сохранение в Word
        doc = Document()
        doc.add_heading("Вычисление значения S", level=1)
        table = doc.add_table(rows=1, cols=3)
        table.style = 'Table Grid'
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'n'
        hdr_cells[1].text = 'R'
        hdr_cells[2].text = 'S'
        # Запись в Word
        row_cells_1 = table.add_row().cells
        row_cells_1[0].text = '10'
        row_cells_1[1].text = f"{R:.4f}"
        row_cells_1[2].text = f"{result10:.4f}"
        row_cells_2 = table.add_row().cells
        row_cells_2[0].text = '50'
        row_cells_2[1].text = f"{R:.4f}"
        row_cells_2[2].text = f"{result50:.4f}"
        row_cells_3 = table.add_row().cells
        row_cells_3[0].text = '100'
        row_cells_3[1].text = f"{R:.4f}"
        row_cells_3[2].text = f"{result100:.4f}"
        # Сохранение файлов
        doc.save("C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.docx")

        # Запись в базу данных
        insert_into_db(10, R, round(result10, 4))
        insert_into_db(50, R, round(result50, 4))
        insert_into_db(100, R, round(result100, 4))
        conn = sqlite3.connect('C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculate_S_table")
        results = cursor.fetchall()
        conn.close()
        print(
            "\nТаблица сохранена в файлы: \n'calculate_S_table.txt', \n'calculate_S_table.xlsx', \n'calculate_S_table.docx'. \nДанные записаны в таблицу")


def execute_query(query, params=None):
    """
    Это функция для выполнения SQL-запроса.
    В зависимости от того, передаются ли параметры она выполняет запрос с параметрами или без них
    :param query: Строка SQL-запроса.
    :param params: Параметры для SQL-запроса (если есть).
    """
    conn = sqlite3.connect('C:/Users/demak/PycharmProjects/pythonProject/LaboratoryWork/pakegeForLaboratoryWork/pakege_LR5/calculate_S_table.db')
    cursor = conn.cursor()
    # Курсор - это объект, предоставляемый модулем sqlite3.
    # Он отвечает на выполнение SQL-запросов и управление результатами этих запросов.
    # После выполнения запроса, например, SELEcT, курсор содержит результаты запроса,
    # которые можно извлекать методом fetchone()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    # Получаем все строки результата
    rows = cursor.fetchall()
    # Печатаем результаты
    for row in rows:
        print(row)

    conn.close()  # Закрываем соединение


def example():
    # Пример запроса: Получить все записи из таблицы
    print("Все записи из базы данных:")
    execute_query("SELECT * FROM calculate_S_table;")


def calculate_polygon_area(n, R):
    """
    Вычисляет площадь правильного n-угольника, вписанного в окружность радиуса R.

    Параметры:
    :param n (int) количество сторон n-угольника
    :param R (float) радиус вписанной окружности

    Возвращает:
    float - площадь n-угольника
    """
    S = 0.5 * calculate_len_side(n, R) * n * calculate_r(n, R)  # вычисление площади n-угольника
    return S

def calculate_r(n, R):
    r = R * cos(pi/n)
    return r

def calculate_len_side(n, R):
    a = 2 * R * sin(math.pi / n)  # вычисление длины стороны n-угольника
    return a
