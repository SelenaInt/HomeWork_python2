# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num // 10: целочисленное деление, то есть деление без остатка, иначе цифра не отбросится,
# а уйдет в дробную часть результата

num = int(input("Введите любое целое число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10  
print("Сумма цифр числа равна = ", sum)