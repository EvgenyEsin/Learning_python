# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищенный словарь уровня модуля.
# Отдельно напишите фуекцию, которая выводит результаты угадывания из защищенного словаря в удобном для чтония виде.
# Для формирования результатов используйте генераторное выражение.

__all__ = ['riddle', 'storage']

_data = {}


def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадайте загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка № {nn}: ').lower()
        if ans in answers:
            return nn
    return 0


def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn


def show_results():
    res = (f'Загадку "{puzzle}" разгадали с {nn}-й попытки' if nn > 0
           else f'Загадку "{puzzle}" не разгадали'
           for puzzle, nn in _data.items())
    print(*res, sep='\n')


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка', 'сосна'],
        'Сидит дед во сто шуб одет': ['лук', 'лучек', 'луковица'],
        'Не лает, не кусает, а в дом не пускает': ['замок', 'засов', 'домофон']
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(f'Угадал с {result}-й попытки!' if result > 0 else 'Не угадал...')
        save_results(puzzle, result)


if __name__ == '__main__':
    storage()
    show_results()