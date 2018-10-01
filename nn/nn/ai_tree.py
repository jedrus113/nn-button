from sklearn import tree
from sklearn.externals import joblib

clf = joblib.load('new_ai.pkl')

def predict(x=[0],y=[0], bx1=[0], by1=[0], bx2=[0], by2=[0]):
    p_tab = []
    x = int(x[0])
    y = int(y[0])

    for i in range(len(bx1)):
        tab = [x,y]
        tab.append(int(bx1[i]))
        tab.append(int(by1[i]))
        tab.append(int(bx2[i]))
        tab.append(int(by2[i]))
        p_tab.append(tab)
    return clf.predict(p_tab)

