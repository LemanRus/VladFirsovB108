#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import sys


class Loto:
    def __init__(self):
        self.bag_of_barrels = list(range(1, 100))
        self.player_card = self.make_card()
        self.computer_card = self.make_card()

    def __iter__(self):
        return self

    def __next__(self):
        if self.bag_of_barrels:
            chosen_barrel = random.choice(self.bag_of_barrels)
            self.bag_of_barrels.remove(chosen_barrel)
            self.turn(chosen_barrel)
        else:
            raise StopIteration

    def turn(self, barrel):
        print("\n\n\nНовый бочонок: {} (Осталось: {})".format(barrel, len(self.bag_of_barrels)))
        print("------ Ваша карточка ------")
        self.print_card(self.player_card)
        print("--- Карточка компьютера ---")
        self.print_card(self.computer_card)
        player_choise = input("Зачеркнуть карточку? (y/n)\n")
        for row in self.computer_card:
            for item in row:
                if item == barrel:
                    row_index = self.computer_card.index(row)
                    item_index = self.computer_card[row_index].index(item)
                    self.computer_card[row_index][item_index] = "-"
        is_in_card = False
        for row in self.player_card:
            for item in row:
                if item == barrel:
                    is_in_card = True
                    row_index = self.player_card.index(row)
                    item_index = self.player_card[row_index].index(item)
        if player_choise == "y":
            if not is_in_card:
                print("Вы проиграли!")
                sys.exit()
            else:
                self.player_card[row_index][item_index] = "-"  # После завершения циклов for выше последние значения - то, что нужно
        elif player_choise == "n":
            if is_in_card:
                print("Вы проиграли!")
                sys.exit()
            else:
                pass
        else:
            print("Советуем изучить правила и начать заново")
            sys.exit()
        computer_card_nums = self.parse_card(self.computer_card)
        player_card_nums = self.parse_card(self.player_card)
        if computer_card_nums == set("-"):
            if player_card_nums == set("-"):
                print("Ничья!")
                sys.exit()
            else:
                print("Вы проиграли!")
                sys.exit()
        else:
            if player_card_nums == set("-"):
                print("Вы выиграли!")
                sys.exit()

    def parse_card(self, card):
        parse = []
        for row in card:
            for item in row:
                if item is not None:
                    parse.append(item)
        return set(parse)


    def make_card(self):
        row_positions = [sorted(random.sample(range(9), 5)) for _ in range(3)]  # В каждом ряду из 9 позиций 5 заняты
        numbers = random.sample(range(1, 99), 27)  # Всего в карточке 15 уникальных чисел, замаскируем их после из 27
        random.shuffle(list(numbers))  # Функция выше вернёт числа по возрастанию, сделаем в случайном порядке
        card = []
        for i in range(3):
            row = []
            for num in range(9):
                if numbers:
                    row.append(numbers[-1])
                    numbers.pop()
            card.append(row)  # Наполняем карточку числами из списка уникальных чисел
        for test in zip(card, row_positions):
            for item in test[0]:  # Нечто с индексами - там, где позиция занята, число останется, где нет - будет None
                if test[0].index(item) not in test[1]:
                    test[0][test[0].index(item)] = None
        return card

    def print_card(self, card):  # Для красивого вывода
        for row in card:
            for i in row:
                if i is None:
                    print("   ", end="")
                else:
                    print("{:>3}".format(i), end="")
            print()
        print("-" * 27)

    def play_loto(self):
        while True:
            next(self)


loto = Loto()
loto.play_loto()
