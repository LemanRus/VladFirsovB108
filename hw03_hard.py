# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y


equation = "y = -12x + 11111140.2121"
x = 2.5

x_pos = equation.find("x")
eq_pos = equation.find("=")

a = float(equation[eq_pos+1:x_pos])             # Считаем, что уравнение записано как в задании
b = float(equation[x_pos+3:len(equation)+1])    # С пробелами и в заданном порядке

y = a * x + b
print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


date = '01.12.1985'
thirty_one = (1, 3, 5, 7, 8, 10, 12)

if len(date) == 10:
    dates = date.split(".")                            # Dates - финики с английского)
    try:
        if len(dates) == 3:
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2])
            if year in range(0, 10000):
                if month in range(0,13):
                    if month in thirty_one:
                        if day in range(1, 31):
                            print("Дата корректна")
                        else:
                            print("Неверно задан день")
                    else:
                        if day in range(1, 30):
                            print("Дата корректна")
                        else:
                            print("Неверно задан день")
                else:
                    print("Неверно задан месяц")
            else:
                print("Неверно задан год")
        else:
            print("Числа необходимо разделить точкой")
    except ValueError:
        print("Дату необходимо задать в числовом виде")
else:
    print("Некорректная дата")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3




interested_room = int(input("Введите номер комнаты от 1 до 2000000000\n"))  # При n > 10000000 компу плохо

# Условие таково, что налицо квадратные числа, т.к. сначала 1, потом 2 по 2, т.е. 2 в квадрате, потом 3 по 3 и т. д.
# Будем сначала строить башню до соответствующего квадратного числа, а потом находить этаж комнаты и её колонку

x = 1                   # Заполнитель для цикла
rooms = []              # Потом заполним комнатами "под" интересующей нас
floors_in_square = {}   # Потом определим количество этажей внутри определённого квадратного числа
tower = {}              # Заполним парами квадратное число - комнаты в нём

interested_floor = "Не получается"  # Проверял вывод, пусть останется
interested_pos = "Не получается"
interested_square = "Не получается"

while True:
    break_flag = 0                  # Будем мощно выходить из цикла
    current_square = x**2           # Квадратное число, в которое поместим его комнаты
    if rooms:
        start_room = rooms[-1]
    else:
        start_room = 0            # Точка отсчёта для цикла
    tower[current_square] = []      # Поместим квадратное число в словарик и обозначим для него комнаты
    for raise_num in range(current_square):
        current_room = start_room + raise_num +1  # Добавляем по одной комнате, +1 потому, что человеки считают не с нуля
        rooms.append(current_room)
        tower[current_square].append(current_room)
        if current_room >= interested_room:  # Не будем строить башню далее, чем необходимо
            break_flag = 1
            break
    if break_flag:
        break
    x += 1

for square, rooms in tower.items():  # Смотрим, в какой квадрат попала наша комната
    if interested_room in rooms:
        interested_square = square

rooms_in_square = tower[interested_square]  # Будем работать только с комнатами внутри определённого выше квадрата

floors_qty_in_square = int(interested_square**0.5)

for row in range(floors_qty_in_square):  # Разместим комнаты внутри квадрата по этажам
    floors_in_square[row] = []
    for column in range(floors_qty_in_square):  # Числа квадратные, количество этажей и колонок равно
        if rooms_in_square:
            floors_in_square[row].append(rooms_in_square[0])
            rooms_in_square.pop(0)

for current_floor, room_in_floor in floors_in_square.items():
    if interested_room in room_in_floor:
        floor_in_square = current_floor + 1  # Считаем с 1, ключ в словарике - наш этаж в квадрате
        floors_under_current_floor = sum([x for x in range(floors_qty_in_square)]) # Все этажи под нашим квадратом
        interested_floor = floors_under_current_floor + floor_in_square # Суммируем все этажи
        interested_column = floors_in_square[current_floor].index(interested_room) + 1  # Порядковый номер слева, как просили

print("Вход:", interested_room)
print("Выход:", interested_floor, interested_column)



