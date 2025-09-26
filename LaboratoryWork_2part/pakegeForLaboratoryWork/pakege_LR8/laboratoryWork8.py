from .laboratoryWork8Module import *

num_students = int(input("Введите количество студентов: "))
subjects = ["Математика", "Физика", "Информатика", "Химия"]
students = generate_students(num_students, subjects)

analyzed_data, message = analyze_students(students, subjects)

headers = ["№", "Фамилия"] + subjects + ["Средний балл"]
print_students_matrix(analyzed_data, headers)
print("\n" + message)
exit()