#  train.py
#  
#  Copyright 2017 Grant Garrett-Grossman <grantlycee@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This model is heavily based off of the stk-learn example for film 
# reviews

# Nevertheless, it is a notable contribution to society, a program 
# capable of discerning whether of not a text is a crackpott conspiracy

import sys # For command line arguments
from time import time # to show progress
import pprint # Pretty stuff
from tabulate import tabulate # More pretty stuff
import logging
import string # To strip ponctuation
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.externals import joblib # In order to save
from matplotlib import pyplot as plt
import numpy as np
from nltk import word_tokenize          
from nltk.stem.wordnet import WordNetLemmatizer 
import matplotlib.pyplot as plt

# Tokenizer that does stemming and strips ponctuation
def tokenize(text):
	#text = text.translate(str.maketrans('','',string.punctuation))
	text = re.sub(r'\W+', ' ', text)
	tokens = word_tokenize(text)
	lemas = []
	for item in tokens:
		lemas.append(WordNetLemmatizer().lemmatize(item))
	return lemas
		
# Plot the most important features
def plot_coefficients(classifier, feature_names, top_features=20):
	print("Generating list of most important features")
	coef = classifier.coef_.ravel()
	top_positive_coefficients = np.argsort(coef)[-top_features:]
	top_negative_coefficients = np.argsort(coef)[:top_features]
	top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
	# create plot
	print("Creating Plot...")
	plt.figure(figsize=(15, 5))
	colors = ['red' if c < 0 else 'blue' for c in coef[top_coefficients]]
	plt.bar(np.arange(2 * top_features), coef[top_coefficients], color=colors)
	feature_names = np.array(feature_names)
	plt.xticks(np.arange(1, 1 + 2 * top_features), feature_names[top_coefficients], rotation=60, ha='right')
	plt.savefig('figure.svg', bbox_inches='tight')
	plt.show()

if __name__ == "__main__":
	# NOTE: we put the following in a 'if __name__ == "__main__"' protected
	# block to be able to use a multi-core grid search that also works under
	# Windows, see: http://docs.python.org/library/multiprocessing.html#windows
	# The multiprocessing module is used as the backend of joblib.Parallel
	# that is used when n_jobs != 1 in GridSearchCV
	
	# Display progress logs on stdout
	print("Initializing...")
	# Comand line arguments
	save = sys.argv[1]
	training_directory = sys.argv[2]

	logging.basicConfig(level=logging.INFO,
		format='%(asctime)s %(levelname)s %(message)s')
	
	dataset = load_files(training_directory, shuffle=False)
	print("n_samples: %d" % len(dataset.data))
	
	# split the dataset in training and test set:
	print("Splitting the dataset in training and test set...")
	docs_train, docs_test, y_train, y_test = train_test_split(
		dataset.data, dataset.target, test_size=0.25, random_state=None)
	
	# Build a vectorizer / classifier pipeline that filters out tokens
	# that are too rare or too frequent
	# Also remove stop words
	print("Loading list of stop words...")
	with open('stopwords.txt', 'r') as f:
		words = [line.strip() for line in f]
	
	print("Stop words list loaded...")
	print("Setting up pipeline...")
	pipeline = Pipeline(
	[
		#('vect', TfidfVectorizer(stop_words=words, min_df=0.001, max_df=0.5, ngram_range=(1,1))), 
		('vect', TfidfVectorizer(tokenizer=tokenize, stop_words=words, min_df=0.001, max_df=0.5, ngram_range=(1,1))),
		('clf', LinearSVC(C=5000)),
	])
		
	print("Pipeline:", [name for name, _ in pipeline.steps])
	
	# Build a grid search to find out whether unigrams or bigrams are
	# more useful.
	# Fit the pipeline on the training set using grid search for the parameters
	print("Initializing grid search...")
	
	# uncommenting more parameters will give better exploring power but will
	# increase processing time in a combinatorial way
	parameters = {
		#'vect__ngram_range': [(1, 1), (1, 2)],
		#'vect__min_df': (0.0005, 0.001),
		#'vect__max_df': (0.25, 0.5),
		#'clf__C': (10, 15, 20),
	}
	print("Parameters:")
	pprint.pprint(parameters)
	grid_search = GridSearchCV(
		pipeline, 
		parameters, 
		n_jobs=-1,
		verbose=True)
	
	print("Training and performing grid search...\n")
	t0 = time()
	grid_search.fit(docs_train, y_train)
	print("\nDone in %0.3fs!\n" % (time() - t0))	
	
	# Print the mean and std for each candidate along with the parameter
	# settings for all the candidates explored by grid search.
	n_candidates = len(grid_search.cv_results_['params'])
	for i in range(n_candidates):
		print(i, 'params - %s; mean - %0.2f; std - %0.2f'
				 % (grid_search.cv_results_['params'][i],
					grid_search.cv_results_['mean_test_score'][i],
					grid_search.cv_results_['std_test_score'][i]))

	# Predict the outcome on the testing set and store it in a variable
	# named y_predicted
	print("\nRunning against testing set...\n")
	y_predicted = grid_search.predict(docs_test)
	
	# Print best parameters
	best_parameters = grid_search.best_estimator_.get_params()
	print("Best parameters:\n")
	for param_name in sorted(parameters.keys()):
		print("\t%s: %r" % (param_name, best_parameters[param_name]))
	
	# Save model
	print("\nSaving model to", save, "...")
	joblib.dump(grid_search.best_estimator_, save)
	print("Model Saved! \nPrepare for some awesome stats!")
	
	
	# Print the classification report
	print("\nClassification Report:")
	print(metrics.classification_report(y_test, y_predicted, 
		target_names=dataset.target_names))

	# Print and plot the confusion matrix
	print("\nConfusion Matrix:")
	cm = metrics.confusion_matrix(y_test, y_predicted)
	print(cm, "\n \n")
	#plt.matshow(cm)
	#plt.show()       
	
	# Display most important features
	n = 20
	i = 1
	a = []
	vectorizer = grid_search.best_estimator_.named_steps['vect']
	clf = grid_search.best_estimator_.named_steps['clf']
	feature_names = vectorizer.get_feature_names()
	coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
	top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
	
	print("Top 10 most important features:")
	for (coef_1, fn_1), (coef_2, fn_2) in top:
		#print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))
		a.append([i, coef_1, fn_1, coef_2, fn_2])
		i += 1
	print(tabulate(a, ["Rank", "Weight", "Bonkers", "Weight", "Fine"], tablefmt="fancy_grid"))
	#print(tabulate(a, ["Rank", "Weight", "Bonkers", "Weight", "Fine"], tablefmt="html"))
	print("Plotting...")
	plot_coefficients(clf, feature_names)
