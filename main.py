from func import args_list, three_lst, averege, min_max_arg
x = int(input('Введите длинну списка: '))
print(args_list(x))
print(three_lst(args_list(x)))
print('Среднее значение чисел: ', averege(three_list=(args_list(x)))) 
min_max_arg(three_list=(args_list(x)))