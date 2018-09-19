#X = [[ coursor_x, coursor_y, 
#       bttn_topleft_x, btton_topleft_y, 
#       bttn_bottomright_x, bttn_bottomright_y,
#       is_mouse_clicked ], ...]

ax = 0
ay = 0
bux = 2
buy = 1
bdx = 3
bdy = 2

def gen():
    tab = []
    ulx = 3
    uly = 1
    drx = 8
    dry = 10
    for x in range(10):
        for y in range(10):
            for ulx in range(10):
                for uly in range(10):
                    for drx in range(ulx, 10):
                        for dry in range(uly, 10):
                            tab.append([x,y,ulx,uly,drx,dry,1])
                            tab.append([x,y,ulx,uly,drx,dry,0])
    return tab

def validate(t):
    tab = []
    for ax, ay, bux, buy, bdx, bdy, c in t:
        tab.append( c == 1\
            and ax >= bux\
            and ax <= bdx\
            and ay >= buy\
            and ay <= bdy )
    return tab

X = gen()
Y = validate(X)

print(len(X))

from sklearn import tree
clf = tree.DecisionTreeClassifier()


clf = clf.fit(X, Y)
prediction = clf.predict([[1,1, 0,0,1,3,1], [0,0, 0,0,1,3,1]])

print(prediction)



