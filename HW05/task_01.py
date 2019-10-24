__author__ = 'Крымов Иван'

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех
# предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

orgs = {}
n = int(input("Введите количество организаций: "))

for i in range(n):
    org_name = input("Введите название организации номер " + str(i + 1) + ": ")
    t_profit = 0
    for j in range(1, 5):
        profit = int(input(f"Введите прибыль за квартал " + str(j) + ": "))
        t_profit += profit
    orgs[org_name] = int(t_profit)

print(orgs)

avg = sum(Counter.values(orgs))/n

for el in orgs:
    if orgs.get(el) < avg:
        print("Прибыль организации {} меньше среднего {}  по группе компаний".format(el, avg))
    else:
        print("Прибыль организации {} выше среднего {}  по группе компаний".format(el, avg))
