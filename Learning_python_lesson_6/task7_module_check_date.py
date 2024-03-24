# Задача 7. 
# Создайте модуль и напишите в нем функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая лата невозможна.
# Проверку года на високосность вынести в отдельную защищенную функцию

__all__ = ['check_date']

def _is_not_leap(year: int) -> bool:
    return not(year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def check_date(full_date:str) -> bool:
    day, month, yaer = (int(item) for item in full_date.split('.'))
    if yaer < 1 or yaer > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 28 and _is_not_leap(yaer):
        return False
    else:
        return True
    

if __name__ == '__main__':
    print(check_date('29.02.2024'))