# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

n = int(input('Enter your num: '))

if n > 0:

    if (n == 0) or (n == 1) :
        print("Факториал равен 1")

    else:
        count = 2
        fact = 1
        while count <= n:
            fact *= count
            count += 1
        print("Факториал числа равен: {}" .format(fact))
        
else: print("Число не положительное")
