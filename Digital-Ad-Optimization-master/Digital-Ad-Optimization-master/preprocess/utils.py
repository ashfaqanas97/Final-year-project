import datetime

def getDateTime(str_date):
	'''
	Converts string date to a date time object.
	Parameters
	----------
	str_date (String): A date string
	Returns
	-------
	Datetime object

	'''
	if len(str_date) == 0:
	    return 'None'
	else:
	    dt_format = "%Y-%m-%d %H:%M:%S.%f"
	    return datetime.datetime.strptime(str_date, dt_format)