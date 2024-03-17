# Задача 1. Напишите функцию для транспонирования матрицы

# элементы в строках меняются местами с элементами в столбцах


def transpose_matrix(matrix):
    
    rows = len(matrix) # Определяем количество строк и столбцов в исходной матрице
    cols = len(matrix[0])

    # Создаем новую матрицу для хранения транспонированной матрицы
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Транспонируем матрицу
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)


# Задача 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
    

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        key_str = str(key) if hash(key) is None else key
        result[str(value)] = key_str
    return result

print(create_dict(a=1, b='hello', c=[1, 2, 3]))


# Задача 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0 # первоначальный баланс карты 0 уе
percent_take = 0.01 # процент за снятие наличных
percent_add = 0.005 # процент за каждую третью операцию 
percent_tax = 0.02 # налог на богатство при сумме на счете более 5 млн

def add_bank(cash: float) -> None: # функция пополнения баланса и начисления процентов
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None: # снятие наличных
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("списаны проценты за cash: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны проценты за cash: ", 600)
    else:
        bank -= cash * percent_take
        print("списаны проценты за cash: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank(): # выход
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int: # пополнение баланса
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()