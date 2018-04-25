import shutil
import os

def moving_server_files(filename, server, directory): 
	'''
	This function moves files from the where the go get command 
	places the retrieved/downloaded files 
	and places them in the correct created directory. 
	Inputs: filename - string, the name of the file that has to be moved; directory - string, 
	the name of the directory that it has to be moved to; server - the server of interest
	Outputs: None --> returns nothing
	'''
	source = os.environ['GOPATH']
	
	destination = os.getcwd() #get the current directory path, because it has the final location of the file

	path = os.path.join(source, 'src/github.com/SendFriend/stellar-backend/' + server)

	files = os.listdir(path) #represent all the files in the directory as a list

	if filename in files: #check whether the file is in the files for the server
			shutil.move(os.path.join(path, filename), os.path.join(destination, directory))
	else: 
		print("The file you asked for is not in the directory of interest.")




