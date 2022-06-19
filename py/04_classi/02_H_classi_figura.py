# Creiamo due classi: la prima è la classe `Quadrato`, che modella tutti i
# quadrati; la seconda è la classe `Cerchio`, che modella tutti i cerchi.
# Entrambe devono discendere da una classe base chiamata `Figura`.

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @property
    def perimeter(self):
        return self.__perimeter

    @property
    def area(self):
        return self.__area

    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self, side: float):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value: float):
        self.__side = value

    def perimeter(self) -> float:
        return round(2 * self.side, 4)

    def area(self) -> float:
        return round(self.side**2, 4)


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        self.__radius = value

    def circumference(self) -> float:
        return round(2 * pi * self.radius, 4)

    def area(self) -> float:
        return round(pi * (self.radius**2), 4)


sqr = Square(8.5)
print(f"Side: {sqr.side}\nPerimeter: {sqr.perimeter()}\nArea: {sqr.area()}")

print("")

circ = Circle(2.7)
print(
    f"Radius: {circ.radius}\n"
    f"Circumference: {circ.circumference()}\n"
    f"Area: {circ.area()}"
)


# soluzione del professore
#
# from abc import ABC, abstractmethod
# from math import pi
#
# class Figura(ABC):
#
#     @property
#     def perimetro(self):
#         return self.__perimetro
#
#     @property
#     def area(self):
#         return self.__area
#
#     @abstractmethod
#     def perimetro(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Quadrato(Figura):
#
#     def __init__(self, lato):
#         self.lato = lato
#
#     @property
#     def lato(self):
#         return self.__lato
#
#     @lato.setter
#     def lato(self, value):
#         self.__lato = value
#
#     def perimetro(self):
#         return self.lato * 4
#
#     def area(self):
#         return self.lato ** 2
#
#
# class Cerchio(Figura):
#
#     def __init__(self, raggio):
#         self.raggio = raggio
#
#     @property
#     def raggio(self):
#         return self.__raggio
#
#     @raggio.setter
#     def raggio(self, value):
#         self.__raggio = value
#
#     def perimetro(self):
#         return 2 * pi * self.raggio
#
#     def area(self):
#         return pi * (self.raggio ** 2)
#
#
# # Esempio di uso
# q = Quadrato(5)
# print('Lato: {} - Perimetro: {} - Area: {}'.format(q.lato, q.perimetro(), q.area()))
#
# c = Cerchio(5)
# print('Raggio: {} - Perimetro: {} - Area: {}'.format(c.raggio, c.perimetro(), c.area()))
