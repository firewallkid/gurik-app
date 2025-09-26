while True:
    print('Меню '
          '\n0 - выйти'
          '\n1 - перейти к первому семестру'
          '\n2 - перейти ко второму семестру')

    try:
        number = int(input('Введите номер семестра: '))

        if number == 0:
            print('Завершение работы')
            exit()
        elif number == 1:
            import LaboratoryWork.mainMenu1
        elif number == 2:
            import LaboratoryWork_2part.mainMenu2
        else:
            print('Неверный ввод. Пожалуйста, введите 0, 1 или 2.')

    except ValueError:
        print('Ошибка ввода. Пожалуйста, введите число (0, 1 или 2).')