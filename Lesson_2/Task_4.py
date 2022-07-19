user_string = str(input('Введите предложение: '))
count = 0
new_string = user_string.split()

for word in new_string:
    count += 1
    if len(word) > 10:
        print(f'{count}) {word[:11]} - Слово длинное. Напечатано только 10 символов')
    else:
        print(f'{count}) {word.upper()} - длина слова {len(word)}')
