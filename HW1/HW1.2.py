"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""

s = int(input("Введите общее количество бумажных журавликов: "))

petya_quant = 0
sereja_quant = 0
katya_quant = 0
while (petya_quant + sereja_quant + katya_quant) < s:
    petya_quant += 1
    sereja_quant += 1
    katya_quant = (petya_quant + sereja_quant) * 2 
print(katya_quant, petya_quant, sereja_quant)
