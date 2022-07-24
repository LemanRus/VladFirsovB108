"""
    ПРИМЕЧАНИЕ: Для решения задачи необходимо познакомиться с модулями os, sys, argparse!
    СМ.: https://pythonworld.ru/moduli/modul-os.html,
    https://pythonworld.ru/moduli/modul-sys.html,
    https://habr.com/ru/company/ruvds/blog/440654/

    Задача похожа на задачу 2 из normal, однако, имеет особенности. Вы можете использовать решения из задачи 2.

    Задача:
    Напишите небольшую консольную утилиту, позволяющую работать с папками и файлами.
    Утилита должна работать с помощью параметров и флагов, передаваемых скрипту в командной строке.
    Примеры:
        python hw06_hard.py -touch ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -rm ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -mkdir ../dir1/newdir -ls ../dir1/
        python hw06_hard.py -ls ../dir1/
        python hw06_hard.py -touch ../dir1/test.txt

        и.т.д.

    Используйте модули argparse (для разбора аргументов), os, sys.

    Утилита должна принимать следующие флаги и выполнять следующие действия:
    "-ls <путь до папки>" - Посмотреть все файлы и подпапки в папке
    "-touch <путь до нового файла>" - Создать файл
    "-rm <путь до файла>" - Удалить файл
    "-mkdir <путь до папки>" - Создать папку

    Каждый из представленных параметров не обязательный, но если не указать никакой, то утилита должна вывести
    уведомление, которая предлагает посмотреть --help.
    Предусмотреть обработку исключений, например, если пытаются посмотреть все файлы не у папки, а у файла и.т.д.
"""


import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Process commands')

parser.add_argument('-touch', type=str, help='создаёт файл')
parser.add_argument('-rm', type=str, help='удаляет указанный файл')
parser.add_argument('-mkdir', type=str, help='создаёт папку')
parser.add_argument('-ls', type=str, help='выдаёт информацию о каталоге')  # Порядок важен для использования нескольких команд в одной строке
                                                                           # Как пофиксить порядок обработки, не придумал

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


def del_file(path):
    try:
        os.remove(os.path.join(path))
    except FileNotFoundError:
        print(f"Файл {path} не существует")


def make_dir(path):
    try:
        os.mkdir(os.path.join(path))
    except FileExistsError:
        print(f"Директория {path} существует!")
    else:
        print(f"Папка {path} создана")


def list_dir(path):
    for item in os.listdir(os.path.join(path)):
        print(item)


def make_file(path):
    os.makedirs(os.path.split(os.path.join(path))[0], exist_ok=True)
    with open(os.path.join(path), "a"):  # Файл как бы есть, даже если уже был) Но пусть будет НЕ перезаписан
        pass
    print(f"Файл {path} создан")


actions = {
    "touch": make_file,
    "rm": del_file,
    "mkdir": make_dir,
    "ls": list_dir,
}

for arg, parameter in vars(args).items():  # Наверняка есть более правильный и изящный способ,
    if parameter:                          # но и этот работает))
        actions[arg](parameter)
