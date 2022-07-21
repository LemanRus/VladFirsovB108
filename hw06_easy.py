import sys, os

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:


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

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dirs():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print(f"Директория dir_{i} существует!")


def del_dirs():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), f"dir_{i}")
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print(f"Директории dir_{i} не существует!")

make_dirs()
del_dirs()


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def ls_dir():
    for item in os.listdir(os.getcwd()):
        if os.path.isdir(item):
            print(item)


ls_dir()


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.