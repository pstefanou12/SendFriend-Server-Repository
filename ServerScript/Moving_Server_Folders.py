import shutil
import os

def moving_server_files(filename, directory): 
	'''
	This function moves files from the where the go get command 
	places the retrieved/downloaded files 
	and places them in the correct created directory. 
	Inputs: filename - string, the name of the file that has to be moved; directory - string, 
	the name of the directory that it has to be moved to
	Outputs: None --> returns nothing
	'''
	source = os.environ['GOPATH']
	
	desination = os.getcwd() #get the current directory path, because it has the final location of the file

	files = os.listdir(source) #represent all the files in the directory as a list

	for file in files: 
		if file == filename: #iterate through the files and if the given file is in the directory, move it to a local directory
			shutil.move(os.path.join(source, file), os.path.join(destination, directory))




