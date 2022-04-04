# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле
# Вариант 5
import re

q = open('ip_address.txt', 'r', encoding='utf-8').read().split('\n')
f = open('first.txt', 'w', encoding='utf-8')
s = open('second.txt', 'w', encoding='utf-8')

w = r'\d{,3}.\d{,3}.\d{,3}.0'
st = False
for i in q:  # ищем нужный раздел, распределяем ip, при окончании раздела выходим
    if i == 'Частоупотребимые маски':
        q.remove(i)
        st = True
    elif st and re.fullmatch(r'\d{,3}.\d{,3}.\d{,3}.\d{,3}', i):
        if re.fullmatch(w, i):
            f.write(i + '\n')
        else:
            s.write(i + '\n')
    elif st:
        break

f.close()
s.close()
