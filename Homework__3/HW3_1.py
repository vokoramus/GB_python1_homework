''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def div(a, b):
    if b == 0:
        print("Деление на 0!")
    return a / b


def int_validator(txt):
    while True:
        n = input(f"{txt}: ")
        try:
            n = int(n)
        except ValueError:
            print("Введите число!")
            continue
        break
    return n


a = int_validator("Числитель")
b = int_validator("Знаменатель")

print("Результат деления:", div(a, b))
