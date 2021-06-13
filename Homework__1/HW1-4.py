'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

n = int(input("Введите n: "))
max_char = n % 10
while n > 0:
    last_chr = n % 10
    if last_chr > max_char:
        max_char = last_chr
    n //= 10
print("max =", max_char)