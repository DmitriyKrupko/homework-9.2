import random

def args_list(x):
    rand_list = []
    n = x
    for i in range(n):
        rand_list.append(random.randint(0, 100))
    
    three_list = sorted(rand_list)[:3]
    
    averege_list = sum(three_list) / len(three_list)
    
    maximum = max(three_list)
    minimum = min(three_list)
    
    print("Список значений:", rand_list)
    print("Список из трёх значений:", three_list)
    print("Среднее значение:", averege_list)
    print('Максимальное значение чисел: ', maximum)
    print('Минимальное значение чисел: ', minimum)
    
    return