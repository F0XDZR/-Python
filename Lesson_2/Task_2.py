value_list = input('Введите через пробел несколько элементов списка: ').split()

print(f'{value_list} - исходный список')

last_num = len(value_list) - 1

for i in range(0, last_num, 2):
    value_list[i], value_list[i+1] = value_list[i+1], value_list[i]

print(f'{value_list} - измененный список')





