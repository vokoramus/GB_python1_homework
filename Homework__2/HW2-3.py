'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

m = int(input("month: "))
lst = [None, "зима", "зима",
       "весна", "весна", "весна",
       "лето", "лето", "лето",
       "осень", "осень", "осень",
       "зима"
       ]
print("from_list: ", lst[m])

dic = {"зима": [1, 2, 12],
       "весна": [3, 4, 5],
       "лето": [6, 7, 8],
       "осень": [9, 10, 11],
       }
for key, value in dic.items():
    # print(key, value)
    if m in value:
        print("from_dict: ", key)
        break

# fictive comment (just for new pull-request)
