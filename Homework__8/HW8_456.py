'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Storage:
    storage = {}

    def __init__(self, name):
        self.name = name

    def receive(self, eq):
        if not eq.name in Storage.storage:
            Storage.storage[eq.name] = []
        Storage.storage[eq.name].append(eq)

    def __str__(self):
        for k, i in Storage.storage.items():
            print(k, i)
        return ""


class Equipment:
    def __init__(self, name, ip, usb):
        self.name = name
        self.ip = ip
        self.usb = usb


class Printer(Equipment):
    def __init__(self, name, ip, usb, toner):
        super().__init__(name, ip, usb)
        self.toner = toner


class Scanner(Equipment):
    def __init__(self, name, ip, usb, sensor_type):
        super().__init__(name, ip, usb)
        self.sensor_type = sensor_type


class CopyMachine(Equipment):
    def __init__(self, name, ip, usb, autocopy=False):
        super().__init__(name, ip, usb)
        self.autocopy = autocopy


class Departement:
    def __init__(self, name):
        self.name = name
        self.equipment = {}

    def receive(self, eq):
        for e in eq:
            if not e.name in self.equipment:
                self.equipment[e.name] = []
            self.equipment[e.name].append(e)
            Storage.storage[e.name].remove(e)
            if not Storage.storage[e.name]:
                Storage.storage.pop(e.name)


# создание склада и отделов
storage1 = Storage("Главный склад")
dep1 = Departement("Бухгалтерия")
dep2 = Departement("Отдел продаж")

# создание оргтехники ("покупка")
pr1 = Printer("принтер", "192.168.1.20", True, 0.95)
pr2 = Printer("принтер", "192.168.1.21", True, 0.70)
sc1 = Scanner("сканер", "192.168.1.22", True, "CIS")
cm1 = CopyMachine("ксерокс", "192.168.1.23", True, True)

# внесение товара на склад:
storage1.receive(pr1)
storage1.receive(pr2)
storage1.receive(sc1)
storage1.receive(cm1)

print("Хранилище после наполнения оборудованием:")
print("Storage: ", Storage.storage)

# передача в подразделения:
dep1.receive((pr1, pr2, sc1))
dep2.receive((cm1,))

print("\nХранилище после передачи оборудования:")
print("Storage: ", Storage.storage)

print("\nОборудование по подразделениям (некрасивое представление, но полагаю более функциональное, только для служебного пользования):")
print("Оборудование (", dep1.name, "): ", dep1.equipment)
print("Оборудование (", dep2.name, "): ", dep2.equipment)

print("\nОборудование по подразделениям (красивое представление списками):")
for dep in (dep1, dep2):
    print("=" * 30, "\nОборудование (", dep.name, "):")
    for k, i in dep.equipment.items():
        print("\t-", k)
        for item in i:
            print("\t\t-", item.ip)

