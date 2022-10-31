import os
import re
class TextLoader:
    def __init__(self, ad):
        self.ad = ad
        self.files = os.listdir(ad)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):
        a = open(self.ad + '/' + self.files[item])
        for i in a:
            i.lower()
            re.sub(r'[^\w\s]', '', i)
        return print(a[8])


out = TextLoader('sample')
print (len(out))
print(out[2])
