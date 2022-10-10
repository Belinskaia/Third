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
    def __abs__(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z)**(0.5)
    @classmethod
    def const(cls, quar):
        A = list(map(int, quar.split(',')))
        return cls(A[0], A[1], A[2])
N = int(input())
S = 0
for i in range(N):
    v = Vector.const(input())
    if abs(v) >= S:
        S = abs(v)
        x = v.x
        y = v.y
        z = v.z
print (x, y, z)

