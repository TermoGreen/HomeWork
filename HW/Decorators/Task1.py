"""
Напишите декоратор печатающий время выполнения функции
"""

import time
def obertka(lol):
    def wrapper():
        a = time.time()
        lol()
        b = time.time()
        c = b-a
        print(c)
    return wrapper

@obertka
def func_to_decor():
   for i in range(1000):
      print(i)




func_to_decor()
