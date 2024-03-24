# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Клю словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from task4_riddle import *


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка', 'сосна'],
        'Сидит дед во сто шуб одет': ['лук', 'лучек', 'луковица'],
        'Не лает, не кусает, а в дом не пускает': ['замок', 'засов', 'домофон']
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(f'Угадал с {result}-й попытки!' if result > 0 else 'Не угадал...')


if __name__ == '__main__':
    storage()