'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.

В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}
        # print(Position.get_full_name(self, position))

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)
        self.full_name = self.get_full_name()
        self.total_income = self.get_total_income()

    def get_full_name(self):
        # return self.name + " " + self.surname
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return self._Worker__income["wage"] + self._Worker__income["bonus"]


w1 = Position("Дядя Вася", "Печкин", "Бриллиантовый директор", 20000, 5000)

print("Имя: ", w1.name)
print("Фамилия: ", w1.surname)
print("Должность: ", w1.position)
print("Полное имя: ", w1.get_full_name())
print("Полный доход: ", w1.get_total_income())
