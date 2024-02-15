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

    def magnitude(self): #Q1
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def unit(self): #Q2
        /self.magnitude

    def dot(self, other): #Q3
        for index in other:
            self[index] = self[index] * other[i]
        dot = 0
        for number in self:
            dot += number
        return dot
            


    
x = vector(1.0, 0.0, 0.0)
y = vector(0.0, 1.0, 0.0)
z = vector(0.0, 0.0, 1.0)

assert math.isclose((x        ).magnitude(),           1.0 )
assert math.isclose((    y    ).magnitude(),           1.0 )
assert math.isclose((        z).magnitude(),           1.0 )
assert math.isclose((x + y    ).magnitude(), math.sqrt(2.0))
assert math.isclose((    y + z).magnitude(), math.sqrt(2.0))
assert math.isclose((x   +   z).magnitude(), math.sqrt(2.0))
assert math.isclose((x + y + z).magnitude(), math.sqrt(3.0))

u = vector(1.0, 2.0, 3.0)
v = vector(4.0, 5.0, 6.0)

assert math.isclose(u.unit().magnitude(), 1.0)
assert math.isclose(v.unit().magnitude(), 1.0)

assert u.dot(v) == 32.0
assert v.dot(u) == 32.0

print("PASS")
