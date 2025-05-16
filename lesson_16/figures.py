import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



class Square(Figure):
    def __init__(self, side, name):
        self.__side = side
        self.name = name

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        self.__side_a = side_a
        self.__side_b = side_b
        self.name = name

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, name):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.name = name

    def perimeter(self):

        return self.__side_a + self.__side_b + self.__side_c

    def area(self):
        s = self.perimeter() / 2
        return int(math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c)))


square = Square(side=5, name="square")
rectangle = Rectangle(side_a=4, side_b=5, name="rectangle")
triangle = Triangle(side_a=6, side_b=5, side_c=8, name="triangle")

figures = [square, rectangle, triangle]


for figure in figures:
    print(f"Area of {figure.name} is {figure.area()}, "
          f"Perimeter of {figure.name} is {figure.perimeter()}")