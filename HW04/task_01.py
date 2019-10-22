__author__ = 'Крымов Иван'

import cProfile
import timeit

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


# вариант 1
def func_1():
    for i in range(2, 10):
        frequency = 0
        for j in range(2, 100):
            if j % i == 0:
                frequency += 1
        return f'Числу {i} кратно {frequency} чисел'


s1 = """

def func_1():
    for i in range(2, 10):
        frequency = 0
        for j in range(2, 100):
            if j % i == 0:
                frequency += 1
        return f'Числу {i} кратно {frequency} чисел'

"""

# вариант 2
def func_2():
    frequency = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                frequency[j - 2] += 1

    for i, item in enumerate(frequency, start=2):
        return f'Числу {i} кратно {item} чисел'

s2 = """

def func_2():
    frequency = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                frequency[j - 2] += 1

    for i, item in enumerate(frequency, start=2):
        return f'Числу {i} кратно {item} чисел'

"""

# вариант 3
def func_3():
    a = [0]*8
    for i in range(2,100):
        for j in range(2,10):
            if i%j == 0:
                a[j-2] += 1
    i = 0
    while i < len(a):
        return f'{i+2}  -  {a[i]}'
        i += 1

s3 = """

def func_3():
    a = [0]*8
    for i in range(2,100):
        for j in range(2,10):
            if i%j == 0:
                a[j-2] += 1
    i = 0
    while i < len(a):
        return f'{i+2}  -  {a[i]}'
        i += 1

"""

cProfile.run('func_1()')
print(timeit.timeit(s1, number=100))
cProfile.run('func_2()')
print(timeit.timeit(s2, number=100))
cProfile.run('func_3()')
print(timeit.timeit(s3, number=100))


# /usr/local/bin/python3.7 /Users/ikrymov/Desktop/GeekBrains.Mail.ru/Python.DataStructure/HW04/task_01.py
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_01.py:14(func_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 8.177999999997576e-06
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_01.py:36(func_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 7.69599999999801e-06
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_01.py:61(func_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 7.25800000000304e-06