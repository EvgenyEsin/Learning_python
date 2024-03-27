# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.


__all__ = ['random_names']

from random import choice, randint
from pathlib import Path

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
MIN_LEN = 4
MAX_LEN = 7


def random_names(filename: str | Path, count: int) -> None:
    with open(filename, 'a', encoding="utf-8") as f:
        for _ in range(count):
            name = ''
            cur_vowel = choice([-1,1])
            for _ in range(randint(MIN_LEN, MAX_LEN)):
                if cur_vowel < 0:
                    name += choice(VOWELS)
                else:
                    name += choice(CONSONANTS)
                cur_vowel *= -1
            print(name.title(), file=f)


if __name__ == '__main__':
    random_names(Path('names.txt'), count=128)
        
