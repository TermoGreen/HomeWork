"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""
def bages(number):
    for i in range(0, num):
        name = input('введите имя: ')
        group = input('укажите группу: ')
        print('Колледж Сириус')
        print('имя: ', name)
        print('группа: ', group)
    print()
    print('Готово! Заберите бейджики.')


num = int(input('введите количество студентов'))
bages(num)