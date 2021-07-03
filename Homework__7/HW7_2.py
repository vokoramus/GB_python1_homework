'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта,
    проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    common_square = 0

    def __init__(self, item_square, data):
        self.item_square = item_square
        if item_square > 0:
            print(f"Создаем {data[0]} ({data[1]} = {item_square}, площадь = {self.square})")
            self.summ()

    @property
    @abstractmethod
    def square(self):
        pass

    def summ(self):
        Clothes.common_square = round(Clothes.common_square + self.square, 2)
        print(self)

    def zero(self):
        Clothes.common_square = 0
        print("=== Обнуление общей площади ===")
        print(self)

    def __str__(self):
        return "Общая площадь = " + str(self.common_square)

class Coat(Clothes):
    def __init__(self, square_item_):
        self.data = "пальто", "размер"
        super().__init__(square_item_, self.data)

    @property
    def square(self):
        return round(self.item_square / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, square_item_):
        self.data = "костюм", "рост"
        super().__init__(square_item_, self.data)

    @property
    def square(self):
        return round(self.item_square * 2 + 0.3, 2)


c = Coat(48)
c2 = Coat(54)
s = Suit(1.85)


# Обнуляем:
z = Coat(0)
z.zero()
