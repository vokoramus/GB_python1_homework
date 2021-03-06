'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''

class Cell:
    def __init__(self, n):
        self.n = int(n)
        pass

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n < other.n:
            print("First par. must be greater than second!")
            return None
        else:
            return Cell(self.n - other.n)

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        if other.n == 0:
            print("Second par. must be not equal zero!")
            return None
        else:
            return Cell(self.n // other.n)

    def make_order(self, height):
        rows = (self.n // height) * ("*" * height + "\n")
        last_row = "*" * (self.n % height)
        return rows + last_row


c1 = Cell(14)
c2 = Cell(3)

c_sum = c1 + c2
print(c_sum.n)
print(c_sum.make_order(4))

c_sub2 = c2 - c1

print("mul: ", (Cell(4) * Cell(5)).n)
print("div: ", (Cell(20) / Cell(3)).n)
