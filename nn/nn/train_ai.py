#!/bin/python3

import numpy as np
import random

def gen_tab():
    tab = []
    max_size = 1000
    for _ in range(10000000):
        x = random.randint(0, max_size)
        y = random.randint(0, max_size)
        
        bx1 = random.randint(0, max_size-50)
        by1 = random.randint(0, max_size-50)
        
        bx2 = random.randint(bx1+50, max_size)
        by2 = random.randint(by1+50, max_size)
        tab.append([x,y,bx1,by1,bx2,by2])
    return tab

def validate(t):
    tab = []
    for ax, ay, bux, buy, bdx, bdy in t:
        tab.append(ax >= bux\
            and ax <= bdx\
            and ay >= buy\
            and ay <= bdy )
    return tab

X = np.random.randint(0, 1000, (100000,6))
Y = validate(X)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

from sklearn.externals import joblib
joblib.dump(clf, 'new_ai.pkl')
