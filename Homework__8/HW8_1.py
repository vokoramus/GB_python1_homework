'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, str_):
        # self.str_ = str_
        date = Date.parse(str_, "D")
        month = Date.parse(str_, "M")
        year = Date.parse(str_, "Y")
        self.validate(date, month, year)
        print(date, month, year)

    @classmethod
    def parse(cls, date, YMD):
        date = date.split("-")
        if YMD == "D":
            return int(date[0])
        if YMD == "M":
            return int(date[1])
        if YMD == "Y":
            return int(date[2])
        else:
            raise ValueError("Ошибка формата!")

    @staticmethod
    def validate(date, month, year):
        if not (1600 <= year <= 2100):
            print("invalid year value!!!")
        if not (1 <= month <= 12):
            print("invalid month value!!!")
        if month in (1, 3, 5, 7, 8, 10, 12):
            day_max = 31
        elif month == 2:
            day_max = 29 if month == 2 and year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0) else 28
        else:
            day_max = 30
        # print("max_day:", day_max)
        if not (1 <= date <= day_max):
            print("invalid day value!!!")


d = Date("2-2-1600")
