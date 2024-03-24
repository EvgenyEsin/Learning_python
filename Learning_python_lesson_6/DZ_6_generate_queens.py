# ДЗ Задача № 3. 
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import random
from DZ_6_chess_module import *


def generate_queens():
    queens_gen = []
    for _ in range(8): # создаем список из случайных координат 8 ферзей. Лучше указать 7 ферзей. 8 ферзей программа долго ищет.
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        queens_gen.append((x, y))
    return queens_gen


if __name__ == '__main__':
    placement = 0 # счетчик для вывода 4 успешных расстановок
    while placement < 4:
        queens_gen = generate_queens()
        if check_queens(queens_gen):
            print(f'Successful placement: {queens_gen}')
            placement +=1