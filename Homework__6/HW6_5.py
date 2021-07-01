'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        t = "pen"
        super().__init__(t)

    def draw(self):
        print("Рисуем Ручкой")


class Pencil(Stationery):
    def __init__(self):
        t = "pencil"
        super().__init__(t)

    def draw(self):
        print("Рисуем Карандашом")


class Handle(Stationery):
    def __init__(self):
        t = "handle"
        super().__init__(t)

    def draw(self):
        print("Рисуем Маркером")


pen = Pen()
pencil = Pencil()
handle = Handle()

print(f"title инструмента 'Ручка': {pen.title}")
print(f"title инструмента 'Карандаш': {pencil.title}")
print(f"title инструмента 'Маркер': {handle.title}")

pen.draw()
pencil.draw()
handle.draw()