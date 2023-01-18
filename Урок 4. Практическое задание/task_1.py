"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

my_name, my_time, my_salary, my_bonus = argv
try:
    my_time = int(my_time)
    my_salary = int(my_salary)
    my_bonus = int(my_bonus)
    my_res = my_time * my_salary + my_bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')