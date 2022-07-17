distance = int(input('Введите результат в км за первый день: '))
target_distance = int(input('Введите цель которой хотите достич в км: '))
count = 1

while distance < target_distance:
    print(f'{count}-й день: {round(distance, 2)}')
    distance += distance * 0.1
    count += 1
else:
    print(f'{count}-й день: {round(distance, 2)}')
    print(f'На {count}-ой день вы достигнете результата - не менее {target_distance} км.')