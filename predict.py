#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.externals import joblib
from tabulate import tabulate # pretty table
from nltk import word_tokenize          
from nltk.stem.wordnet import WordNetLemmatizer 
import string
import re


# Tokenizer that does stemming and strips ponctuation
def tokenize(text):
	#text = text.translate(str.maketrans('','',string.punctuation))
	text = re.sub(r'\W+', ' ', text)
	tokens = word_tokenize(text)
	lemas = []
	for item in tokens:
		lemas.append(WordNetLemmatizer().lemmatize(item))
	return lemas
        
# Command line arguments
save = sys.argv[1]
file_dir = sys.argv[2]

if __name__ == "__main__":
	# Load trained model
	print("Loading model...")
	clf = joblib.load(save) 
	print("Model loaded!")
	print("\nModel Parameters:")
	print(clf.named_steps['clf'].get_params())
	# Read file into string and run analysis
	with open(file_dir, 'r') as myfile:
		data=myfile.read().replace('\n', '')
		# Run data through model
		predicted = clf.predict([data])
		#print(predicted)
		certainty = clf.decision_function([data])
	
	# Is it bonkers?
	if predicted[0]:
		verdict = "Not too nuts!"
	else: 
		verdict = "Bonkers!" 

	print("\nInput classified as:")
	print(tabulate([["Verdict", verdict], ["Certainty", float(certainty)]], 
		tablefmt="html"))
