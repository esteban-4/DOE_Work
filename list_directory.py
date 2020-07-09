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


#*******************************
# import os
# import sys
# import time
# from datetime import datetime


# user_datetime = datetime.strptime('2020-06-18 08:30:20', '%Y-%m-%d %H:%M:%S')

# req_format=datetime.strftime(user_datetime ,'%a %b %d %H:%M:%S %Y')
# dir_list=[]
# directory_path = os.getcwd()
# for root, _, filenames in os.walk(directory_path):
# 	for filename in filenames:
# 		file_path   = root + '/' + filename
# 		modified    = os.path.getmtime(file_path)
# 		created     = os.path.getctime(file_path)	
# 		local_time = time.ctime(modified)
# 		print("File: %s" % file_path 
# 		+ "    Created:       %s" % time.ctime(created) + "    Last modified: %s" % time.ctime(modified))
		#****************************
		# if local_time >= req_format:
		# 	print(b)

		# 	dir_list.append([filename])
		# print(dir_list)


			# created     = os.path.getctime(file_path)
            # print ("File: %s" % file_path)
            # print ("    Created:       %s" % time.ctime(created))
            # print ("    Last modified: %s" % time.ctime(modified))


# print(type(req_format))
# print(type(local_time))
# print (local_time)



# 	while i >= user_datetime:
# 			print 


# import os
# print(os.path.dirname(os.path.realpath(__file__)))	


# import os
# d = '.'
# subdirs = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
# print(subdirs)

# ctime = os.path.getctime('C:/Users/espi524/Documents/python')
# localtime = time.ctime(ctime)
# print (localtime)

# from datetime import datetime

# print (datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p"))

# timestamp = '"2020-06-22 03:28:46"'
# path = '.'
# files = []
# find = subprocess.Popen('find ' + path + "-newermt" + timestamp, shell=True, 
# stdout=subprocess.PIPE)
# for line in find.stdout:
#    files.append(line.decode('UTF-8').strip())
# print(files)

# find ./ -newermt "2020-06-22"
# print (os.getcwd())

# find /user -newermt "Feb 1"

# export newerthan = "2020-22-06 01:05:00"
# find . -newermt "$newerthan"

# path = os.getcwd()
# user_time = 
# touch /tmp/mark.start -d user_time
# find path -newer /tmp/mark.start


# import os
# import subprocess
# timestamp = '"2020-06-22 03:28:46"'
# path = os.getcwd()
# files = []
# find = subprocess.Popen('find ' + path + ' -newer ' + timestamp, shell=True, 
# stdout=subprocess.PIPE)
# for line in find.stdout:
#    files.append(line.decode('UTF-8').strip())
# print(files)

