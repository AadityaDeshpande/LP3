Assignment on KNN Classifier
data captured from figure given in BE_Comp Syllabus


sample:

```
classifier=KNeighborsClassifier(n_neighbors=3,p=2,weights='uniform',metric='minkowski')

classifier.fit(x,y)

x_pred=np.array([4.5,3])

```
##Outputs Blue

```
classifier=KNeighborsClassifier(n_neighbors=4,p=2,weights='distance',metric='minkowski')

classifier.fit(x,y)

#x_pred=np.array([6,6])
x_pred=np.array([4.5,3])
```

##Outputs Orange

for detailed information 
enter commands
```
$  python3

>>> help("sklearn.neighbors.KNeighborsClassifier")

>>> help("sklearn.cluster.KMeans")  for assign 4

>>> help("sklearn.linear_model.LinearRegression") for assign 1

>>> help("sklearn.tree.DecisionTreeClassifier")

```
