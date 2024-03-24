# ДЗ. Задача 1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from sys import argv
from task7_module_check_date import *


if __name__ == '__main__':
    year = argv[1:]
    print(check_date(year))


# Запуск в терминале осуществляется с помощью команды: python DZ_6_check_date_in_terminal.py '28.02.2024'
# Ответ: True

# Модуль <module_check_date> сздан в отдельном файле, привожу код оттуда:

# def _is_not_leap(year: int) -> bool:
#     return not(year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


# def check_date(full_date:str) -> bool:
#     day, month, yaer = (int(item) for item in full_date.split('.'))
#     if yaer < 1 or yaer > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
#         return False
#     if month in (4, 6, 9, 11) and day > 30:
#         return False
#     elif month == 2 and day > 28 and _is_not_leap(yaer):
#         return False
#     else:
#         return True
    

# if __name__ == '__main__':
#     print(check_date('29.02.2024'))