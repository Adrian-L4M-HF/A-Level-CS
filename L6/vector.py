"""A vector class with dunder methods, and a polar coords conversion."""
import math

class Vector():
    """Simple vector maths object."""
    def __init__(self, *coords):
        self.coords = coords

    def __len__(self):
        return len(self.coords)
    
    def check_2_dimension(self):
        """Raise ValueError if the dimension of a vector is not 2"""
        if len(self) != 2:
            raise ValueError("Incorrect no. of dimensions, should be 2")
            
    def check_dimension_with_other(self, other):
        """Raise ValueError if the dimension of two vectors are not same"""
        if len(self) != len(other):
            raise ValueError("Dimensions of both Vectors should be same")

    def __add__(self, other):
        """Add another vector, return the vector sum."""
        Vector.check_dimension_with_other(self, other)
        return Vector(*[x + y for x, y in zip(self.coords, other.coords)])

    def __sub__(self, other):
        """Subtract a vector, return the vector difference."""
        Vector.check_dimension_with_other(self, other)
        return Vector(*[x - y for x, y in zip(self.coords, other.coords)])
    
    def __eq__(self, other):
        """Return True if equal element-wise."""
        try: 
            Vector.check_dimension_with_other(self, other)
        except: 
            return None
        for x, y in zip(self.coords, other.coords):
            if x != y:
                return None
        return True                

    def __str__(self):
        """Return a string representation of the command needed to create this
        vector"""
        return f'Vector{self.coords}'
    
    def magnitude(self):
        """Return the magnitude of a vector"""
        sum_of_square_of_vectors = 0
        for i in range(0, len(self.coords)):
            sum_of_square_of_vectors += (self.coords[i])**2
        mag = math.sqrt(sum_of_square_of_vectors)
        return mag
    
    def polar(self):
        """Return polar coords for the vector, tuple(magnitude, angle)"""
        Vector.check_2_dimension(self)
        mag = Vector.magnitude(self)
        ang = math.atan2(self.coords[1],self.coords[0])
        return (mag, ang)

    def dot(self, other):
        """Returns the scalar product of both two dimensional vectors as a float."""
        Vector.check_2_dimension(self)
        Vector.check_dimension_with_other(self, other)
        V_self = Vector.magnitude(self)
        V_other = math.sqrt((other.coords[0])**2 + (other.coords[1])**2)
        dot_product = V_self * V_other
        return dot_product

"""Tests"""
A = Vector(2,5)
B = Vector(3,4)
C = Vector(2,3,3)
D = Vector(2,5)

print("Test for __add__()")
print(A.__add__(D))
print(A.__add__(B))
#print(A.__add__(C)) #should raise ValueError
print((A.__add__(B)).__add__(A.__add__(D)))
print()

print("Test for __sub__()")
print(B.__sub__(D))
print(A.__sub__(B))
#print(A.__sub__(C)) #should raise ValueError
print((B.__sub__(D)).__sub__(A.__sub__(B)))
print()

print("Test for __eq__()")
print(A.__eq__(D))
print(B.__eq__(D)) #None
print(C.__eq__(D)) #None
print()

print("Test for __str__()")
print(A)
print(B)
print(C)
print()

print("Test for magnitude()")
print(A.magnitude())
print(B.magnitude())
print(C.magnitude())
print()

print("Test for polar()")
print(B.polar())
print(D.polar())
#print(C.polar()) #should raise ValueError
print()

print("Test for dot()")
print(A.dot(B))
print(A.dot(D))
#print(D.dot(C)) #should raise ValueError
