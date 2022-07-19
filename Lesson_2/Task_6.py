
product_list = []
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
analytics_dict = {}
name_list = []
price_list = []
count_product_list = []
units_list = []
count = 0
user_input = None

while user_input != 'q':
    print('\n------------- Добрый день -------------')
    print('Что хотите сделать?')
    print('Добавить товар - "+"')
    print('Посмотреть меню - "m"')
    print('Выйти - "q"')
    user_input = input('\nВведите команду: ')
    if user_input == '+':
        quantity = int(input('Какое колличество наименований Вы хотите внести?: '))

        for product in range(quantity):
            count += 1
            print(f'------------- Заполнение карты товара №{count} -------------')
            name = input('Введите наименование: ')
            price = input('Введите цену: ')
            count_product = input('Введите колличество: ')
            units = input('Введите название учетных единиц: ')

            a = (count, {'название': name, 'цена': price, 'количество': count_product, 'eд': units})
            product_list.append(a)
            print('\n------------- Товар успешно добавлен. -------------\n')
    elif user_input == 'q':
        print('Всего хорошего!')
    elif user_input == 'm':
        print('\n------------- Меню -------------')
        print('Посмотреть перечень товаров - "p"')
        print('Посмотреть аналитику - "a"')
        print('Вернуться в предыдущее меню - "-"')
        print('Выйти - "q"')
        user_input2 = input('\nВведите команду: ')
        if user_input2 == 'p':
            print('\n------------- Перечень внесенных товаров: -------------')
            for i in product_list:
                print(i)
        elif user_input2 == 'a':
            for count in range(len(product_list)):

                name_list.append(product_list[count][1]['название'])
                price_list.append(product_list[count][1]['цена'])
                count_product_list.append(product_list[count][1]['количество'])
                if not product_list[count][1]['eд'] in units_list:
                    units_list.append(product_list[count][1]['eд'])
                count += 1

            analytics_dict['название'] = name_list
            analytics_dict['цена'] = price_list
            analytics_dict['количество'] = count_product_list
            analytics_dict['eд'] = units_list

            print('\n------------- Аналитика товаров: -------------')
            for i in analytics_dict:
                print(i,analytics_dict[i])
        elif user_input2 == '-':
            continue
        elif user_input2 == 'q':
            print('Всего хорошего!')
            break
        else:
            print('Такой команды несуществует!')
            continue
    else:
        print('Такой команды несуществует!')
        continue