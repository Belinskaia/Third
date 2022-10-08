class Animal():
    def __init__(self, n, a):
        self.name = n
        self.age = a


class Multicellular(Animal):
    pass


class Chordates(Multicellular):
    pass


class Mammals(Chordates):
    pass


class Oddtoed(Mammals):
    pass


class Zebra(Oddtoed):
    def information(self):
        return self.name, self.age


class Cetaceous(Mammals):
    pass


class Dolphin(Cetaceous):
    def information(self):
        return self.name, self.age


class Cheiroptera(Mammals):
    pass


class Wings:
    def movement(self, m):
        print('{}е крыло взмахнуло'.format(m + 1))


class Webbed(Wings):
    def _init_(self):
        self.amount = 2


class Feather(Wings):
    pass


class Mixin:
    def fly(self):
        for i in range(len(self.wings)):
            self.wings[i].movement(i)


class Bats(Mammals, Mixin):
    def _init_(self, name, age):
        super().__init__(name, age)
        self.wings = [Webbed() for _ in range(2)]


class Avifauna(Chordates, Mixin):
    def _init_(self, name, age):
        super().__init__(name, age)
        self.wings = [Feather() for _ in range(2)]

class Arthropoda(Multicellular):
    pass


class Insects(Arthropoda, Mixin):
    def _init_(self, name, age, q):
        super().__init__(name, age)
        self.wings = [Wings() for _ in range(q)]
