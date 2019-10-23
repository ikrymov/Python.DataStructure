__author__ = 'Крымов Иван'

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)

print(arr)

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print("Минимальное число в массиве это число {}, а максимальное число в массиве - это число {}".format(arr[imn],arr[imx]))

arr[imn], arr[imx] = arr[imx], arr[imn]

print(arr)
