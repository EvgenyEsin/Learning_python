# Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.


__all__ = ['generate_file']

from Task4_ import create_file


def generate_file(**kwrgs) -> None:
    for extension, amount in kwrgs.items():
        create_file(extension, count=amount)


if __name__ == '__main__':
    generate_file(bin=2, jpg=1, txt=3)