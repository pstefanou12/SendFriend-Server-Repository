import os

def symlink_files(file, location): 
	'''
	This function will symlink files from one location to another. For this script, 
	.service files will be symlinked to the location where systemctl files are 
	located on Ubuntu.
	Inputs: file - a file with the path that will be symlinked; location - 
	the location/directory with the path that the file will be symliked to
	Outputs: symlinks files, but does not return anything
	'''

	current = os.getcwd() #get path for the current location of the directory

	file_path = os.path.join(current, file)

	os.symlink(file_path, location)