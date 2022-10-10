class Vector():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "Vector ({}; {}; {})".format(self.x, self.y, self.z)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self,other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    @classmethod
    def const(cls, quar):
        A = list(map(int, quar.split(',')))
        return cls(A[0], A[1], A[2])
A = Vector.const('1, 2, 2')
B = Vector.const('3, 4, 3')
C = A + B
print(C.x, C.y, C.z)
