from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
x =[[181,80,44],[177,70,43],[160,60,30],[154,54,37],
	[166,65,40],[190,90,47],[175,64,39],[177,60,43],
	[171,57,44],[191,85,42],[165,55,40]]
y= ['male','female','female','female','female','male',
	'male','female','male','female','male']

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf = clf.fit(x,y)
prediction = clf.predict([[0,0,0]])
print(prediction)