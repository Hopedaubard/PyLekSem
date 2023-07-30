# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, 
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

n = 2
def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

list_1 = []
for i in range (1, n + 1):
    list_1.append(fibonacci(i))
print(list_1)

print(fibonacci(n))

