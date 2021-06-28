'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint, random

file = "HW5_5_text.txt"
common_sum = 0
# separator = ";"
separator = " "

with open(file, 'w', encoding="utf-8") as f:
    for _ in range(randint(2, 10)):
        arr = [str(round(random() * 100, 2)) for _ in range(randint(2, 10))]
        f.write(separator.join(arr) + "\n")

with open(file, 'r', encoding="utf-8") as f:
    for line in f.readlines():
        try:
            s = [float(i) for i in line.rstrip().split(separator)]
            common_sum += sum(s)
            # print(sum(s))
        except ValueError:
            print("Only numbers must be in file")

print(round(common_sum, 2))
