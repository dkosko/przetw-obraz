import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
import sklearn.svm
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, plot_confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from random import randint
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score
from sklearn import preprocessing
from sklearn import utils
from matplotlib.pyplot import imread
from PIL import Image 
import numpy as np
import os




def learn_digits():
    def load_data():
        data = np.ones((1016,16384))
        for d in digits:
            filenames = os.listdir('digits/' + str(d))
            for name in filenames:
                img = Image.open("digits/" + str(d) + "/" + name) # This returns an image object   
                img = np.asarray(img) # convert it to ndarray
                img = img.reshape(-1, img.size)
                data[d,:] = img
        return data   

    digits = [0,1,2,3,4,5,6,7,8,9]
    data = load_data()
    print(data)

if __name__ == '__main__':
    learn_digits()
