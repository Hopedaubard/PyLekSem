# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

a = int(input("Введите число: "))
if a < 0:
    print("Число не удовлетворяет условию задачи!")
elif a > 1:
    count = 0
    num = 1
    a1 = 1
    a2 = 1
    while (num < a):
        num = a1 + a2
        a1 = a2
        a2 = num 
        count += 1
    if (num == a):
        print("Порядковый номер данного числа в последовательности Фиббоначи")
        print (count)
    
else: print(-1)
