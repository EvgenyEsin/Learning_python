# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадайте загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка № {nn}: ').lower()
        if ans in answers:
            return nn
    return 0


if __name__ == '__main__':
    result = riddle(riddle_text = 'Зимой и летом одним цветом', answers = ['ель', 'ёлка', 'елка', 'сосна'])
    print(f'Угадал с {result}-й попытки!' if result > 0 else 'Не угадал...')