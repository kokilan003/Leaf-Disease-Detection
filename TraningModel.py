
import cv2
import matplotlib.pyplot as mt
import glob
import sys
import numpy as np
import pickle
from sklearn.neural_network import MLPClassifier
hog = cv2.HOGDescriptor()
features = []
labels=[]
for img in glob.glob("C:/Users/koki/Desktop/project/Train/green leaves/*.jpg"):
    image= cv2.imread(img)
    image=cv2.resize(image,(150, 150))
    h = hog.compute(image)
    features.append(h)
    labels.append(0)




for img in glob.glob("C:/Users/koki/Desktop/project/Train/Brown spot/*.jpg"):
    image= cv2.imread(img)
    image=cv2.resize(image,(150, 150))
    h = hog.compute(image)
    features.append(h)
    labels.append(1)



for img in glob.glob("C:/Users/koki/Desktop/project/Train/paddy blast/*.jpg"):
    image= cv2.imread(img)
    image=cv2.resize(image,(150, 150))
    h = hog.compute(image)
    features.append(h)
    labels.append(2)





for img in glob.glob("C:/Users/koki/Desktop/project/Train/bacterial blight/*.jpg"):
    image= cv2.imread(img)
    image=cv2.resize(image,(150, 150))
    h = hog.compute(image)
    features.append(h)
    labels.append(3)





fet= np.array( features )
features=[]
lb=np.array(labels)
lb=np.reshape(lb,[915, 1])
fet=np.reshape(fet,[915,124740])
print(np.shape(fet))
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(fet,lb)
pickle.dump(clf,open('neural.model', 'wb'))
