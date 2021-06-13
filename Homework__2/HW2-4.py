'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''

string = input("input string: ")
word_list = string.split()
for n, word in enumerate(word_list):
    if len(word) > 10:
        word = word[:10]
    print(f"{n + 1}: {word}")
