print('Программа переводит секунды в "чч:мм:сс" и выводит на экран.')

user_input = int(input('Введите секунды: '))

seconds = user_input % 60
minutes = (user_input // 60) % 60
hours = round((user_input / 60) // 60)

print(f'{user_input} секунд это - {hours:02} : {minutes:02} : {seconds:02}')
