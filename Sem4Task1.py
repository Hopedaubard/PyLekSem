"""
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

.split
"""

string = input('Введите элементы списка через пробел -> ').split()
dict = {}
result = ''
for i in string:
    if i in dict:
        dict[i] += 0
        result += str(i) + '_' + str(dict[i]) + ' '
    else:
        dict[i] = 1
        result += str(i) + ' '
print (result)

"""

string = input('Введите элементы списка через пробел -> ').split()

dict = {}
result = ''
for i in string:
    if i in dict:
        dict[i] += 1
        result += str(i) + '_' + str(dict[i]) + ' '
    else:
        dict[i] = 0
        result += str(i) + ' '
print(result)
"""
"""
string = input('Введите элементы списка через пробел -> ').split()

dict = {}
result = ''
for i in string:
    if i not in dict:
        dict[i] = 0
        result += str(i) + ' '
    else:
        dict[i] += 1
        result += str(i) + '_' + str(dict[i]) + ' '
print(dict)
print(result)

"""