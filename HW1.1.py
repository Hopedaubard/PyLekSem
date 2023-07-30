"""
Задача 2: Найдите сумму цифр трехзначного числа.

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

user_num = int(input("Введите 3-х значное число: "))
if user_num < 1000 and user_num > 99:
    sum_digits = 0
    while user_num > 0:
        sum_digits += user_num % 10
        user_num = user_num//10
    print(sum_digits)
else: print('{} не трёхзначное число!' .format(user_num))
