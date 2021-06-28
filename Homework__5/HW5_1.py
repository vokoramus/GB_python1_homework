'''1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

data = []

with open("HW5_1_text.txt", 'w', encoding="utf-8") as f:
    while True:
        string = input("Input string to recording (empty string to stop): ")
        if string == "":
            f.writelines(data)
            break
        else:
            data.append(string + '\n')

print("Data recorded")
