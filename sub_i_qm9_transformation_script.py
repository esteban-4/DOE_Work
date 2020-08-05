import os
import sys
import cdi_file_operations
import cdi_dirac_data_uploader
import create_upload_list
import getdiraclfns

def main():
	debug = False
	se_path="/pic/projects/ccsdiit/se"
	#sbatch_lfn = sys.argv[1]
	info = getdiraclfns.getJobInfo()
	sbatch_lfn = info["Value"]["InputData"]
	print("Currently executing sbatch file at:	%s" %(sbatch_lfn))
	touch DISABLE_WATCHDOG_CPU_WALLCLOCK_CHECK
	head_tail = os.path.split(sbatch_lfn)
	destination = os.path.join(se_path, head_tail[0][1:])
	sbatch_file = head_tail[1]
	print("	Results will be saved to:		%s" %(destination))
	os.system("chmod +x input.sbatch")
	os.system("./input.sbatch"  + " > " + destination + os.sep + "out.nwo") #sbatch.input file will be executed
	#Upload files to DIRAC (all files in the directory)
	upload_list=create_upload_list.crawl_folder_and_get_list(destination,[])
	#print("Upload list: %s" %(upload_list))
	## Get default DIRAC Settings ##
	diracVar = cdi_dirac_data_uploader.getDiracConfigSettings()
	tuple_list = []
	metadata_list = {}
	directory_list = {}
	ancestry_list = []
	ancestry_dict = {}
	for up_list in upload_list:
	       lfn = up_list.replace(se_path,"")
	       print("lfn is %s" %(lfn))
	       pfn = up_list
	       print("pfn is %s" %(pfn))
	       physicalFileLocation = pfn
	       fileprops = cdi_file_operations.getFileProperties(physicalFileLocation)
	       tuple_list.append((lfn, physicalFileLocation, fileprops["size"], diracVar["SE"], fileprops["guid"], fileprops["checksum"] ))
	       if ".nwo" in up_list:
		       ####################
		       # Add Metadata #
		       ####################
		       metadata_list[lfn] = {"DataExt": "nwo"}
	if debug:
	       print("Tuple List to register image files: %s" %(tuple_list))
	       print("Metadata List: %s" %(metadata_list))
	if not debug:
	       cdi_file_operations.registerfile_eg(tuple_list)
	       cdi_dirac_data_uploader.add_dirac_metadata_bulk(metadata_list)
