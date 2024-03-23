# Задача 1.

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(file_path):
    *parts, filename_part = file_path.split("/")
    path = "/".join(parts)
    filename, extension = filename_part.split(".")
    return path, filename, extension


file_path = "C:/Program Files/Microsoft Office/Office16/EXCEL.EXE"
result = split_path(file_path)
print(result)

# Задача 2.  

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ["Den", "Alex", "Symon", "John"]
rates = [1000, 1200, 1500, 1400]
bonuses = ["10.5%", "15%", "12.75%", "13.4%"]

result = {names: rates * float(bonuses[:-1]) / 100 for names, rates, bonuses in zip(names, rates, bonuses)}

print(result)


# Задача 3. 

# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создаем генератор чисел Фибоначчи
fibonacci = fibonacci_generator()

# Генерируем и выводим первые 10 чисел Фибоначчи
for _ in range(10):
    print(next(fibonacci))