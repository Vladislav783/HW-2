#1. Реализовать скрипт, в котором должна быть
# предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

# from sys import argv
#
# print (int(argv[script_name], [hours_production], [rate_per_hour]))
#ладно, ступор возник, зато нашел способ подсчета с помощью simple calc

def simple_calc():
    a = float(input('Введите количество отработанных часов: '))
    b = float(input('Введите сумму оплаты труда за 1 час: '))
    c = float(input('Укажите размер премии: '))
    pay = a * b
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')

