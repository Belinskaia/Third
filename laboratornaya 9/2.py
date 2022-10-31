class BinTree:
    def __init__ (self, value, left = None, right = None):
        self.start = None
        self.lenght = 0
        self.left, self.right = left, right
    def __iter__(self):
        for node in self.left:
            yield node.value
        yield self.value
        for node in self.right:
            yield node.value
