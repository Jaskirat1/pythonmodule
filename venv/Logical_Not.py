import numpy as np
#1.
input1 = np.array([0,0])
input2 = np.array([1,1])

theta = 0
#2. create precepton (activation function)
def activation(s):
    if s>= theta:
        return 0
    else:
        return 1

#3. create sumation function
#x is input and w is weight
def sumation(x,w):
     s= np.dot(x,w)
     y = activation(s)
     return y #output

#4.Decide weights
weightsAnd = np.array([1,1])

output1 = sumation(input1,weightsAnd)
print(output1)