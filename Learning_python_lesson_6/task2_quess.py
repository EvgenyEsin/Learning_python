# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угодоть его за заданное число попыток.
# Функция выводит подсказки "больше" и "меньше".
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

__all__ = ['quess']

from random import randint


def quess(lower: int=0, upper: int=100, count: int=10) -> bool:
    number = randint(lower, upper)
    for nn in range(1, count + 1):
        answer = int(input(f'Попытка № {nn}, введите число между {lower} и {upper}: '))
        if answer > number:
            print(f'Число {answer} больше загаданного.')
        elif answer < number:
            print(f'Число {answer} меньше загаданного.')
        else:
            return True
    return False

if __name__ == '__main__':
    print(quess())