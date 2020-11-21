# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:16:33 2019

@author: Talha Bilal
"""

import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display
#matplotlib inline

import pandas as pd
import numpy as np
import time
from PIL import Image

from skimage.feature import hog
from skimage.color import rgb2grey

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import roc_curve, auc
import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import svm
dataset_url = 'E:\\DIPA_Brain_DataSet\\Orignal\\Dataset_complete.csv'
data = pd.read_csv(dataset_url,sep=',', header=None);
#print (data.head())
y = data.loc[:,0];
x = data.loc[:,1:561];
ss = StandardScaler()
# run this on our feature matrix
bees_stand = ss.fit_transform(x)

pca = PCA(n_components=500)
# use fit_transform to run PCA on our standardized matrix
x = ss.fit_transform(bees_stand)

X_train, X_test, y_train, y_test = train_test_split(x, y,test_size=0.3);
#print("\nX_train:\n")
#print(X_train.head())
#print(X_train.shape)

#print("\nX_test:\n")
#print(X_test.head())
#print(X_test.shape)
#svclassifier = svm.SVC(kernel='linear') 
svclassifier = KNeighborsClassifier(3)
#svclassifier = MLPClassifier(alpha=1, max_iter=1000) 
start = time.time()
svclassifier.fit(X_train, y_train)
stop = time.time()
print(f"Training time: {stop - start}s")
y_pred = svclassifier.predict(X_test)
array = confusion_matrix(y_test,y_pred);   
df_cm = pd.DataFrame(array, range(3),range(3))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size
plt.show()
#print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
#dataset_url1 = 'C:/Users/Talha Bilal/Desktop/test.csv'
#data1 = pd.read_csv(dataset_url1,sep=',', header=None)
#z=data1.loc[:,:];
#y_pred1 = svclassifier.predict(z);
#print(y_pred1);