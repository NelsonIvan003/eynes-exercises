import math


class Circle:
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Para crear el círculo, el radio debe ser mayor que cero. "
                             f"Intentó ingresar como radio: {r}")

        self.radius = r
        print(f"Haz creado exitosamente un círculo de radio: {self.radius}")


# circle_1 error
try:
    circle_1 = Circle(0)
except ValueError as e1:
    print("Error:", e1)

# circle_2 error
try:
    circle_2 = Circle(-2)
except ValueError as e2:
    print("Error:", e2)

# circle_3 success
try:
    circle_3 = Circle(5)
except ValueError as e3:
    print("Error:", e3)




