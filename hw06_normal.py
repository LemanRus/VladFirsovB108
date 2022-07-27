# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
import os
import sys


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5  # Из отрицательных чисел корни тоже бывают, комплексные числа тоже числа))

try:
    a = float(input("a = "))
    b = float(input("b = "))
except ValueError:  # Ограничено вводом, больше не предвижу ошибок...
    print("Вводите числа!")
else:
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))


# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html


# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


from hw06_easy import ls_dir


def change_dir():
    dir_to_go = input("Введите имя папки: ")
    if dir_to_go in os.listdir(os.getcwd()):
        os.chdir(dir_to_go)
        print("Текущая папка:", os.getcwd())
    else:
        print("Такой папки нет в текущем рабочем каталоге")


def del_dir():
    dir_to_del = input("Введите имя папки: ")
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_to_del))
    except FileNotFoundError:
        print("Такой папки нет в текущем рабочем каталоге")
    else:
        print(f"Папка {dir_to_del} удалена")


def make_dir():
    dir_to_make = input("Введите имя папки: ")
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_to_make))
    except FileExistsError:
        print(f"Директория {dir_to_make} существует!")
    else:
        print(f"Папка {dir_to_make} создана")


actions = {
    "1": change_dir,
    "2": ls_dir,
    "3": del_dir,
    "4": make_dir,
}
while True:
    print("Выберите действие:\n"
          "1. Перейти в папку\n"
          "2. Просмотреть содержимое текущей папки\n"
          "3. Удалить папку\n"
          "4. Создать папку\n"
          "Для выхода введите 'exit'")

    user_choise = input()
    if user_choise == "exit":
        sys.exit()
    choised_action = actions.get(user_choise)
    if choised_action is not None:
        choised_action()
        print("-" * 30 + "Выполнено" + "-" * 30 + "\n")
    else:
        print("\nВыбран несуществующий пункт меню\n")