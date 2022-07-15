# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ["banana", "apple", "pineapple", "melon", "watermelon"]

max_fruit_value = 0
for fruit in fruits:
    if len(fruit) > max_fruit_value:
        max_fruit_value = len(fruit)

fruit_output_template = ":>{}".format(max_fruit_value)
fruit_output_template = "{:>3}. {" + fruit_output_template + "}"  # Красиво до 999 фруктов

for fruit in fruits:
    print(fruit_output_template.format(fruits.index(fruit) + 1, fruit))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

scientists = ["Alex", "Bob", "Mike", "John", "Tom", "Jim", "Amber", "Jim", "Jim", "Jim"]
chemists = ["Amber", "Mike", "Rob", "Jim"]

for name in chemists:
    if name in scientists:
        while scientists.count(name) != 0:
            scientists.remove(name)

print(scientists)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

my_list = [2, 23, 4, 54, 6, 786, 45, 32, 12, 11, 73]
new_list = []

for i in my_list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print(new_list)

# new_list = [x / 4 if x % 2 == 0 else x * 2 for x in my_list]
# print(new_list)
