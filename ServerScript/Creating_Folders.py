import os 

def create_folder(directory): 
	'''
	This function generates a folder in the current directory if the folder does not alreay exist.
	Inputs: a string for the name of the directory --> in the format ('/folder_name/')
	Outputs: Error if the folder already exists, or none --> just generates a new directory
	'''
	try: 
		if not os.path.exists(directory): 
			os.makedirs(directory)
	except OSError:  
		print("Error: Creating directory. y" + directory)
