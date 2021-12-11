# Вариант 5.
# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# можно приобрести книги Пушкина и Тютчева

dct = {'Магистр': ('Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'),
       'ДомКниги': ('Толстой', 'Грибоедов', 'Чехов', 'Пушкин'), 'БукМаркет': ('Пушкин', 'Достоевский', 'Маяковский'),
       'Галерея': ('Чехов', 'Тютчев', 'Пушкин')}  # создание словаря
for i in dct:  # проверка на нужных авторов через перебор ключей
    if 'Пушкин' in dct[i] and 'Тютчев' in dct[i]:
        print(i)