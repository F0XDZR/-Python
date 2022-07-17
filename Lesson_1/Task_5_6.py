revenue = int(input('Введите сумму выручки руб.: '))
cost = int(input('Введите сумму издержки руб.: '))

if revenue > cost:
    print('Все идет хорошо! Выручка больше издержек. Так держать, бизнес в прибыли!')
    profit = revenue - cost
    profitability = profit / revenue
    print(f'Рентабельность бизнеса составила - {100 * profitability:.1f}%.')
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / number_of_employees
    print(f'Прибыль на одного сотрудника составила - {profit_per_employee:.2f} руб.')
else:
    print('Нужно поэкономить. Издержки больше выручки. Бизнес работает в убыток.')