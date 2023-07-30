# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def func(n):


    if n == 0:
        return " "
    num = input('Введите элемент: ')
    return func(n-1) + f' ' + num

print(func(5))

# def Reverse(num):
#     if num == 0:
#         return ""
#     number = input("Введите число: ")
#     return f"{Reverse(num-1)}{number} " #пробел в конце, потому что идём в обратную сторону
    

# n = int(input("Введите число N элементов: "))
# print(Reverse(n))

# https://github.com/L0GIN0UT/Python_semiar_lectures/tree/main/%D0%A1%D0%B5%D0%BC%D0%B8%D0%BD%D0%B0%D1%80%205.%20%D0%A0%D0%B5%D0%BA%D1%83%D1%80%D1%81%D0%B8%D1%8F%20%D0%B8%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B