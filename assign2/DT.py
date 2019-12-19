from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

import pandas as pd
import numpy as np

dataset=pd.read_csv("assign2Data.csv")
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,5]

le=LabelEncoder()
x=x.apply(le.fit_transform)

regressor=DecisionTreeClassifier()
regressor.fit(x.iloc[:,1:5],y)

testset=pd.read_csv("assign2Test.csv")
tx=testset.iloc[:,:]
print(tx)

tx=tx.apply(le.fit_transform)

x_in=np.array([1,1,0,0])

y_pred=regressor.predict([x_in])
print("Prediction:", y_pred)

export_graphviz(regressor, out_file ='tree.dot')

#sudo apt install graphviz
#dot -Tpng tree.dot -o tree.png
