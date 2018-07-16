from sklearn.neural_network import MLPClassifier
import numpy as np

x =[(np.random.rand(36).reshape(12,3)).tolist()]

y= ['male','female','female','female','female','male',
	'male','female','male','female','male','female']
clf = MLPClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[0,0,0]])
print(prediction)