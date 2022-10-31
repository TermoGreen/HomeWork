# coding=windows-1251

x = input("Введите имя гения (off для завершения)")
if x != "off":
    lol = lambda x: x+ " гений"
    print(lol(x))

else:
    print("Завершено")