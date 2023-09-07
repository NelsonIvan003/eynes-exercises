import math


class Circle:
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Para crear el círculo, el radio debe ser mayor que cero. "
                             f"Intentó ingresar como radio: {r}")
        self.radius = r
        print(f"Has creado exitosamente un círculo de radio: {self.radius}")

    def get_radius(self):
        return self.radius

    def set_radius(self, r):
        if r <= 0:
            raise ValueError(f"Error al intentar modificar el círculo. El nuevo radio debe ser mayor que cero.")
        self.radius = r

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)

    def get_perimeter(self):
        return math.pi * 2 * self.radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("Error: Para poder realizar la multiplicación debe ingresar un valor mayor que cero.")
        return Circle(self.radius * n)

    def __str__(self):
        message = f"Círculo de radio: {self.radius}, perímetro \u2248 {self.get_perimeter()}, área \u2248 {self.get_area()}"
        return message


try:
    circle_3 = Circle(5)
    print(circle_3)
    circle_4 = circle_3 * 7
    print(circle_4)
except ValueError as e3:
    print("Error:", e3)




