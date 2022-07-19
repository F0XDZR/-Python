natural_numbers = [7, 5, 3, 3, 2]

print(f'{natural_numbers} - Исходный список')

user_num = int(input('Введите натуральное число: '))

# Вариант решения №1
result1 = natural_numbers.copy()
result1.append(user_num)
print(f'{sorted(result1, reverse=True)} - вариант №1')

# Вариант решения №2
result2 = natural_numbers.copy()
len_list = len(result2)

if user_num in result2:
    for i in range(len(result2)):
        if user_num != result2[i]:
            continue
        else:
            if i == len(result2) - 1:
                result2.append(user_num)
                break
            elif user_num != result2[i + 1]:
                result2.insert(i + 1, user_num)
                break
else:
    for i in range(len(result2)):
        if user_num > result2[i]:
            result2.insert(i, user_num)
            break
        elif i == len(result2) - 1:
            result2.append(user_num)
print(f'{result2} - вариант №2')