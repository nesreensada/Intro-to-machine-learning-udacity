#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train , labels_test = train_test_split(features,\
    labels, random_state=42, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, precision_score
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)
predicated = clf.predict(features_test)
print 'precision score' ,precision_score(labels_test , predicated)
 
print 'recall score', recall_score(labels_test , predicated)
for index,feature in enumerate(features_test):
    print feature, clf.predict([feature]),'true value is:',labels_test[index]

