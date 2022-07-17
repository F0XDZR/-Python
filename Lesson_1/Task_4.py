user_number = input('Введите любое целое положительное число: ')
max_num = 0
i = 0
print(f'Вы ввели {user_number}, его длина {len(user_number)} цифр(ы)')

while i < int(len(user_number)):
    if int(user_number[i]) >= max_num:
        max_num = int(user_number[i])
    i += 1

print(f'Максимальная цифра из вашего числа - {max_num}')
