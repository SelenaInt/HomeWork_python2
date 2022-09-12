# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num // 10: целочисленное деление, то есть деление без остатка, иначе цифра не отбросится,
# а уйдет в дробную часть результата




# 1
# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2
# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

# 3
# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# 4
s = '0.56'
summ = 0
for i in s:
    if i.isdigit():
        summ += int(i)
print(summ)