# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
#
# 300
# 220 284

def task():
    number = int(input('Введите число: '))
    list_res= []
    for i in range(1, number):
        temp = find_dividers_sum(i)
        if find_dividers_sum(temp) == i and temp != i:
            list_res.append(i)
            # print(list_res)
            print(f"{i} и {temp} – дружественные")
    print(list_res)


def find_dividers_sum(n):
    divider_sum = 0
    for i in range(1, n):
        # print(i)
        if n%i == 0:
            divider_sum += i
    return divider_sum

task()

# https://github.com/L0GIN0UT/Python_semiar_lectures/tree/main/Seminar_6_Povtorenie_spiskov


# Вариант Ивана

# while True:
#     k = int(input('Введите K -> '))
#     if k > 0 and k < 100000:
#         break


# def sumdivider(n):      # 220 - 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
#     sum = 1
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             sum += i + n//i
#     return sum
# # print(sumdivider(k))

# for i in range(1,k):
#     j = sumdivider(i)
#     if i == sumdivider(j) and i < j < k:
#         print(f'Пара дружественных чисел {i, j} в пределе {k}')