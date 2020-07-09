import os
import time
from datetime import datetime

user_datetime = '2020-06-18 08:30:20'

def list_directory(user_datetime):
	dir_list=[]
	date_format= '%a %b %d %H:%M:%S %Y'
	user_datetime = datetime.strptime(user_datetime ,'%Y-%m-%d %H:%M:%S')
	user_datetime=user_datetime.strftime(date_format)
	directory_path = os.getcwd()
	for root, _, filenames in os.walk(directory_path):
		for filename in filenames:
			file_path   = root + '/' + filename
			modified    = os.path.getmtime(file_path)    
			local_time = time.ctime(modified)
			if  (datetime.strptime(user_datetime ,date_format)) <= (datetime.strptime(local_time, date_format)) :
				dir_list.append('File: ' + filename + '   Path:  '  + file_path)	# print("File: %s" % file_path)

	print(dir_list)


            	

list_directory(user_datetime)
