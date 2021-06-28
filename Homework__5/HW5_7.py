'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

from json import dump

file = "HW5_7_text.txt"
file2 = "HW5_8_text.json"
firm_list = [{}, {"average_profit": 0}]
n = 0
# firm_dict = {}
# firm_list.append(firm_dict)
# firm_json = ...

with open(file, 'r', encoding="utf-8") as f:
    for line in f.readlines():
        firm_data = line.rstrip().split()
        profit = int(firm_data[2]) - int(firm_data[3])
        firm_list[0][firm_data[0]] = profit
        if profit >= 0:
            firm_list[1]["average_profit"] += profit
            n += 1

firm_list[1]["average_profit"] /= n

print(firm_list)

with open(file2, 'w', encoding="utf-8") as f:
    dump(firm_list, f)
