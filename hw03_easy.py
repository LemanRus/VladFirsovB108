# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ["banana", "apple", "pineapple", "melon", "watermelon"]

for fruit in fruits:
    print("{:>3}. {:>12}".format(fruits.index(fruit) + 1, fruit))
