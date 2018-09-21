#import random
#import numpy as np

def gen_tab():
    tab = []
    max_size = 1000
    for _ in range(100000):
        for line in np.random.randint(0, max_size, (10,6)):
            tab.append(line)
    return tab

def validate(t):
    tab = []
    for ax, ay, bux, buy, bdx, bdy in t:
        tab.append(ax >= bux\
            and ax <= bdx\
            and ay >= buy\
            and ay <= bdy )
    return tab

#X = gen_tab()
#Y = validate(X)

from sklearn import tree
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X, Y)

from sklearn.externals import joblib
#joblib.dump(clf, 'new_ai.pkl')
clf = joblib.load('new_ai.pkl')

def predict(x=[0],y=[0], bx1=[0], by1=[0], bx2=[0], by2=[0]):
    p_tab = []
    x = int(x[0])
    y = int(y[0])

    for i in range(len(bx1)):
        tab = []
        tab.append(int(bx1[i]))
        tab.append(int(by1[i]))
        tab.append(int(bx2[i]))
        tab.append(int(by2[i]))
        p_tab.append(tab)
    return clf.predict(p_tab)

