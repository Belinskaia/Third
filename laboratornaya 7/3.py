class Mymeta(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        y = list(attrs.keys())
        for i in range(len(y)):
            if "certain_line" in y[i]:
                if 'function' in str(attrs[y[i]]):
                    raise Exception('Unsuitable fragment in the name of function.')
                    return
        return super().__init__(name, bases, attrs)

class Proverochka(object, metaclass = Mymeta):
    def certain_line_random(self):
        print(888)
    def normal_function(self):
        print("oups")


if __name__ == '__main__':
    Q = Proverochka()
    Q.certain_line_random()
    Q.normal_function()

