# Задача 1

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#  Функцию hex используйте для проверки своего результата.

HEX = 16
result: str = ''
num = int(input('Введите целое число: '))
print(hex(num))

while num > 0:
    hex_number = num % HEX if (num % HEX) < 10 else chr(num % HEX + 87)
    result = str(hex_number) + result
    num //= HEX

print('0x: ' + result)


# Задача 2.

# Напишите программу, которая принимает две строкивида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(num, den):
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def add_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    new_num = num1 * den2 + num2 * den1
    new_den = den1 * den2

    return simplify_fraction(new_num, new_den)

def multiply_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    new_num = num1 * num2
    new_den = den1 * den2

    return simplify_fraction(new_num, new_den)

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result = add_fractions(fraction1, fraction2)
product_result = multiply_fractions(fraction1, fraction2)

print(f"Сумма дробей: {sum_result[0]}/{sum_result[1]}")
print(f"Произведение дробей: {product_result[0]}/{product_result[1]}")


# проверка с помощью функции fractions
from fractions import Fraction

def sum_and_product_of_fractions(fraction1, fraction2):
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)

    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2

    return sum_frac, product_frac

sum_result, product_result = sum_and_product_of_fractions(fraction1, fraction2)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")
