'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input("Числитель: "))
    b = float(input("Знаменатель: "))
    if b == 0:
        raise MyZeroDivision("Division by zero!!!")
    print("Результат = ", a / b)
except MyZeroDivision as e:
    print(e.txt)
