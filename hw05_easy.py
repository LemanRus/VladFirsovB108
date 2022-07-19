import random

# Все задачи текущего блока решите с помощью генераторов списков!


# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


random_list = [random.randint(0, 100) for _ in range(0, 20)]
new_list = [x**2 for x in random_list]

print("Исходный список:", random_list)
print("Элементы в квадрате:", new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


fruit_list1 = ["Banana", "Apple", "Grapefruit", "Grapes", "Orange", "Strawberry"]
fruit_list2 = ["Apple", "Grapes", "Melon", "Watermelon", "Banana"]

fruits = [fruit for fruit in fruit_list1 if fruit in fruit_list2]

print(fruits)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


random_list_for_task_3 = [random.randint(-100, 100) for _ in range(0, 20)]
new_list_for_task_3 = [x for x in random_list if x % 3 == 0 and x >= 0 and x % 4 != 0]

print("Исходный список:", random_list_for_task_3)
print("Новый список:", new_list_for_task_3)
