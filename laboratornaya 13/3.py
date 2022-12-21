import os
import re
import pickle

class TextLoader:
    def __init__(self, ad):
        self.ad = ad
        self.files = os.listdir(self.ad)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):  # аналог
        with open(self.ad + '/' + self.files[item]) as folder:
            a = folder.read().lower()
        return re.sub(r'[^\w\s]', '', a)

    def __iter__(self):  # итератор, делающий то же, что и getitem
        for i in self.files:
            with open(self.ad + '/' + i) as folder:
                a = folder.read().lower()
                yield re.sub(r'[^\w\s]', '', a)

    def __getstate__(self):
        state = self.__dict__.copy()
        #del state['atribute that cannot be serialized']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.files = os.listdir(self.ad)


out = TextLoader('C:/Users/Didi/Downloads/sample')
print(len(out))
print(out[2])
with open('derevce.txt', 'wb') as f:
    pickle.dump(out, f)
    out = pickle.load(f)
for i in out:
    print(i)
