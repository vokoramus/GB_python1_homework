'''Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().'''

from HW3_6 import int_func  # это еще не проходили, но сделал так, чтобы не дублировать функцию сюда

res = []

string = input("Введите строку: ").split(" ")
for word in string:
    res.append(int_func(word))

print(" ".join(res))
