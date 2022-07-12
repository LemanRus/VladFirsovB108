# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ["banana", "apple", "pineapple", "melon", "watermelon"]

for fruit in fruits:
    print("{:>3}. {:>12}".format(fruits.index(fruit) + 1, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

scientists = ["Alex", "Bob", "Mike", "John", "Tom", "Jim"]
chemists = ["Amber", "Mike", "Rob", "Jim"]

for name in scientists:
    if name in chemists:
        scientists.remove(name)

print(scientists)