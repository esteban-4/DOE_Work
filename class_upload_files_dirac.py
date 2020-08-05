import os, glob
import time
from datetime import datetime


class add_files:
    def list_directory(self, directory_path, user_datetime):
        dir_list = []
        date_format = '%a %b %d %H:%M:%S %Y'
        user_datetime = datetime.strptime(user_datetime, '%Y-%m-%d %H:%M:%S')
        user_datetime = user_datetime.strftime(date_format)
        # directory_path = os.getcwd()
        for root, _, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = root + '/' + filename
                modified = os.path.getmtime(file_path)
                local_time = time.ctime(modified)
                if (datetime.strptime(user_datetime, date_format)) <= (datetime.strptime(local_time, date_format)):
                    dir_list.append(file_path)
        return dir_list

    def adding_file_list(self, dirlist):
        lfn_dir = '/ccsdi/user/e/espino/'
        se = 'PNNL-PIC-SRM-SE'
        s = "#!/bin/bash\n"
        for my_file in dirlist:
            base_name = os.path.basename(my_file)
            upload_lfn = os.path.join(lfn_dir, base_name)
            s += "dirac-dms-add-file %s %s %s\n" % (upload_lfn, my_file, se)
        with open("upload_script.sh", "w") as sf:
            sf.write(s)
