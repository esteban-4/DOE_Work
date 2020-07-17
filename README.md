# DOE_Work
# Internship projects
# 
### Instructions how to run the class in this repo of DOE_Work
###This class was created so we could add certain files that are filtered by date to DIRAC
1) Clone the repo onto your system by doing: git clone https://github.com/esteban-4/DOE_Work.git

2) Function: list_directory(user_datetime)
  In order to run this function you need one parameter which is date and time the format should be '%Y-%m-%d %H:%M:%S'
  To call this function you have do it in the following way: add_files.list_directory('[datetime you choose]')
  To print: print(add_files.list_directory('[datetime you choose]'))
  
 3) Function: adding_file_list(dirlist)
  This function as well requires one parameter which is a list of files that will be passed from the function list_directory()
  To call this function the format is: add_files.adding_file_list()
  For the paramter you can either assign a varibale to the first function such as x = add_files.list_directory('[datetime you choose]')
  and put in "x" for the paramter or you can put "add_files.list_directory('[datetime you choose]')" inside the parameter
  
 4)To upload the files to DIRAC, once you are connected to DIRAC you run the follwoing lines:
    python class_upload_files_dirac.py
    chmod a+x upload_script.sh
    . upload_script.sh
  
  
  After that it should upload the files to the DIRAC folder.
  ******Example******
  x = add_files.list_directory('2020-07-16 08:30:20')		
  print (x)	
Output:
['File: class_upload_files_dirac.py   Path:  C:\\Users\\espi524\\Documents\\python/class_upload_files_dirac.py',
'File: upload_script.sh   Path:  C:\\Users\\espi524\\Documents\\python/upload_script.sh']


x = add_files.list_directory('2020-07-16 08:30:20')		
add_files.adding_file_list(x)
This function will not print anything out however since its just for adding the files
