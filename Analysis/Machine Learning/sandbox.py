# sandbox.py

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()
test_data_indices = [2, 52, 102]

train_target = np.delete(iris.target, test_data_indices)
train_data = np.delete(iris.data, test_data_indices, axis=0)

test_target = iris.target[test_data_indices]
test_data = iris.data[test_data_indices]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print clf.predict(test_data)
print test_target
