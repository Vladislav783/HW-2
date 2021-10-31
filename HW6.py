# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
print('Напишите число от 1 до 10:')
a = int(input())
print("генерируемые целые числа с указаного:")
for item in count(a):
    if item > 10:
        break
    else:
        print(item)

print("Повторяющиеся элементы списка:")
i = 0
for value in cycle([1, 2, 3]):
    if i > 10:
        break
    print(value)
    i += 1

#сложновато как-то. Сделать бы cycle от 1 до указаного пользователем числа...