# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

my_list = [12, 25, 144, 11, 17, -5, -893, 14, 81, 0]
roots = []

for i in my_list:
    if i >= 0:
        if not i**0.5 % 1:
            roots.append(int(i**0.5))

print(roots)