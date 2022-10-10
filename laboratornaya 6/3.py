class Student:
    def __init__(self, S, N, P, D):
        self.Surname = S
        self.Name = N
        self.Patronymic = P
        self.Document = D

    def __hash__(self):
        return hash(self.Document)

    def __eq__(self, other):
        return self.Document == other.Document

s = Student('ghjh', 'jghkjh', 'jkhjh', '989gjk')
f = Student('ghjh', 'jghkjh', 'jkhjh', '98988gjk')
g = Student('gvfhjrfghghdgh', 'jghkjh', 'jkhjh', '989gjk')
print(set([g,s,f]))
