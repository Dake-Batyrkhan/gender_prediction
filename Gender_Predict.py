
from sklearn import tree

X = [[181, 80, 44], [177, 70, 39], [160, 60, 38], [166, 65, 40], [182, 73, 43], [175, 77, 41], [172, 57, 41], [168, 88, 39], [158, 68, 35], [160, 70, 39]]

Y = ['male', 'female', 'female' , 'female', 'male', 'male', 'male', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([])

print prediction