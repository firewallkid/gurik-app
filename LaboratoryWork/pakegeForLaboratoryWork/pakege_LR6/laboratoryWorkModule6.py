import openpyxl
from openpyxl import Workbook


def log_iteration_to_file(iteration, x, fx, dfx, file_name="calculate.txt"):
    """
    Функция для записи данных об одной итерации в файл.
    :param file_name: Имя файла
    :param iteration: Номер итерации
    :param x: Текущее значение х
    :param fx: Значение функции f(x)
    :param dfx: Значение производной f'(x)
    """
    with open(file_name, "a") as file:
        file.write(f"Итерация {iteration:10} | x:{x:12.6f} | f(x):{fx:12.6f} | df(x):{dfx:12.6f}\n")


def log_iteration_to_excel(iteration, x, fx, dfx, file_name="calculate.xlsx"):
    """
    :param file_name: Имя файла
    :param iteration: Номер итерации
    :param x: Текущее значение x
    :param fx: Значение функции f(x)
    :param dfx: Значение производной f'(x)
    """
    try:
        workbook = openpyxl.load_workbook("calculate.xlsx")
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Calculate"
        sheet.append(["Итерация", "x", "f(x)", "f'(x)"])
    sheet.append([iteration, x, fx, dfx])
    workbook.save(file_name)


def newton_method(a, b, tochn=1e-6, max_iter=100, file_name="calculate.txt"):
    """
    :param a: Значение начала отрезка.
    :param b: Значение конца отрезка.
    :param tochn: Точность вычисления
    :param max_iter: Максимально допустимое количество итераций.
    :param file_name: Имя файла.
    """
    with open(file_name, "w"):
        x = (a + b) / 2
        iteration = 1
        while iteration <= max_iter:
            # Вычисляем f(x) и f'(x) вручную
            fx = function(x)
            dfx = Dfunction(x)
            if dfx == 0:
                raise ValueError("Производная равна нулю!")
            x_new = x - fx / dfx
            if abs(x_new - x) < tochn:
                print(f"\nКорень найден за {iteration} итераций.\nНайденный корень: {x:.4f}")
                print(f"Проверка: f({x:.6f}) = {function(x):.6e}")
                with open("calculate.txt", 'a') as file:
                    file.write(f"\nКорень найден за {iteration} итераций.\nНайденный корень: {x:.4f}")
                log_iteration_to_excel("Результат", x_new, 0, "-")
                return x_new
            log_iteration_to_file(iteration, x, fx, dfx)
            log_iteration_to_excel(iteration, x, fx, dfx)
            x = x_new
            iteration += 1
    print("Достигнуто максимальное количество итераций.")


def function(x):
    fx = x ** 5 - x - 1
    return fx


def Dfunction(x):
    dfx = 5 * x ** 4 - 1
    return dfx