__author__ = 'Крымов Иван'


# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def even_odd_numbers(num):
    even_num = 0
    odd_num = 0
    zero_num = 0
    for el in num:
        if int(el) == 0:
            zero_num += 1
        elif (int(el) % 2 != 0) and (int(el) != 0):
            odd_num += 1
        elif int(el) % 2 == 0:
            even_num += 1
    print("В веденном числе {} четных цифр, {} нечетных цифр и {} нуля.".format(even_num, odd_num, zero_num))


number = input("Введите целое число:")
even_odd_numbers(number)
