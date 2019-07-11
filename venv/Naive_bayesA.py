from sklearn.naive_bayes import GaussianNB
FEATURES =  [
              [100, 110],
              [120, 150],
              [150, 200],
              [180, 220],
              [1000, 800],
              [1200, 1200],
              [1500, 1400],
              [2000, 1800]
           ]

LABELS = [0,0,0,0,1,1,1,1]
TARGET_NAMES = ["Bike","Car"]
#create model
model = GaussianNB()
#train the model with datasets
#it will also optimize the data for us!
model.fit(FEATURES,LABELS)

#check your model for prediction

sampleInput = [1990,1989]
predictedClass= model.predict([sampleInput])

print(">>Predicted vehicle is :-",predictedClass)
print(">>Predicted vehicle is :-",predictedClass[0])
print(">>predicted vehicle is :-",TARGET_NAMES[predictedClass[0]])