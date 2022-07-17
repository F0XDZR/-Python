user_string = str(input('Введите предложение: '))

new_string = user_string.split()

for word in new_string:
    if len(word) > 10:
        print(f'{word[:11]} - Слово длинное. Напечатано только 10 символов')
    else:
        print(f'{word.upper()} - длина слова {len(word)}')
