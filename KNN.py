from sklearn import neighbors
import time 

#dataset
color=[0,0,0,1,1,1,1,1] #0: azul   1:rojo
pos=[[-1,2],
[0,2],
[1,2],
[1,1],
[4,1],
[4, 0],
[4,-1],
[5,-1]]#posición en el plano

n_neighbors= 4
clf=neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
clf.fit(pos,color)

new_point=[0,0]
print(clf.predict([[0,0]]))
time.sleep(30)
