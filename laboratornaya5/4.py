class Animal():
    def __init__(self, n, a, extra):
        self.name = n
        self.age = a
        self.additional_information = extra


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
        return self.name, self.age, self.additional_information


class Cetaceous(Mammals):
    pass


class Dolphin(Cetaceous):
    def information(self):
        return self.name, self.age, self.additional_information


class Cheiroptera(Mammals):
    pass


class Wings():
    _amount = None
    def fly(self):
        print("Взмахнуть всеми крыльями сразу")



class Webbed(Wings):
    def _init_(self):
        self.amount = 2


class Feather(Wings):
    def _init_(self):
        self.amount = 2


class Bats(Cheiroptera, Webbed):
    pass


class Avifauna(Chordates, Feather):
    pass


class Arthropoda(Multicellular):
    pass


class Inserts(Arthropoda, Wings):
    def _init_(self, q):
        self.name = q