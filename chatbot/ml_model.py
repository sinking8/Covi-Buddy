#RANDOM FOREST 
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

class Mlmodel:
	y_train_symp = []
	y_train =[]
	y_dict = {}
	classifier= RandomForestClassifier(n_estimators= 10, criterion="entropy")

	def __init__(self):
		curr_dir = os.getcwd()+"\\chatbot\\Dataset"

		train_data = pd.DataFrame(pd.read_csv(curr_dir+"\\training.csv"))
		self.y_train_symp = train_data.columns
		X_train= train_data.drop("prognosis",axis=1).values
		self.y_train = train_data['prognosis']

		test_data = pd.DataFrame(pd.read_csv(curr_dir+'\\testing.csv'))
		X_test = test_data.drop("prognosis",axis=1).values
		y_test = test_data['prognosis']

		label_encoder = LabelEncoder()
		y_train_unique = self.y_train.unique()
		y_train_unique_encoded = label_encoder.fit_transform(y_train_unique)

		for i in range(len(y_train_unique)):
			self.y_dict[y_train_unique_encoded[i]] = y_train_unique[i] 

		##Label Encoding train_Y
		le = label_encoder.fit(self.y_train)
		y_train_encoded = le.transform(self.y_train)
		y_train_encoded = np.ravel(y_train_encoded)
		  
		self.classifier.fit(X_train,y_train_encoded) 

	def return_symp_names(self):
		return self.y_train_symp

	def return_symp_dict(self):
		return(self.y_dict)

	def test_model(self,test):

		if(len(np.unique(test))==1):
			return "no disease"

		return(self.y_dict[self.classifier.predict(test)[0]])  
