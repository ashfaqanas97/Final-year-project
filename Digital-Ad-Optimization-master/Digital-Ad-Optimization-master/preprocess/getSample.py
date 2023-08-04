import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')

def sampleData(filename):
	'''
	Connects to database and samples 1M rows,
	saves sample as csv file
	'''
	conn = sqlite3.connect(filename)

	conn.execute('CREATE TABLE SAMPLE AS SELECT * FROM trainSearchStream JOIN SearchInfo ON trainSearchStream.SearchID = SearchInfo.SearchID')

	conn.execute('CREATE TABLE SAMPLE_1M AS SELECT * FROM (SELECT * FROM SAMPLE ORDER BY sample.UserID ASC LIMIT 1000000) AS subsample LEFT JOIN AdsInfo ON subsample.AdID = AdsInfo.AdID')

	data = conn.execute('SELECT * FROM SAMPLE_1M')

	df = pd.DataFrame(data.fetchall())

	df.drop([6,15], axis=1,inplace=True)

	df.columns = ['search_id','ad_id','position','object_type','hist_ctr','is_click','search_date','id_id','user_id','is_user_logged_on','search_query','location_id_search','category_id_search_filter','search_parameters','location_geo_target',
                 'category_id_ad','ad_parameters','price','title','is_context']

	df.to_csv(DATA_DIR + os.sep + 'sample1M.csv',encoding='utf-8')