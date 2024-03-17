# Задача 1

# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

data = [1, 2, 3, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
new_data = []

for i in data:
    if data.count(i) > 1:
        new_data.append(i)

print(data, list(set(new_data)))


# Задача 2

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

text = """Вязание – это увлекательное занятие. Оно развивает в человеке усидчивость и терпение. Каждое поколение открывает для себя его привлекательность. Связанная своими руками игрушка оказывается неповторимой и более доступной по цене, чем готовое изделие. В нашем 21 веке вязание становится очень актуальным. Возможность применения разнообразных ниток и моделей сделало вязание крючком для меня любимым занятием. Вязание меня успокаивает, помогает собраться с мыслями.
Вязание крючком отличается от других видов рукоделия. Несмотря на свою компактность и простоту, оно позволяет создавать неповторимые, уникальные модели одежды, декоративные вещи и удивительные игрушки. К тому же исходный материал (пряжу) можно использовать несколько раз без особых потерь. Проявив фантазию в работе с нитками разных фактур и цветов можно выразить свою индивидуальность, уйти от традиционных взглядов на моду, как в домашнем интерьере, так и в изготовлении игрушек.
А главное, эта работа способствует развитию творческого начала, которое поможет в будущем стать хорошей хозяйкой. Рационально использовать материалы, создавать красивые вещи, для семьи и квартиры своими руками.
Не секрет, что даже взрослые любят игрушки. Они позволяют пусть и на короткое время вернуться в мир, где нет тревог и забот, где все просто и интересно, в мир своего детства. Может, поэтому многих захватывает изготовление игрушек. Кто-то мастерит их из кожи и дерева, кто-то – из лоскутков ткани, отливает фарфоровые или гипсовые лица кукол, лепит из глины крошечные ручки и ножки, а кто-то берет в руки спицы или крючок и начинает вязать. Порой из рук мастерицы выходит не совсем аккуратный персонаж, не то, что хотелось бы, но все равно эта игрушка для ребенка становится наиболее любимой.
Для кого-то вязание игрушек становится настоящим увлечением, а процесс их создания увлекает и завораживает. Сначала связаны голова и туловище, а затем одна за другой появляются ручка или лапка. Многим нравится вязать кукол, а лица каждый раз получаются другими, несмотря на то, что вяжутся они по одной и той же схеме. Каждая связанная вами игрушка будет иметь свой характер и свою историю создания, а затем – и историю жизни.
Я выбрала эту тему, потому что я создаю руками вещи для своего дома. Вязать - это непередаваемое ощущение; дарить подарки, сделанные своими руками - тоже. Мне нравится, что можно вязать вместе с друзьями. Именно крючком можно создать вещи, которые нельзя повторить в производстве и на машинах.
"""

symbol = "1234567890.,!?;:-–[]{}()=\n"
for i in symbol:
    text = text.replace(i, "") # заменяем все символы на пробелы
text = text.lower().split() # переводим текст в нижний регистр и создаем список из отдельных слов

for i in text:
    if len(i) <= 3: # мы хотим иметь дело только со словами длиной более 3 букв.
        text.pop(text.index(i))

word_counts = {} # Создаем пустой словарь для подсчета частоты встречаемости слов
for word in text:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True) # Сортируем слова по частоте встречаемости
most_common_words = sorted_word_counts[:10] # Получаем 10 самых часто встречающихся слов

print(f'Количество слов в тексте: {len(text)}')
print(f'Самые частые слова: {most_common_words}')


# Задача 3

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.


def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}
max_weight = int(input('Введите максимальную грузоподъемность в граммах: '))
print(pack_backpack(items, max_weight)) 

