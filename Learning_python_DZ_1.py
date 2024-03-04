# Задача № 1. Треугольник существует......

# Составим список для названий сторон треугольника
name_tr = ['A', 'B', 'C']
# Составим список для хранения длины сторон треугольника
triangle = [0, 0, 0]

# Заполним список triangle c помощью цикла for
for i in range (3):
    while triangle[i] <= 0:
        triangle[i] = float(input(f'Введите длину стороны {name_tr[i]}: '))
        if triangle[i] <= 0:
            print('Ошибка!')

a = triangle[0]
b = triangle[1]
c = triangle[2]

# Проверка на существование треугольника
if a + b <= c or b + c <= a or a + c <= b:
    print('Такого треугольника не существует!')
# Проверка на равность сторон
elif a == b and b == c:
    print('Треугольник равносторонний')
elif a != b and b != c and a!= c:
    print('Треугольник разносторонний')
else:
    print('Треугольник равнобедренный')



# Задача № 2. Напиши код, который запрашивает число ........

# Введем число
n = 0
while n < 1:
    n = int(input('Введите число от 2 до 100 000: '))
    if n < 2 or n > 100000:
        print('Неверно введено число')

# Проверка на простое число
count = 0 # для количества делителей
for i in range(2, n//2+1):
    if n % i == 0:
        count += 1

if (count == 0):
    print("Число простое")
else:
    print("Число не является простым")


# Задача № 3. Программа загадывает число ......... 

from random import randint
num = randint(0, 1000)

count = 1
user_num = None
while count < 11:
    user_num = int(input('Введите число: '))
    if user_num > num:
        print('Меньше')
    elif user_num < num:
        print('Больше')
    else:
        print('Угадал!')
        break
    count += 1
print('Игра окончена')
    
