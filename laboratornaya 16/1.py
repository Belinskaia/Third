import numpy as np

#вектор с элементами от 12 до 42
a = np.arange(12, 43)
print (a)

#вектор из нулей длины 12, но пятый елемент единица
E5 = np.zeros(10)
E5[4] = 1
print(E5)

#матрица (3, 3), заполненая от 0 до 8
T = np.arange(0, 9)
D = T.reshape(3,3)
print(D)

#найти все положительные числа
a = np.array([1,2,0,0,4,0])
print("Индексы положительных элементов: \n", np.where(a > 0))

#умножить матрицы разных размерностей
f = np.random.random((5,3))  
v = np.random.random((3,2))  
print (f.dot(v))

#матрица (10,10) с нулями на границе и единицами внутри
R = np.zeros((10,10))
R[1:-1,1:-1] = 1
print(R)

#создать рандомный вектор и отсортировать его
h = np.random.random(5)
print(h)
h.sort()
print(h)

#эквивалент enumerate
a = np.random.random(5)
for ind, val in np.ndenumerate(a):
  print(ind, val)
  
