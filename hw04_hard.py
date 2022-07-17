import os.path
import re

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

#
# expression = input("Введите выражние: ")
#
# fracs = re.split(r"\s[+-]\s", expression)  # Вычленим дроби
# action_sign = True if re.findall(r"\s[+]\s", expression) else False  # И поймём, что с ними делать
#
# frac1, frac2 = fracs
#
#
# def dissolve_frac(frac):  # Для избегания повторения кода
#     frac_int = 0 if len(frac) < 4 else int(frac.split(" ")[0])
#     frac_frac = frac if len(frac) < 4 else frac.split(" ")[1]
#     frac_frac_enumerator = int(frac_frac.split("/")[0])
#     frac_frac_denominator = int(frac_frac.split("/")[1])
#     frac_enumerator = frac_int * frac_frac_denominator + frac_frac_enumerator if frac_int >= 0 else \
#         frac_int * frac_frac_denominator - frac_frac_enumerator
#     return frac_enumerator, frac_frac_denominator  # Получаем неправильную дробь
#
#
# frac1_enumerator, frac1_denominator = dissolve_frac(frac1)
# frac2_enumerator, frac2_denominator = dissolve_frac(frac2)
#
# common_denominator = frac1_denominator * frac2_denominator  # Находим общий знаменатель самым надёжным образом
#
# frac1_enumerator_acted = frac1_enumerator * frac2_denominator  # Умножаем также и числитель
# frac2_enumerator_acted = frac2_enumerator * frac1_denominator
#
# common_enumerator = frac1_enumerator_acted + frac2_enumerator_acted if action_sign else \
#     frac1_enumerator_acted - frac2_enumerator_acted  # Производим собственно расчёт
#
# common_int = common_enumerator // common_denominator  # Выделяем целую часть
# common_frac_enumerator = common_enumerator % common_denominator  # Числитель дробной части
#
# if common_frac_enumerator != 0:  # Если дробная часть есть
#     if common_denominator % common_frac_enumerator == 0:
#         common_denominator = common_denominator // common_frac_enumerator
#         common_frac_enumerator = 1
#     elif common_denominator % frac1_denominator == 0 and common_frac_enumerator % frac1_denominator == 0:  # Некоторое упрощение
#         common_frac_enumerator = common_frac_enumerator // frac1_denominator
#         common_denominator = common_denominator // frac1_denominator
#     elif common_denominator % frac2_denominator == 0 and common_frac_enumerator % frac2_denominator == 0:
#         common_frac_enumerator = common_frac_enumerator // frac2_denominator
#         common_denominator = common_denominator // frac2_denominator
#
# if common_frac_enumerator:  # Дроби типа 6/9 выводятся в неупрощённом виде, поиск наименьшего общего делителя будет объёмным)
#     if common_int:
#         print("{} {}/{}".format(common_int, common_frac_enumerator, common_denominator))
#     else:
#         print("{}/{}".format(common_frac_enumerator, common_denominator))
# else:
#     print(str(common_int))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

path_workers = os.path.join("data", "workers")
path_hours = os.path.join("data", "hours_of")
path_salary = os.path.join("data", "salary")

workers_dict = {}
hours_dict = {}

with open(path_workers, "r", encoding="UTF-8") as workers:
    pass_head = 1
    for line in workers:
        if pass_head:
            pass_head = 0
            continue
        worker = re.split(r'\W+',line)
        workers_dict["{} {}".format(worker[0], worker[1])] = [x for x in worker[2:5]]

with open(path_hours, "r", encoding="UTF-8") as hours:
    pass_head = 1
    for line in hours:
        if pass_head:
            pass_head = 0
            continue
        worker_hours = re.split(r'\W+', line)
        hours_dict["{} {}".format(worker_hours[0], worker_hours[1])] = [x for x in worker_hours[2:3]]

salary = {}

for worker, biography in workers_dict.items():
    for worker_hours, done_hours in hours_dict.items():
        if worker == worker_hours:
            if int(biography[2]) == int(done_hours[0]):
                salary[worker] = [int(biography[0])]
            elif int(biography[2]) > int(done_hours[0]):
                salary[worker] = [int(biography[0]) * int(done_hours[0]) / int(biography[2])]
            elif int(biography[2]) < int(done_hours[0]):
                salary[worker] = [int(biography[0]) + int(biography[0]) * (int(done_hours[0]) - int(biography[2])) / int(biography[2]) * 2]

with open(path_salary, "w", encoding="UTF-8") as salary_file:
    print("{:10}{:10}{:10}".format("Имя", "Фамилия", "Зарплата"), file=salary_file)
    for worker, rubles in salary.items():
        name = worker.split(" ")[0]
        last_name = worker.split(" ")[1]
        print("{:10}{:10}{:<10.2f}".format(name, last_name, rubles[0]), file=salary_file)  # Не проверял результат


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


path_fruits = os.path.join("data", "fruits.txt")

for char in map(chr, range(ord("А"), ord("Я") + 1)):
    with open(path_fruits, "r", encoding="UTF-8") as fruits:
        print(char)
        cur_path = os.path.join("data",  "fruits_output", "fruits_{}.txt".format(char))   # Чтобы не засорять, создал папку вручную
        with open(cur_path, "w", encoding="UTF-8") as fruit_output:
            for line in fruits:
                print(line)
                if line.capitalize()[0] == char:
                    print("!!!!!")
                    print(line, file=fruit_output)
