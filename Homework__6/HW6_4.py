'''
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed += speed
        print("\n", f"{'-' * 5} Car {self.name} started {'-' * 5}")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f"Car {self.name} stopped")

    def turn(self, direction):
        print(f"Car turned: {direction}")

    def show_speed(self):
        print(f"Car {self.name}: current speed is {self.speed}.")

class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > TownCar.MAX_SPEED:
            print(f"   Your speed is too big! Max.speed is {TownCar.MAX_SPEED}.")


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > WorkCar.MAX_SPEED:
            print("Your speed is too big! Max.speed is", WorkCar.MAX_SPEED)


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


town_car_1 = TownCar("green", "WV")
sport_car_1 = SportCar("yellow", "Bugatti")
work_car_1 = WorkCar("white", "Mercedes")
police_car_1 = PoliceCar("blue", "Chevrolet")

print(f"{'=' * 35}")
print(f"*** АТРИБУТЫ ***")
print(town_car_1.name)
print(police_car_1.is_police)
print(work_car_1.color)
print(f"{'=' * 35}")

town_car_1.go(80)
sport_car_1.go(250)
work_car_1.go(30)
police_car_1.go(150)

town_car_1.stop()
sport_car_1.stop()
work_car_1.stop()
police_car_1.stop()
