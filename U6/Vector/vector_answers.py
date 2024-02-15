import math

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return vector(x, y, z)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def magnitude(self): #A1
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def unit(self): #A2
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("Magnitude = 0")

        x = self.x / mag
        y = self.y / mag
        z = self.z / mag

        return vector(x, y, z)

    def dot(self, other): #A3
        return self.x * other.x + self.y * other.y + self.z * other.z
    
a = vector(1.0, 0.0, 0.0)
b = vector(0.0, 1.0, 0.0)
c = vector(0.0, 0.0, 1.0)

assert math.isclose((a        ).magnitude(),           1.0 )
assert math.isclose((    b    ).magnitude(),           1.0 )
assert math.isclose((        c).magnitude(),           1.0 )
assert math.isclose((a + b    ).magnitude(), math.sqrt(2.0))
assert math.isclose((    b + c).magnitude(), math.sqrt(2.0))
assert math.isclose((a   +   c).magnitude(), math.sqrt(2.0))
assert math.isclose((a + b + c).magnitude(), math.sqrt(3.0))

u = vector(1.0, 2.0, 3.0)
v = vector(4.0, 5.0, 6.0)

assert math.isclose(u.unit().magnitude(), 1.0)
assert math.isclose(v.unit().magnitude(), 1.0)

assert u.dot(v) == 32.0
assert v.dot(u) == 32.0

print("PASS")
