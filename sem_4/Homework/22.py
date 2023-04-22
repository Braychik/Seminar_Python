# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

n = int(input())
m = int(input())

random_n = []
random_m = []

for i in range(n):
    random_n.append(random.randint(0,9))
print(random_n)

for i in range(m):
    random_m.append(random.randint(0,9))
print(random_m)

result = set(random_n).intersection(random_m)
print(sorted(result))