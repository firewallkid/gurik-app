import sqlite3, csv, openpyxl, os
from docx import Document
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sr_ball = 4.5

def create_db():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            name TEXT,
            math INTEGER,
            physics INTEGER,
            programming INTEGER
        )
    """)
    students_data = [
        ("Иванов Иван", 4, 5, 3),
        ("Петров Петр", 3, 4, 2),
        ("Сидоров Алексей", 5, 5, 4),
        ("Козлова Мария", 4, 3, 5),
        ("Смирнова Анна", 3, 4, 4),
        ("Иванов Петр", 4, 5, 5)
    ]
    cursor.executemany(
        "INSERT INTO students (name, math, physics, programming) VALUES (?, ?, ?, ?)",
        students_data
    )
    connection.commit()
    connection.close()

def get_students_from_db():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name, math, physics, programming FROM students")
    students = [{"name": row[0], "math": row[1], "physics": row[2], "programming": row[3]} for row in cursor.fetchall()]
    connection.close()
    return students

def find(students, sr_ball):
    rez_spisok = []
    for student in students:
        student["score"] = (student["math"] + student["physics"] + student["programming"]) / 3
        if student["score"] >= sr_ball:
            rez_spisok.append(student)
    return rez_spisok

def scan():
    students = get_students_from_db()

    max_average_score = 0
    best_student = None

    for student in students:
        scores = [student["math"], student["physics"], student["programming"]]
        even = [num for num in scores if num % 2 == 0]
        odd = [num for num in scores if num % 2 != 0]

        if len(even) >= len(odd):
            average_score = sum(scores) / len(scores)
            if average_score > max_average_score:
                max_average_score = average_score
                best_student = student["name"]

    if best_student:
        print(f"\nМаксимальный средний балл студента, у которого количество"
              f"\nчетных оценок не меньше, чем четных у {best_student}: {max_average_score:.2f}")
    else:
        print(f"У всех студентов количество четных оценок меньше, чем нечетных.")


def save_to_excel(rez_spisok):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Высокий средний балл"
    sheet.append(["Студент", "Средний балл"])
    for student in rez_spisok:
        sheet.append([student["name"], student["score"]])
    workbook.save("Spisok.xlsx")
    print("Результаты сохранены в файл Excel")


def save_to_word(students, rez_spisok):
    doc = Document()
    doc.add_heading("Список студентов", level=1)
    for student in students:
        doc.add_paragraph(f"{student['name']} - Математика: {student['math']}, Физика: {student['physics']}, Программирование: {student['programming']}")

    doc.add_heading("Студенты с высоким средним баллом", level=1)
    for student in rez_spisok:
        doc.add_paragraph(f"{student['name']} - Средний балл: {student['score']:.2f}")

    doc.save("Списки в Word.docx")
    print("Результаты сохранены в файл Word")


def save_to_pdf(students):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Arial", "", os.path.join("C:\\Windows\\Fonts", "arial.ttf"), uni=True)
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "СПИСОК СТУДЕНТОВ", ln=True, align='C')
    pdf.ln(5)

    for student in students:
        pdf.cell(200, 10, f"{student['name']} - Математика: {student['math']}, Физика: {student['physics']}, Программирование: {student['programming']}", ln=True)

    pdf.output("Списки.pdf")
    print("Результаты сохранены в файл PDF")

def save_lists_to_csv(original_list, filtered_list):
    with open("students_lists.csv", mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Исходный список студентов"])
        for student in original_list:
            writer.writerow([student["name"], student["math"], student["physics"], student["programming"]])
        writer.writerow([])
        writer.writerow(["Студенты с высоким средним баллом"])
        for student in filtered_list:
            writer.writerow([student["name"], student["score"]])
    print("Результаты сохранены в students_lists.csv")

def diagram_student(students):
    names = [student["name"] for student in students]
    math_scores = [student["math"] for student in students]
    physics_scores = [student["physics"] for student in students]
    programming_scores = [student["programming"] for student in students]
    x = np.arange(len(names))
    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, math_scores, width, label = 'Математика')
    rects2 = ax.bar(x - width, physics_scores, width, label = 'Физика')
    rects3 = ax.bar(x + width, programming_scores, width, label = 'Программирование')
    ax.set_xlabel("Студенты")
    ax.set_ylabel("Оценки")
    ax.set_title("Оценки студентов по предметам")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation = 45, ha = "right")
    ax.legend()
    plt.tight_layout()
    plt.show()


def calculate(csv_filename):
    male=0
    female=0
    count=0
    with open(csv_filename,newline='',encoding='utf-8') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row["Male Height in Cm"] and row["Female Height in Cm"]:
                male+=float(row["Male Height in Cm"])
                female+=float(row["Female Height in Cm"])
                count+=1
        if count>0:
            male=male/count
            female=female/count
        else:
            male=0
            female=0
        return male,female

def calc_pandas(csv_file):
    df = pd.read_csv(csv_file)
    avg_male_height = df["Male Height in Cm"].mean()
    avg_female_height = df["Female Height in Cm"].mean()
    return avg_male_height, avg_female_height


def filter_countries(csv_filename):
    filtered = []
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for raw in reader:
            male = float(raw["Male Height in Cm"])
            if 175 <= male <= 179:
                filtered.append((raw["Rank"], raw["Country Name"], male))
        return filtered
def filt_countries(csv_file):
    df = pd.read_csv(csv_file)
    df["Male Height in Cm"] = pd.to_numeric(df["Male Height in Cm"], errors = "coerce")
    filtered_df = df[(df["Male Height in Cm"] >= 175) & (df["Male Height in Cm"] <= 179)]
    return filtered_df[["Rank", "Country Name", "Male Height in Cm"]]


def find_shortest(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    shortest_male = min(data, key=lambda x: float(x["Male Height in Cm"]))
    shortest_female = min(data, key=lambda x: float(x["Female Height in Cm"]))

    return shortest_male["Country Name"], shortest_female["Country Name"]
def find_shortest_pandas(csv_file):
    df = pd.read_csv(csv_file)
    shortest_male = df.nsmallest(10, "Male Height in Cm")[["Country Name", "Male Height in Cm"]]
    shortest_female = df.nsmallest(10, "Female Height in Cm")[["Country Name", "Female Height in Cm"]]
    return shortest_male["Country Name"], shortest_female["Country Name"]

