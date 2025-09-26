numberWork = None
while numberWork != 0:
    print('Меню '
          '\n0 - выйти'
          '\n1 - выполнить первую лабораторную работу'
          '\n2 - выполнить вторую лабораторную работу'
          '\n3 - выполнить третью лабораторную работу'
          '\n4 - выполнить четвёртую лабораторную работу'
          '\n5 - выполнить пятую лабораторную работу'
          '\n6 - выполнить шестую лабораторную работу')
    numberWork = int(input('Введите номер лабораторной работы: '))
    if numberWork == 0:
        print('Завершение работы')
    elif numberWork == 1:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR1.laboratoryWork1
    elif numberWork == 2:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR2.VvodVivod
    elif numberWork == 3:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR3.laboratoryWork3
    elif numberWork == 4:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR4.laboratoryWork4
    elif numberWork == 5:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR5.laboratoryWork5
    elif numberWork == 6:
        import LaboratoryWork.pakegeForLaboratoryWork.pakege_LR6.laboratoryWork6
    else:
        print('Неверный ввод'
          '\nЗавершение работы')
    exit()