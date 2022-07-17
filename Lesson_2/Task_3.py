dict_month = {
    1: 'В январе Зима',
    2: 'В феврале Зима',
    3: 'В марте Весна',
    4: 'В апреле Весна',
    5: 'В мае Весна',
    6: 'В июне Лето',
    7: 'В июле Лето',
    8: 'В августе Лето',
    9: 'В сентябре Осень',
    10: 'В октябре Осень',
    11: 'В ноябре Осень',
    12: 'В декабре Зима',
}

list_winter = [1, 2, 12]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]

user_input = int(input('Введите номер месяца: '))

print(f'{dict_month[user_input]}')

if user_input in list_winter:
    print('Зимой холодно. Одевайтесь теплее!')
elif user_input in list_spring:
    print('А весной все еще прохладно.')
elif user_input in list_summer:
    print('Летом тепло и солнышко!')
elif user_input in list_autumn:
    print('Осень - Красивая пора')
