import pickle

try:
    with open('F.pickle', 'w') as F:
        with open('the.serialisation1', 'wb') as f:
            pickle.dump(F, f, pickle.HIGHEST_PROTOCOL)
except Exception:
    print("serialisation error")

try:
    with open('the.serialisation2', 'wb') as f:
        pickle.dump(range, f, pickle.HIGHEST_PROTOCOL)
except Exception:
    print("serialisation error")

print()

try:
    with open('the.serialisation3', 'wb') as f:
        pickle.dump(print, f, pickle.HIGHEST_PROTOCOL)
except Exception:
    print("serialisation error")

import collections
try:
    with open('the.serialisation4', 'wb') as f:
        pickle.dump(collections.deque, f, pickle.HIGHEST_PROTOCOL)
except Exception:
    print("serialisation error")

class Zebra():
    def __init__(self, extra):
        self.additional_information = extra
    def information(self):
        return self.name, self.age, self.additional_information

try:
    with open('the.serialisation5', 'wb') as f:
        pickle.dump(Zebra, f, pickle.HIGHEST_PROTOCOL)
    #print(pickle.dumps(Zebra))
except Exception:
    print("serialisation error")

def through(a):
    if type(a) == int:
        return a**(5*a)
    return 0
try:
    with open('the.serialisation6', 'wb') as f:
        pickle.dump(through, f, pickle.HIGHEST_PROTOCOL)
    #print(pickle.dumps(through))
except Exception:
    print("serialisation error")
