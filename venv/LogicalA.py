"""import numpy as np
#1.
input1 = np.array([0,0])
input2 = np.array([0,1])
input3 = np.array([1,0])
input4 = np.array([1,1])


theta = 1
#2. create precepton (activation function)
def activation(s):
    if s>= theta:
        return 1
    else:
        return 0



#3. create sumation function
#x is input and w is weight
def sumation(x,w):
     s= np.dot(x,w)
     y = activation(s)
     return y #output


#4.Decide weights
weightsAnd = np.array([0.5,0.5])

output1 = sumation(input1,weightsAnd)
output2 = sumation(input2,weightsAnd)
output3 = sumation(input3,weightsAnd)
output4 = sumation(input4,weightsAnd)
print(output1)
print(output2)
print(output3)
print(output4)
"""
import numpy as np
class Preceptron:
    theta = 1
    def __init__(self,inputs,weights):

       self.inputs = inputs    #self.inputs -->  objects
       self.weights = weights

    def activation(self,s):
        if s >= Preceptron.theta:
            return 1
        else:
            return 0

    def summation(self):
        s =np.dot(self.inputs, self.weights)
        y = self.activation(s)
        return y


input1 = np.array([0,0])
input2 = np.array([0,1])
input3 = np.array([1,0])
input4 = np.array([1,1])


weights = np.array([1,1])

#object construction statement

neuron = Preceptron(input4,weights)
output = neuron.summation()
print(output)




