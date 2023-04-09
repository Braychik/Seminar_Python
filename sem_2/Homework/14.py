# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))

k = 1
result = str(1)
count = 0
while count < n:
    count = 2 ** k
    if count < n:
        result = result + str(f" - {count}")
    k += 1
print(result)
