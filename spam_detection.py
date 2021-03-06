import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split

##Step1: Load Dataset
dataframe = pd.read_csv("spam.csv")
print(dataframe.describe())

##Step2: Split in to Training and Test Data

x = dataframe["EmailText"]
y = dataframe["Label"]

#x_train,y_train = x[0:4457],y[0:4457]
#x_test,y_test = x[4457:],y[4457:]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20)

##Step3: Extract Features
cv = CountVectorizer()  
features = cv.fit_transform(x_train)

#print(features.toarray())

##Step4: Build a model

model = svm.SVC()
model.fit(features,y_train)

#Step5: Test Accuracy

features_test = cv.transform(x_test)
y_test = model.predict(features_test)
print(y_test)

print("Accuracy of the model is: ", model.score(features_test,y_test))