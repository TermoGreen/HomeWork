"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def discount(score):
    if 0 < score < 50:
        scores = '10%'
        print('ваша скидка:' + scores)
    elif 50 <= score < 100:
        scores = '15%'
        print('ваша скидка:' + scores)
    elif score >= 100:
        scores = '20%'
        print('ваша скидка:' + scores)


discount(int(input('введите количество баллов: ')))