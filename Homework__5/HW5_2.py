'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

count_lines, count_words, count_all_words = 0, 0, 0

with open("HW5_2_text.txt", 'r', encoding="utf-8") as f:
    for line in f.readlines():
        count_lines += 1
        print(f"строка №{count_lines}: ", end="")
        for w in line.strip().split():
            count_words += 1
        count_all_words += count_words
        print(count_words, "слов")
        count_words = 0

print("Итого: ", count_lines, " строк, ", count_all_words, "слов всего.")
