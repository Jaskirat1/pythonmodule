from sklearn.datasets import load_iris
from sklearn import tree
#1. lets create a data set
irisData = load_iris()
print(">>IRIS DATA SET ")
print(irisData)
print()


print(">>Iris data set features")
print(irisData.data)

print(">>Lables")
print(irisData.target)

print(">>Lable names")
print(irisData.target_names)

#2. lets create decision tree ML model
model = tree.DecisionTreeClassifier()

#3.train the model|

model.fit(irisData.data,irisData.target)
#4.test the model for any inputt data
inputSample = [5.5,2.5,4.0,1.3]

predicatedClass = model.predict([inputSample])
print("Type of flower is :-",predicatedClass)
print(("Type of flower is :-",predicatedClass[0]))
print("Type of flower is :-",irisData.target_names[predicatedClass[0]])


