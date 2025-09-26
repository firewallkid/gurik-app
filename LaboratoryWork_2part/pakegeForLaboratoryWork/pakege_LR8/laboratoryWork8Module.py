import random
from tabulate import tabulate


def generate_students(n, subjects):
    surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов",
                "Васильев", "Козлов", "Морозов", "Новиков", "Федоров"]
    students = []
    for i in range(n):
        surname = random.choice(surnames)
        grades = {subject: random.randint(2, 5) for subject in subjects}
        students.append([surname, grades])
    return students


def print_students_matrix(matrix, headers):
    print(tabulate(matrix, headers=headers, tablefmt="grid"))


def find_max_even_grade(matrix, subjects):
    """Находит максимальную четную оценку выше главной диагонали"""
    even_count = 0
    odd_count = 0
    max_even = None

    for i, student in enumerate(matrix):
        for j in range(i + 1, len(subjects)):
            if j >= len(subjects):
                continue
            subject = subjects[j]
            grade = student[1].get(subject, 0)

            if grade % 2 == 0:  # Изменено условие на четность
                even_count += 1
                if max_even is None or grade > max_even:
                    max_even = grade
            else:
                odd_count += 1

    return max_even if even_count > odd_count else None  # Изменено условие возврата


def analyze_students(matrix, subjects):
    """Анализирует студентов и возвращает данные для таблицы и сообщение"""
    max_even = find_max_even_grade(matrix, subjects)

    # Формируем данные для таблицы
    analyzed_data = []
    filtered_students = []

    for i, student in enumerate(matrix, 1):
        surname = student[0]
        grades = student[1]
        avg = sum(grades.values()) / len(grades)
        analyzed_data.append([i, surname] + [grades[subj] for subj in subjects] + [f"{avg:.2f}"])

        # Формируем запись для фильтрации
        if max_even is not None and avg < max_even:
            entry = f"{i} - {surname}, Средний балл: {avg:.2f}"
            filtered_students.append(entry)

    # Формируем сообщение
    message = ""
    if max_even is not None:
        message = f"Максимальная четная оценка выше диагонали: {max_even}"
        if filtered_students:
            message += "\nСтуденты с средним баллом ниже:\n" + '\n'.join(filtered_students)
        else:
            message += "\nНет студентов с средним баллом ниже максимальной четной оценки"
    else:
        message = "Количество нечетных оценок выше или равно четным в элементах выше диагонали"

    return analyzed_data, message
