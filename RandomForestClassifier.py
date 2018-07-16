from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
x =[[181,80,44],[177,70,43],[160,60,30],[154,54,37],
	[166,65,40],[190,90,47],[175,64,39],[177,60,43],
	[171,57,44],[191,85,42],[165,55,40]]
y= ['male','female','female','female','female','male',
	'male','female','male','female','male']

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf = clf.fit(x,y)
input_height= float(input("Enter height: \n"))
input_weight= float(input("Enter weight: \n"))
input_age= float(input("Enter age: \n"))
prediction = clf.predict([[input_height,input_weight,input_age]])
print(prediction)