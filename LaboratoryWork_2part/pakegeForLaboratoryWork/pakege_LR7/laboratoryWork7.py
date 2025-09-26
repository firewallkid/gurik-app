from .laboratoryWork7Module import *

txt_file = "file7.txt"
excel_file = "file7.xlsx"
word_file = "file7.docx"
sql_file = "file7.db"


n = int(input("Введите размерность матрицы: "))
matrix = rnd(n, n)
print("Сгенерированная последовательность:")
prnt(matrix)

max_odd, odd_count, even_count = find_max_odd_above_diagonal(matrix)
if odd_count > even_count:
    new_array = create_new_array(matrix, max_odd)
    print(f"\nМаксимальный нечетный элемент выше диагонали: {max_odd}")
    prnt(new_array)  # Вывод нового массива в виде одномерного списка

    save_to_file(txt_file, matrix, max_odd, new_array)
    save_to_excel(excel_file, matrix, max_odd)
    save_to_word(word_file, matrix, max_odd, new_array)
    save_to_sqlite(sql_file, matrix, max_odd)


else:
    print("Количество нечетных элементов меньше, чем четных.")
