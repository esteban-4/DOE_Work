#!/usr/bin/env python
import DIRAC
from pprint import pprint
from DIRAC.Core.Base import Script

Script.parseCommandLine(ignoreErrors=True)
from DIRAC.Resources.Catalog.FileCatalog import FileCatalog
from DIRAC.Core.DISET.RPCClient import RPCClient
from DIRAC.DataManagementSystem.Client.DataManager import DataManager

##
from DIRAC.Core.DISET.RPCClient import RPCClient
from DIRAC.RequestManagementSystem.Client.Request import Request
from DIRAC.RequestManagementSystem.Client.Operation import Operation
from DIRAC.RequestManagementSystem.Client.File import File
from DIRAC.RequestManagementSystem.Client.ReqClient import ReqClient

from DIRAC import S_OK, S_ERROR, gLogger, gConfig
from DIRAC.DataManagementSystem.Client.DataManager import DataManager
from DIRAC.Core.Utilities.Adler import fileAdler, compareAdler
from DIRAC.Core.Utilities.File import makeGuid, getSize
from DIRAC.Core.Utilities.ReturnValues import returnSingleResult

import class_upload_files_dirac
import subprocess
import pdb

# Get list of new files
add_files = class_upload_files_dirac.add_files()
datestamp = '2020-07-16 08:30:20'
baseDirectory = '/../python_scripts'
pdb.set_trace()
file_list = add_files.list_directory(baseDirectory, datestamp)
print ('There are a total of %s files that were updated after %s' %(len(file_list), datestamp))


# Upload the new files
add_files.adding_file_list(file_list)
subprocess.call(['sh', './upload_script.sh'])
