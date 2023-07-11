name = input()
price = int(input())
weight = int(input())
amount = int(input())
total = price * weight
change = amount - total
print('================Чек================')
print('Товар:', name.rjust(34 - len('Товар:'), ' '))
print('Цена:', f"{weight}кг * {price}руб/кг".rjust(34 - len('Цена:'), ' '))
print('Итого:', f"{total}руб".rjust(34 - len('Итого:'), ' '))
print('Внесено:', f"{amount}руб".rjust(34 - len('Внесено:'), ' '))
print('Сдача:', f"{change}руб".rjust(34 - len('Сдача:'), ' '))
print('===================================')
