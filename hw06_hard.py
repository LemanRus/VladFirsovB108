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

