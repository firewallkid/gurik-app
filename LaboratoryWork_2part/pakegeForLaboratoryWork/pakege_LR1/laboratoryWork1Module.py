import random

def generation_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for i in range(size)]

def result_list(random_list):
    even = odd = 0
    for i in random_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even < odd:
        print('Четных чисел меньше, чем нечетных.\n', even, '<', odd)
    else:
        mx = max([i for i in random_list if i % 2 == 0])
        print('Количество четных чисел:', even)
        print('Максимальное четное число:', mx)

    result = [i for i in random_list if i > even]
    print('Массив состоящий из элементов исходного, значения которых больше количества четных чисел:\n', result)