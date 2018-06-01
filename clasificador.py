import sklearn 
from sklearn import tree
import time 


label=[0,1,2,] ###  0: mala, 1:regular 2:buena  #### 
features=[[2.7,3.1],[7.3,5.5],[9.3,8.9]] #matriz de calificaciones, basado en imdb y metacritic
clf= tree.DecisionTreeClassifier()
clf = clf.fit(features,label)#entrenamiento: relaciona matris de caracteristicas con las etiquetas
print(clf.predict([[6.4,5]])) #clf.predict realiza la predicción de un nuevo elemento
time.sleep(30)
