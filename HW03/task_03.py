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
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))

arr[imn], arr[imx] = arr[imx], arr[imn]

print(arr)
