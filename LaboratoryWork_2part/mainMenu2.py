while True:
    print('\nМеню:'
          '\n0 - выйти'
          '\n1 - выполнить первую лабораторную работу'
          '\n2 - выполнить вторую лабораторную работу'
          '\n5 - выполнить пятую лабораторную работу'
          '\n6 - выполнить шестую лабораторную работу'
          '\n7 - выполнить седьмую лабораторную работу'
          '\n8 - выполнить восьмую лабораторную работу'
          '\n11 - выполнить одиннадцатую лабораторную работу'
          '\n12 - выполнить двенадцатую лабораторную работу')

    try:
        numberWork = int(input('Введите номер лабораторной работы: '))

        if numberWork == 0:
            print('Завершение работы')
            exit()  # Выход из программы
        elif numberWork == 1:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR1.laboratoryWork1
        elif numberWork == 2:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR2.laboratoryWork2
        elif numberWork == 5:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR5.laboratoryWork5
        elif numberWork == 6:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR6.laboratoryWork6
        elif numberWork == 7:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR7.laboratoryWork7
        elif numberWork == 8:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR8.laboratoryWork8
        elif numberWork == 11:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR11.laboratoryWork11
        elif numberWork == 12:
            import LaboratoryWork_2part.pakegeForLaboratoryWork.pakege_LR12.laboratoryWork12
        else:
            print('Ошибка: Введите число из списка (0, 1, 2, 5, 6, 7, 8)')

    except ValueError:
        print('Ошибка: Введите число, а не текст!')