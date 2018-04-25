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
	
	desination = os.getcwd() #get the current directory path, because it has the final location of the file

	path = os.join(source, 'github.com/SendFriend/stellar-backend/' + server)
	print("PATH:")
	print(path)
	files = os.listdir(source) #represent all the files in the directory as a list

	if filename in files: #iterate through the files and if the given file is in the directory, move it to a local directory
			shutil.move(os.path.join(source, filename), os.path.join(destination, directory))
	else: 
		print("The file you asked for is not the directory of interest.")




