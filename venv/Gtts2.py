from sklearn.datasets import load_iris
from sklearn import tree


#lets create our dataset

irisData = load_iris()
print("<<----Iris Data------>>")
print()

print("<<<<IRIS DATASET FEATURES>>>")
print(irisData.data)
print()

print("<<<<IRIS DATA SET LABELS>>>>")
print(irisData.target)
print()

print("")