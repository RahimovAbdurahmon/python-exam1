# Вопрос 1
# RU: Какие основные типы контейнеров есть в Python и чем они отличаются?
# EN: What are the main types of containers in Python and how do they differ?
# TJ: Дар Python кадом намудҳои асосии контейнерҳо ҳастанд ва онҳо чӣ фарқ доранд?
# Container ho dar python in list, set(sokhtani list dar asosi set), tuple, dictionary meshavad



# Вопрос 2
# RU: Чем отличается список (list) от множества (set) в Python?
# EN: What is the difference between a list and a set in Python?
# TJ: Фарқи байни list ва set дар Python чист?
# Mo list-ro bo scope-hoi array mesozem va set ro bo dict mesozem va dar set elementho duclic omada nametavonand(iane takror nameoiand)


# Вопрос 3
# RU: Можно ли изменить кортеж (tuple) после создания? Почему?
# EN: Can a tuple be changed after creation? Why or why not?
# TJ: Оё пас аз эҷод кардани tuple онро метавон тағйир дод? Чаро?
# Ne nametavonem


# Вопрос 4
# RU: Что означает, что тип данных является изменяемым (mutable) или неизменяемым (immutable) в Python?
# EN: What does it mean for a data type to be mutable or immutable in Python?
# TJ: Дар Python маънои тағйирёбанда (mutable) ё тағйирнопазир (immutable) будани намуди маълумот чист?
# mutable in tagir meiobad ba misoli dict, list, set va immutalbe bad az sokhtan tagir nameiobad


# Вопрос 5
# RU: Что такое словарь (dict) в Python и чем он отличается от списка?
# EN: What is a dictionary (dict) in Python and how does it differ from a list?
# TJ: Словарь (dict) дар Python чист ва он аз рӯйхат чӣ фарқ дорад?
# mo dar dict(dictionary) set mesozem ammo dar dict mo property(key and value) mesozem ki har iak element kluch va qimmat dorad mo bo kluch metavonem qimmathora jeg zanem


# TASKS

# 1
# RU: Дана строка. Подсчитайте, сколько раз в ней встречается буква 'а' (регистр не важен).
# EN: Given a string. Count how many times the letter 'a' appears (case insensitive).
# TJ: Як сатр дода шудааст. Шумораи ҳар бор пайдо шудани ҳарфи 'а'-ро ҳисоб кунед (ба калонӣ ва хурдии ҳарф аҳамият надорад).
# Input:
# Abracadabra
# Output:
# 5
# str = "Abracadabra"
# print(str.lower().count("a"))



# 2
# RU: Дан список чисел. Выведите список без повторяющихся элементов, сохраняя порядок.
# EN: Given a list of numbers. Print the list without duplicates, keeping the original order.
# TJ: Як рӯйхати адад дода шудааст. Рӯйхатро бе такрорҳои такрорӣ боқӣ гузоред, тартиби аслӣ ҳифз карда шавад.

# Input:
# [1, 2, 2, 3, 4, 3, 5]
# Output:
# [1, 2, 3, 4, 5]

# lst = [1, 2, 2, 3, 4, 3, 5]
# res = set(lst)
# print(list(res))



# 3
# RU: Дан кортеж чисел. Найдите сумму всех нечётных чисел.
# EN: Given a tuple of numbers. Find the sum of all odd numbers.
# TJ: Як tuple аз адад дода шудааст. Ҷамъи ҳамаи ададҳои тақро ёбед.

# Input:
# (1, 2, 3, 4, 5)
# Output:
# 9

# tuple = (1, 2, 3, 4, 5)
# cnt = 0
# for i in tuple:
#     if i % 2 != 0:
#         cnt+=i
# print(cnt)



# 4
# RU: Дан словарь: ключ — имя студента, значение — список оценок. Выведите имя студента с максимальной средней оценкой.
# EN: Given a dictionary where key is student's name and value is a list of grades. Print the name of the student with the highest average grade.
# TJ: Як dictionary дода шудааст, ки калид номи донишҷӯ ва арзиш рӯйхати имтиҳонҳояш аст. Номи донишҷӯро бо балли миёнаи баландтарин чоп кунед.

# Input:
# {'Alice': [5, 4, 5], 'Bob': [3, 4, 4], 'Charlie': [5, 5, 5]}
# Output:
# Charlie

# dict = {'Alice': [5, 4, 5], 'Bob': [3, 4, 4], 'Charlie': [5, 5, 5]}
# find_name = ""
# max = -999999
# for i in dict.keys():
#     sum = 0
#     # print(i)
#     for j in dict[i]:
#         sum+=j
#     sum = sum // len(dict[i])
#     if sum > max:
#         max = sum
#         find_name = i
# print(find_name)



# 5
# RU: Дан список строк. Создайте новый список, где каждая строка написана задом наперёд.
# EN: Given a list of strings. Create a new list where each string is reversed.
# TJ: Як рӯйхати сатрҳо дода шудааст. Рӯйхати нав эҷод кунед, ки ҳар як сатр баръакс навишта шудааст.

# Input:
# ['abc', 'hello', 'world']
# Output:
# ['cba', 'olleh', 'dlrow']

# list = ['abc', 'hello', 'world']
# list_res = []
# for i in list:
#     list_res.append(i[::-1])
# print(list_res)



# 6
# RU: Дан текст (строка). Подсчитайте количество уникальных слов без учёта регистра.
# EN: Given a text (string). Count the number of unique words ignoring case.
# TJ: Як матн (сатр) дода шудааст. Шумораи калимаҳоро бе назардошти регистр ҳисоб кунед.

# Input:
# "Hello world hello"

# Output:
# 3

# str = "Hello world hello"
# print(len(str.split()))

# 7 
# RU: Дан список чисел и число k. Найдите все пары чисел, сумма которых равна k.
# EN: Given a list of numbers and a number k. Find all pairs of numbers whose sum equals k.
# TJ: Як рӯйхати адад ва адади k дода шудааст. Ҳама ҷуфт ададҳоро ёбед, ки ҷамъашон баробар ба k бошад.

# Input:
# [1, 2, 3, 4, 5], k = 5
# Output:
# [(1, 4), (2, 3)]

list = [1, 2, 3, 4, 5]
k = 5
list_res = []
cnt = 0
list_sum = []
for i in list:
    cnt+=i
    list_sum.append(cnt)
    print(cnt)
    if(cnt == k):
        list_res.append(tuple(list_sum))
        cnt = 0
        list_sum = []
print(list_res)



# 8
# RU: Дан словарь с товарами и количеством продаж. Выведите топ-3 товара с наибольшими продажами.
# EN: Given a dictionary with products and sales counts. Print the top 3 products by sales.
# TJ: Як dictionary бо маҳсулотҳо ва миқдори фурӯш дода шудааст. Се маҳсулоти пешсафро бо бештар фурӯш нишон диҳед.

# Input:
# {'apple': 50, 'banana': 30, 'orange': 40, 'pear': 20}
# Output: 
# ['apple', 'orange', 'banana']

# dict = {'apple': 50, 'banana': 30, 'orange': 40, 'pear': 20, "grapes": 60, "kivi": 10}
# values = []
# for i in dict.values():
#     values.append(i)
# reversed_dict = {}
# for i in dict.keys():
#     reversed_dict[dict[i]] = i
# reversed_dict
# values.sort()
# values = values[:-4:-1]
# result = []
# for i in values:
#     result.append(reversed_dict[i])
# print(result)



# 9
# RU: Дан текст с цифрами. Извлеките все числа и выведите их сумму.
# EN: Given a text containing numbers. Extract all numbers and print their sum.
# TJ: Як матн бо рақамҳо дода шудааст. Ҳама рақамҳоро берун кашед ва ҷамъашонро чоп кунед.

# Input:
# "My numbers are 2, 7 and 3."
# Output:
# 12

# str = "My numbers are 2, 7 and 3."
# str_list = str.split(" ")
# nums = []
# cnt = 0
# for i in str_list:
#     for j in i:
#         if j.isdigit():
#             nums.append(int(j))
# for i in nums:
#     cnt+=i
# print(cnt)



# 10
# RU: Дан список кортежей с координатами точек (x, y). Найдите пару точек с минимальным расстоянием между ними.
# EN: Given a list of tuples with point coordinates (x, y). Find the pair of points with the minimum distance between them.
# TJ: Як рӯйхати tuple бо координатаҳои нуқтаҳо (x, y) дода шудааст. Ҷуфти нуқтаҳоро бо камтарин масофа ёбед.

# Input:
# [(1, 2), (4, 6), (5, 5), (2, 1)]
# Output: 
# ((1, 2), (2, 1))

# tuple = [(1, 2), (4, 6), (5, 5), (2, 1)]
# min_x = 999999
# min_y = 999999
# for i in tuple:
#     if i[0] < min_x and i[1] < min_y:
#         min_x = i[0]
#         min_y = i[1]
# res = ((min_x, min_y))
# print(res)