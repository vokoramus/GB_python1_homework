'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def multiple(a, b):
    return a * b

seq = [n for n in range (100, 1001) if n % 2 == 0]
res = reduce(multiple, seq)
print(res)
print("Офигеть, результат содержит", len(str(res)), "цифр")
