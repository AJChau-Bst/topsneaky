import numpy as np
import matplotlib.pyplot as plt
import csv
import sklearn
#from sklearn.naive_bayes import GaussianNB
#from sklearn import svm
#from sklearn import tree
import random
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

roboFeats = np.array([[32.6,12.8,45.3],[18.7,22.4,19.9],[14.0,10.1,23.1],[34.2,21.9,31.5]])
kmeans = KMeans(n_clusters=4, max_iter=150, n_init=5).fit(roboFeats)


data = [[40, 40, 60], [12, 53, 11]]

print (kmeans.predict([[40, 40, 60], [12, 53, 11]]))

pca = PCA(3)
df = pca.fit_transform(data)

df.shape

label = kmeans.predict(df)


 
#plotting the results
plt.scatter(label[:,0] , label[:,1])
plt.show()