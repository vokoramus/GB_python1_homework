'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.'''


def int_func(word):
    return word.capitalize()


if __name__ == "__main__":  # для возможности импорта в HW3_7.py
    print(int_func("abracadabra"))
