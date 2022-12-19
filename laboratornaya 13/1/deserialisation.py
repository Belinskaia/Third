import pickle

try:
    with open('the.serialisation2', 'rb') as f:
        ran = pickle.load(f)
    for i in ran(10):
        print(i, end = ' ')
except Exception:
    print("deserialisation error")

print()

try:
    with open('the.serialisation3', 'rb') as f:
        prin = pickle.load(f)
    prin(8)
except Exception:
    print("deserialisation error")

try:
    with open('the.serialisation4', 'rb') as f:
        D = pickle.load(f)
    print(D)
except Exception:
    print("deserialisation error")

try:
    with open('the.serialisation5', 'rb') as f:
        CS = pickle.load(f)
    print(CS)
except Exception:
    print("deserialisation error")

try:
    with open('the.serialisation6', 'rb') as f:
        sdl = pickle.load(f)
    print(sdl)
except Exception:
    print("deserialisation error")
    
