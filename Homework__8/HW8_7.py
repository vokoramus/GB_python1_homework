'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self, s):
        s_parsed = s.split(" ")
        # print(s_parsed)
        self.Re = int(s_parsed[0])
        sign = s_parsed[1]
        self.Im = int(s_parsed[2][1:]) * (-1 if sign == "-" else 1)

        # print(self.Re)
        # print(self.Im)
        # print(sign)

    def __str__(self):
        return self.construct_complex(self.Re, self.Im)

    def __add__(self, other):
        Re_new = self.Re + other.Re
        Im_new = self.Im + other.Im
        return Complex(self.construct_complex(Re_new, Im_new))

    def __mul__(self, other):
        Re_new = self.Re * other.Re - self.Im * other.Im
        Im_new = self.Re * other.Im + other.Re * self.Im
        return Complex(self.construct_complex(Re_new, Im_new))

    @staticmethod
    def construct_complex(Re, Im):
        return str(Re) + (" - j" if Im < 0 else " + j") + str(abs(Im))


c1 = Complex("2 + j3")
c2 = Complex("-1 + j1")
# print(c1.Re, c1.Im)
# print(c2.Re, c2.Im)

print("sum: ", c1 + c2 + c1)
print("mul: ", c1 * c2)
