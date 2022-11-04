import os
import re
class TextLoader:
    def __init__(self, ad):
        self.ad = ad
        self.files = os.listdir(self.ad)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item): # аналог
        with open(self.ad + '/' + self.files[item]) as folder:
            a = folder.read().lower()
        return re.sub(r'[^\w\s]', '', a)

    def __iter__(self): # итератор, делающий то же, что и getitem
        for i in self.files:
            with open(self.ad + '/' + i) as folder:
                a = folder.read().lower()
                yield re.sub(r'[^\w\s]', '', a)

out = TextLoader('C:/Users/Didi/Downloads/sample')
print(len(out))
print(out[2])
for i in out:
    print(i)
    
