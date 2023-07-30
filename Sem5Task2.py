# Хакер Василий получил доступ к классному журналу и хочет 
# заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.


# 1 2 3 4 5 5 5 5
# 1 2 3 4 1 1 1 1

list1 = [1, 2, 3, 4, 5, 5, 5, 5]

def min_max (my_list):
    min = max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)


print(min_max(list1))

min, max = min_max (list1)

def change_min_max(my_list, min, max):
    for i in range(len(my_list)):
        if my_list[i]==max:
            my_list[i]=min
    return my_list

print (change_min_max(list1, min, max))

# my_list = [1, 2, 3, 4, 5, 5, 5, 5]

# def min_max(my_list):
#     min = max = my_list[0]
#     for i in my_list:
#         if i>max:
#             max=i
#         if i<min:
#             min = i
#     return (min, max)

# # min, max = min_max(my_list)

# def change_min_max(my_list, temp):
#     for i in range(len(my_list)):
#         if my_list[i]==temp[1]:
#             my_list[i]=temp[0]
#     return my_list

# print (change_min_max(my_list, min_max(my_list)))