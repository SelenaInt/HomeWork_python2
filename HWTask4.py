# Задача №17: Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

# 1
# import random
# def write_file(number):
#     with open('file.txt', 'w') as data:
#         for i in range(number):
#             data.write(f"{random.randrange(0, 2*number)}\n")


# def read_file():
#     with open('file.txt', 'r') as data:
#         indexs = list(map(int,data.readlines()))
#     return indexs


# n = int(input("Введите число N: "))
# lst_number = [i for i in range(-n, n+1)]
# write_file(n)
# lst_index = read_file()
# prod= 1
# for i in range(len(lst_index)):
#     prod *= lst_number[lst_index[i]]
# print(f"Результат равен = {prod}")

# 2
# n = int(input('Введите N: '))
# a = []
# for i in range(-n, n+1):
#     a.append(i)
# print(a, sep=',')

# l = []
# with open('file.txt', 'r') as f:
#     for line in f:
#         l.append(int(line))

# c = l[0]
# d = l[1]
# k = a[c]*a[d]
# print('Произведение элементов на указанных в файле позициях = ', k)

# 3
from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)