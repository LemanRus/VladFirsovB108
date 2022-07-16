# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
from functools import reduce


def fibonacci(n, m):
    fib_row = ["1", "1"]
    fib1 = fib2 = 1

    for i in range(2, m):
        fib1, fib2 = fib2, fib1 + fib2
        fib_row.append(str(fib2))
    return ", ".join(fib_row[n-1:m])


print(fibonacci(5, 6))
print(fibonacci(1, 1))
print(fibonacci(1, 2))
print(fibonacci(1, 3))
print(fibonacci(3, 5))
print(fibonacci(10, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):  # Суперклассика) Пузырёк не интересно, на быструю сортировку меня не хватит, пусть будет сортировка выбором)
    for pos in range(len(origin_list)):
        min_num_pos = pos
        for rest_pos in range(pos + 1, len(origin_list)):
            if origin_list[rest_pos] < origin_list[min_num_pos]:
                min_num_pos = rest_pos
        origin_list[pos], origin_list[min_num_pos] = origin_list[min_num_pos], origin_list[pos]


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(origin_list)
print(origin_list)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def is_even(num):  # Для проверки
    if num % 2 == 0:
        return True
    else:
        return False

def my_filter(func, list_to_filter):  # Обойдёмся без генераторов и вернём список
    my_list = []
    for item in list_to_filter:
        if func(item):
            my_list.append(item)
    return my_list


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
filtered = my_filter(is_even, seq)
filtered2 = my_filter(lambda x: x in (3, 4, 5), seq)  # Вроде всё работает) Может, есть какой непредусмотренный случай
filtered3 = my_filter(lambda x: str(x).isdigit(), seq)
print(filtered, filtered2, filtered3, sep="\n")


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a1, a2, a3, a4):  # Принимаем кортежи с 2 координатами
    point1 = complex(a1[0], a1[1])  # Складывает-вычитает пусть сам, и модуль тоже находит
    point2 = complex(a2[0], a2[1])  # Т.к. на комплексной плоскости числа - те же самые точки и вектора
    point3 = complex(a3[0], a3[1])
    point4 = complex(a4[0], a4[1])

    prob_vec_1_2 = point1 - point2  # Точки в любом случае липо по кругу, либа слева направо (справа налево) по очереди
    prob_vec_3_4 = point3 - point4  # И направление вектора неважно
    prob_vec_1_3 = point1 - point3
    prob_vec_2_4 = point2 - point4

    prob_vec_2_3 = point2 - point3  # Для случая расположения точек по кругу
    prob_vec_1_4 = point1 - point4

    vecs = [prob_vec_1_4, prob_vec_2_3, prob_vec_2_4, prob_vec_1_2, prob_vec_1_3, prob_vec_3_4]

    """Даже если мы не угадали, как расположены на плоскости точки, мы либо докажем, что 4 противоположные стороны 
    попарно равны, что доказывает, что дан параллелограмм, либо 2 противоположные стороны равны и равны диагонали, 
    что даёт квадрат, который тоже параллелограмм"""
    # if 0 in list(map(abs, vecs)):  # Защита от вырожденных случаев
    #     return False
    # elif:
    if abs(prob_vec_1_2) == abs(prob_vec_3_4) and abs(prob_vec_2_4) == abs(prob_vec_1_3):
        return True
    elif abs(prob_vec_1_2) == abs(prob_vec_3_4) and abs(prob_vec_2_3) == abs(prob_vec_1_4):
        return True
    else:
        return False


print(is_parallelogram((0, 0), (5, 3), (5, 0), (0, 3)))
print(is_parallelogram((0, 0), (5, 3), (5, 0), (0, -3)))
print(is_parallelogram((0, 0), (5, 3), (-5, 0), (0, -3)))
print(is_parallelogram((0, 0), (5, 3), (5, 0), (0, 2)))
print(is_parallelogram((0, 0), (0, 0), (0, 0), (0, 0)))  # Вырожденный параллелограмм со сторонами бесконечно малой длины)
print(is_parallelogram((1, 1), (1, 1), (2, 2), (2, 2)))  # Условие задачи не уточняет, куда это относить