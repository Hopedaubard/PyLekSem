# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, у которых два соседних 
# и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество 
# элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# def task24():
#     list_new = [1, 100, 6, 2, 54, 1, 7, 23]
#     print(f' ')

# def find_between_less_elements(my_list):
#     count = 0
#     for i in range(1,len(my_list)-1):
#         if my_list[i-1] < my_list[i] > my_list[i+1]:
#             count += 1
#     return count

def task30():
    list_new = [200, 100, 6, 2, 54, 1, 5, 1]
    print(find_between_less_elements(list_new))

def find_between_less_elements(my_list):
    count = 0
    for i in range(1,len(my_list)-1):
        if my_list[i-1] < my_list[i] > my_list[i+1]:
            count += 1
    return count

task30()       