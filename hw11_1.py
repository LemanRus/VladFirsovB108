# Реализовать решение следующей задачи:
# «Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) пишут в одну книгу.
# Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся,
# чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный поток.
# Одновременно книгу может читать несколько читателей, но писать единовременно может только один писатель.»

import random
import threading

book = ""

writers_qty = 2  # Задать сразу количество потоков-писателей
readers_qty = 3  # Так же и для читателей

readers_count = 0

take_book = threading.Lock()  # Взять может и писатель, и читатель, одинаковая блокировка для одинакового приоритета
work_with_book = threading.Lock()  # Блокировка для собственно книги, для кода записи или чтения
readers_counter = threading.Lock()  # Читателей много, первый заблокирует книгу, последний освободит


def writer():
    global book

    while True:
        with take_book:
            work_with_book.acquire()

        print(f'Сейчас пишет: {threading.current_thread().name}.')
        if len(book) < 100:
            book += "".join(map(chr, [random.randint(49, 150) for _ in range(15)]))  # Цифровая литература
        else:
            book = "".join(map(chr, [random.randint(49, 150) for _ in range(15)]))
        print(f"Текст книги: {book}")

        work_with_book.release()


def reader():
    global readers_count

    while True:
        with take_book:
            readers_counter.acquire()
            readers_count += 1
            if readers_count == 1:
                work_with_book.acquire()
        readers_counter.release()

        print(f'Сейчас читает {threading.current_thread().name}:')

        with readers_counter:
            readers_count -= 1
            if readers_count == 0:
                work_with_book.release()


threads = [threading.Thread(target=reader) for _ in range(readers_qty)] + \
          [threading.Thread(target=writer) for _ in range(writers_qty)]

for thread in threads:
    thread.start()
