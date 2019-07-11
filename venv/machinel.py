import numpy as np



X = [1,2,3,4,5]
Y = [2,4,5,4,5]


MX = np.mean(X)
MY = np.mean(Y)

print(int(MX))
print(int(MY))

for i in X:
     X1 = X-MX
print(X1)
for i in Y:
    Y1 = Y - MY
print(Y1)
print("-----------")
X2 = np.square(X1)
print(X2)
print("-----------")
Y2 = np.square(Y1)
print(Y2)
print("-------------")
Z1 = np.square(X1,Y1)
print(Z1)


