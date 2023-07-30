# Ищем сумму от 1 до N

# def sum_numbers(n):
#     summa = 0
#     for i in range (1, n + 1):
#         summa += i
#     return(summa)
# # print('stop') – не работает
 
# print(sum_numbers(5))
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range (1, n + 1):
#         summa += i
#     return(summa)
# # print('stop') – не работает
 
# print(sum_numbers(5, 'qwert'))
# a = sum_numbers(5)
# print(a)

def sum_str(*args): # * – передать неограниченное кол-во аргументов
    res = ' '
    for i in args:
        res += i
    return res

print(sum_str('q','w','e','r'))
print(sum_str('5','4','3','2'))