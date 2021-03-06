'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''
goods = []
num = 0
parameters = [
    "название",
    "цена",
    "количество",
    "ед.изм.",
]

menu = {}
menu[0] = "выход"
menu[1] = "добавить товар"
menu[2] = "вывести аналитику"

while True:
    for i in range(100): print()
    print("======= меню ==========")
    for k, v in menu.items():
        print(f"{k} - {v}")
    print("=======================")
    com = input("Введите команду: ")
    if not com.isdigit(): continue
    com = int(com)
    if com > len(menu) + 1: continue

    if com == 0:
        for i in range(100): print()
        print("до свидания! ...")
        break
    elif com == 1:
        for i in range(100): print()
        print("добавление товара...")
        new_good = {}
        num += 1
        for par in parameters:
            par_value = input(f"Введите {par}: ")
            new_good[par] = par_value
        goods.append((num, new_good))

        for g in goods:
            print(g)
        x = input()

    elif com == 2:
        for i in range(100): print()
        print("======= аналитика ==========")
        res = {}
        for i, par in enumerate(parameters):
            param_values = set()
            for g in goods:
                param_values.add(g[1][par])
            res[par] = list(param_values)

        # print result
        for r in res.items():
            print(r)
        input("     ...... нажмите любую клавишу .......")

# fictive comment (just for new pull-request)
