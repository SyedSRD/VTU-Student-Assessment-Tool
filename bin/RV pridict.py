from sklearn import preprocessing, cross_validation,svm
import pandas as pd
import numpy as np


df=pd.read_csv('E:\\VTUBroadSpec\\bin\\rv_data.csv')
X = np.array(df.drop(['result'],1))
y= np.array(df['result'])

X_train, X_test,y_train, y_test = cross_validation.train_test_split(X,y,test_size = 0.2)

clf=svm.SVC()

clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)

exmp =np.array([1,0,2.3,3])
exmp =exmp.reshape(1 ,-1)

prediction = clf.predict(exmp)

print(prediction)
print(accuracy)

