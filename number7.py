# Есть словарь кодов товаров

import random

goods = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

#  Есть словарь списков словарей количества товаров на складе.

store = {
    '100000110': [
        {'quantity': 31, 'price': 1637}
        ],
    '100000146': [
        {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}
        ],
    '100000149': [
        {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}
        ],
    '100000194': [
        {'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}
        ],
    '100000224': [
        {'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}
        ],
    '100000280': [
        {'quantity': 26, 'price': 175},
        ]
}

# Рассчитать на какую сумму лежит каждого товара на складе.

user_input = input('Введите искомый товар: ')
search_result = goods[user_input]

quantity = 0
for dict in store[search_result]:
    quantity += (dict['quantity'])

price = 0
for dict in store[search_result]:
    price += (dict['price'])

# quantity = store[search_result][0]['quantity']
# print(quantity)
print(f'{user_input} - {quantity} шт, стоимость - {price} руб')