'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц).  Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
 первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, *args):
        self.__mtr = args

    def __str__(self):
        res = ""
        for st in self.__mtr:
            for d in st:
                res += str(d) + "\t"
            res += "\n"

        return res

    def m_dim(self):
        y = len(self.__mtr)
        x = 0
        if y:
            x = len(self.__mtr[0])
        # print("LEN", y, x)
        return y, x

    def __add__(self, other):
        if self.m_dim() != other.m_dim():
            raise TypeError("Matrix dimensions are not equal")
        else:
            # print("ok")
            result = []
            for i in range(self.m_dim()[0]):
                result_new_str = [sum(i) for i in zip(self.__mtr[i], other.__mtr[i])]
                result.append(result_new_str)
            return Matrix(*result)


m1 = Matrix([31, 22],
            [37, 43],
            [51, 86])

m2 = Matrix([-30, -22, 1],
            [-36, -42, 1],
            [-50, -85, 1])

m3 = Matrix([-30, -21],
            [-36, -42],
            [-50, -85])

print(m1)

# print(m1 + m2)  # My TypeError

m_sum2 = m1 + m3
print(m_sum2)
# print("m_sum2 dim: ", m_sum2.m_dim())

m_sum3 = m1 + m3 + m3
print(m_sum3)
# print(m_sum3.m_dim())

