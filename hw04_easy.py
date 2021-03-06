# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


def convert(km):
    miles_qty = km / 1.069
    miles = "{:.4f} miles".format(miles_qty)
    print(miles)  # Вывод, как в задании, но покрасивее просто числа)

convert(12)
convert(45.895)
convert(0)
convert(-6) #  На случай какой-нибудь разницы или обратного пути)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    str_number = str(number)
    num_parts = str_number.split(".")
    if num_parts[1][ndigits:ndigits+1] in range(5):
        frac_part = num_parts[1][:ndigits]
    else:
        frac_part = str(int(num_parts[1][:ndigits]) + 1)
    if len(frac_part) == ndigits:
        return num_parts[0] + "." + frac_part
    else:
        return str(int(num_parts[0]) + 1) + "." + "0"*ndigits

print(my_round(2.1234567, 4))
print(my_round(2.1999947, 3))
print(my_round(2.9999967, 2))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    str_ticket_number = str(ticket_number)
    first_part = str_ticket_number[:len(str_ticket_number) // 2]
    if len(str_ticket_number) % 2 == 0:
        last_part = str_ticket_number[len(str_ticket_number) // 2:]
    else:
        last_part = str_ticket_number[len(str_ticket_number) // 2 + 1:]
    first_nums = []
    last_nums = []
    for i in first_part:
        first_nums.append(int(i))
    for k in last_part:
        last_nums.append(int(k))
    return sum(first_nums) == sum(last_nums)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436651))
print(lucky_ticket(436751))
print(lucky_ticket(43759))