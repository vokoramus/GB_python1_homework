'''
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
lst = []
while True:
    length = input("Input list lenght: ")
    if length.isdigit():
        length = int(length)
        break

for n in range(1, length + 1):  # starts from 1 for normally numeration output for user
    if n == 1:
        end = "st"
    elif n == 2:
        end = "nd"
    else:
        end = "th"
    el = input(f"Input list the {n}-{end} element: ")
    lst.append(el)
print("1: ", lst)

# pairs reversing
# var 1 - with slices
lst_even_idx = lst[::2]
lst_odd_idx = lst[1::2]
# print(lst_even_idx)
# print(lst_odd_idx)

new_list = []
trigger = 1
for _ in range(length):
    if trigger == 1:
        new_el = lst_even_idx.pop(0)
        new_list.append(new_el)
    else:
        new_el = lst_odd_idx.pop(0)
        new_list.insert(-1, new_el)
    # print(new_el)
    trigger *= -1
print("2: ", new_list)

# var 2 - direct reversing (will change user`s list)
for n in range(length // 2):
    lst[2 * n], lst[2 * n + 1] = lst[2 * n + 1], lst[2 * n]
print("3: ", lst)

