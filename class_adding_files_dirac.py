import os, glob
import time
from datetime import datetime

class add_files:
	def list_directory(user_datetime):
		dir_list=[]
		dir_list2 =[]
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
					dir_list.append('File: ' + filename + '   Path:  '  + file_path)	
					dir_list2.append(file_path)
		return dir_list2

	def adding_file_list(dirlist):

		lfn_dir = '/ccsdi/user/t/thom991/' 

		se = 'PNNL-PIC-SRM-SE'

		s = "#!/bin/bash\n"

		for my_file in dirlist:
			base_name  = os.path.basename(my_file)
			upload_lfn = os.path.join(lfn_dir, base_name)
			s += "dirac-dms-add-file %s %s %s\n" % (upload_lfn, base_name, se)
			print("dirac-dms-add-file %s %s %s\n" % (upload_lfn, base_name, se))

		with open("upload_script.sh", "w") as sf:
			sf.write(s)
a = add_files.list_directory('2020-07-12 08:30:20')			
add_files.adding_file_list(a)