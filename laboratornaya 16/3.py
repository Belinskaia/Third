import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import math

fig = plt.subplots()
y = lambda x: np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
x = np.linspace(0, 16, 10)
plt.plot(x, y(x))

#1
b1 = math.sin(1/5)*math.exp(1/10)+5*math.exp(-1/2)
b2 = math.sin(15/5)*math.exp(15/10)+5*math.exp(-15/2) 
b = np.array([[b1],[b2]])
A = np.array([[1,1],[1,15]])
w = linalg.solve(A,b)
print(w)
f = lambda x: w[0]+w[1]*x
plt.plot(x, f(x))

#2
b3 = math.sin(8/5)*math.exp(8/10)+5*math.exp(-8/2)
b = np.array([[b1],[b2],[b3]])
A = np.array([[1,1,1],[1,15,225],[1,8,64]])
w = linalg.solve(A,b)
print(w)
d = lambda x: w[0]+w[1]*x+w[2]*x**2
plt.plot(x, d(x))

#3
b3 = math.sin(4/5)*math.exp(4/10)+5*math.exp(-4/2)
b4 = math.sin(10/5)*math.exp(10/10)+5*math.exp(-10/2)
b = np.array([[b1],[b2],[b3],[b4]])
A = np.array([[1,1,1,1],[1,15,225,15**3],[1,4,16,64],[1,10,100,1000]])
w = linalg.solve(A,b)
print(w)
t = lambda x: w[0]+w[1]*x+w[2]*x*x+w[3]*x*x*x
plt.plot(x, t(x))

plt.show()
