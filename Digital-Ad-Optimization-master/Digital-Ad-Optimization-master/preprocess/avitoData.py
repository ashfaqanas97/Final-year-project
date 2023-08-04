import os
import sys
import sqlite3
import pandas as pd

from utils import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')

class AvitoData:

	def __init__(self):

		self.sampleDir = os.path.join(DATA_DIR,"sample1M.csv")
		self.dataset = self.loadData(self.sampleDir)
		# Only include certain features for training 
		self.featureNames = ['position','hist_ctr','month','day','weekday','is_query','ads_shown','user_clicks','user_impressions','is_user_logged_on']


	def loadData(self, filename):
		return pd.read_csv(filename)


	def prepareData(self):

		self.dataset['search_date'] = self.dataset['search_date'].map(lambda x:getDateTime(x))
		self.dataset['month'] = self.dataset['search_date'].map(lambda x: x.month)
		self.dataset['day'] = self.dataset['search_date'].map(lambda x: x.day)
		self.dataset['weekday'] = self.dataset['search_date'].map(lambda x: x.weekday())
		self.dataset['hour'] = self.dataset['search_date'].map(lambda x: x.hour)
		self.dataset['is_query'] = self.dataset['search_query'].map(lambda x: 1 if str(x) != 'nan' else 0 )
		self.dataset['ads_shown'] = self.dataset.groupby('search_id')['ad_id'].transform("count")

		self.dataset = self.dataset

	def splitData(self):
		'''
		Splits the data into training and test sets
		Parameters
		'''
		test_start_date = '2015-05-12'
		test_data = self.dataset[self.dataset['search_date'] > '2015-05-12']
		train_data = self.dataset[self.dataset['search_date'] <= '2015-05-12']

		test_sorted = test_data.sort_values(['user_id','search_date'], ascending=[True,True])
		user_last_sessions = test_sorted.drop_duplicates(subset='user_id', keep='last')

		test = self.dataset[self.dataset['search_id'].isin(user_last_sessions['search_id'])]
		train = self.dataset[~self.dataset['search_id'].isin(user_last_sessions['search_id'])]
		X_train, X_test = self.generateUserFeatures(train=train, test=test)

		# Use rows only with labels
		X_train = X_train[X_train['object_type'] == 3]
		X_test = X_test[X_test['object_type'] == 3]

		y_train = X_train['is_click']
		y_test = X_test['is_click']

		X_train = X_train[self.featureNames]
		X_test = X_test[self.featureNames]

		return X_train, y_train, X_test, y_test

	def generateUserFeatures(self, train, test):
		'''
		Generates user level features using training set only. Needs to be performed after splitting the data.
		If user is found in test data, fill in appropriate values.
		Parameters
		----------
		train (DataFrame): The training data.
		test (DataFrame): The test data.
		'''
		train['user_clicks'] = train.groupby('user_id')['is_click'].transform("sum")
		train['user_impressions'] = train.groupby('user_id')['is_click'].transform("size")

		test = test.assign(user_clicks = test['user_id'].map(train.groupby('user_id')['is_click'].sum()).fillna(0).astype(int))
		test = test.assign(user_impressions = test['user_id'].map(train.groupby('user_id')['is_click'].size()).fillna(0).astype(int))
		return train, test

