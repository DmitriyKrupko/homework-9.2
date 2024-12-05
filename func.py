import random
def args_list(x):
    rand_list = []
    n = x
    for i in range(n):
        rand_list.append(random.randint(0, 100))
    return rand_list
#Формируем список из произвольных значений
def three_lst(rand_list):
    three_list = sorted(rand_list)[:3]
    return three_list
#Выдёргиваем из списка три значения
def averege(three_list):
    averege_list = sum(three_list) / len(three_list)
    return averege_list
#Считаем среднее значение
def min_max_arg(three_list):
    maximum = max(three_list)
    minimum = min(three_list)
    print('Максимальное значение чисел: ', maximum)
    print('Минимальное значение чисел: ', minimum)
#Определяем минимальные и максимальные значения   