'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''

en_ru_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
}

with open("HW5_4_text.txt", 'r', encoding="utf-8") as f_in, \
        open("HW5_4_out.txt", 'w', encoding="utf-8") as f_out:
    for line in f_in.readlines():
        words_list = line.rstrip().split()
        print("=" * 20)
        print(words_list)
        for w in words_list:
            w_lower = w.lower()
            print(w_lower)
            if w_lower in en_ru_dict:
                idx = words_list.index(w)
                words_list.insert(idx, en_ru_dict[w_lower].capitalize())
                words_list.pop(idx + 1)
        f_out.write(" ".join(words_list) + "\n")
