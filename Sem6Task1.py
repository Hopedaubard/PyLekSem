# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# m = int(input('Введите длину списка m: '))
# n = int(input('Введите длину списка n: '))
# list_m = list_creator(m)
# list_n = list_creator(n)
# res_list = se

# def set_from_list (list_n, list_m):
#     my_list = []
#     for i in range(0, x):
#         for i not in range(list_m):
#             my_list.add(list_n[i])
#     return my_list


# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(imput(f'Введите элемент списка из {x} элементов: ')))
#     return my_list

def task029():
    m = int(input("Введите длину списка m: "))
    n = int(input("Введите длину списка n: "))
    list_m = list_creator(m)
    list_n =list_creator(n)
    res_list = set_from_list(list_m, list_n)
    print(*res_list)

def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
    return my_list

def set_from_list(list_m, list_n):
    my_list = [list_m[i] for i in range(len(list_m)) if list_m[i] not in list_n]
    return my_list

task029()


# Вариант Ивана
# n = int(input('Введите кол-во элементов множества -> '))
# arr = [input('Введите элемент массива -> ') for i in range(0, n)]
# res = [1 for i in range(0,len(arr)) if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]]
# print(sum(res))