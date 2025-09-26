from laboratoryWork2Module import *
import tabulate

create_db()
students = get_students_from_db()
print('\nСписок студентов в базе данных:')
table = tabulate.tabulate(students, headers='keys', tablefmt='grid')
print(table)
rez_spisok = find(students, sr_ball)
print('\nРезультирующий список студентов, чей средний балл больше 4,5')
print(tabulate.tabulate(rez_spisok))
save_to_excel(rez_spisok)
save_to_word(students, rez_spisok)
save_lists_to_csv(original_list=students, filtered_list=rez_spisok)
save_to_pdf(students)
scan()
diagram_student(students)
csv_file = "Height of Male and Female by Country 2022.csv"
male, female = calc_pandas(csv_file)

filtered_countries1=filter_countries("Height of Male and Female by Country 2022.csv")
for rank,country,height in filtered_countries1:
    print(f"{rank}. {country}: {height} см")
filtered_countries2=filt_countries("Height of Male and Female by Country 2022.csv")
print(filtered_countries2.to_string(index=False))


shortest_male1,shortest_female1=find_shortest("Height of Male and Female by Country 2022.csv")
print(f"Страна с самыми низкими мужчинами: {shortest_male1}")
print(f"Страна с самыми низкими женщинами: {shortest_female1}")
shortest_male2,shortest_female2=find_shortest_pandas("Height of Male and Female by Country 2022.csv")
print(f"Страна с самыми низкими мужчинами: {shortest_male2}")
print(f"Страна с самыми низкими женщинами: {shortest_female2}")

