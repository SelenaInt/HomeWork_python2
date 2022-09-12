# Реализуйте алгоритм перемешивания списка.

# 1
# import random
# def mix_list(list_original):
#     # Создаем копию, поскольку мы не должны изменять оригинал
#     list = list_original[:]
#     # Цикл от 0 до длины списка -1
#     list_length = len(list)
#     for i in range(list_length):
#         # Получение случайного индекса
#         index_aleatory = random.randint (0, list_length - 1)
#         # Замена
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     # Возвращаем список
#     return list

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)

# 2
# from random import shuffle
# some_list = ['a', 'b', 'c', 'd', 'f']
# shuffle(some_list)
# print(some_list)

# 3
# import random
# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)

# 4
# 3
import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i] 
print(list)
