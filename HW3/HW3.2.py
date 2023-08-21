# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


list_1 = [10, 2, 3, 5, 4]
num_main = 7    # int(input())

differ_module = abs(num_main - list_1[0])
num_found = list_1[0]
for i in range(1, len(list_1)):
    if differ_module > abs(list_1[i] - num_main):
        differ_module = abs(list_1[i] - num_main)
        num_found = list_1[i]
print(num_found)