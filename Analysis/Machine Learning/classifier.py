# classifier.py

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
# importing classifiers
from sklearn import tree  # decision tree
from sklearn.neighbors import KNeighborsClassifier  # nearest neighbors
from sklearn import svm

classifiers = [tree.DecisionTreeClassifier, KNeighborsClassifier, svm.SVC]



#          DATA SECTION
iris = load_iris()

# raw data
X = iris.data
Y = iris.target




# randomly split to test, train segments
split_ratio = .2
features, test_features, labels, test_labels = train_test_split(X, Y, test_size=split_ratio)


# testing all the models
messages = []
classy = {}  # save the classifiers we made!
for classifier in classifiers:
    clf = classifier()
    clf.fit(features, labels)
    predictions = clf.predict(test_features)
    accuracy = accuracy_score(test_labels, predictions)
    classy[classifier.__name__] = clf
    message = classifier.__name__ + " accuracy: "
    messages.append([accuracy, message])

messages.sort(key=lambda model: model[0], reverse=True)
for message in messages:
    print(message[1] + str(message[0]))
