# Задача No43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента, равные 
# друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

def task():
    l = int(input("Введите длину списка: "))
    list_m = list_creator(l)
    print(counter_func(list_m))

def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
    return my_list

def counter_func (my_list):
    counter = 0
    # counter = [counter += 1 for i in range(len(my_list) if my)]
    for i in range(len(my_list)):
        for j in range (i+1, len(my_list)):
            if my_list[i] == my_list[j]:
                counter += 1
    return counter

task()