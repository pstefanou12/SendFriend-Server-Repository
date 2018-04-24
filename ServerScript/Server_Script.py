import os
import shutil
import Creating_Folders
import Moving_Server_Folders

#downloading the given servers 
os.system('go get https://github.com/stellar/bridge-server') #retrieving the bridge server 
os.system('go get github.com/SendFriend/stellar-backend/tree/master/compliance-server') #retreving the compliance server 
os.system('go get -u github.com/stellar/go/services/federation') #retrieving the federation server 

#Creating three folders in the current directory for the servers 
Creating_Folders.create_folder('./bridge_server/')
Creating_Folders.create_folder('./compliance_server/')
Creating_Folders.create_folder('./federation_server/')

#Move the files of of interest to the corresponding directories
#Bridge Server Files
Moving_Server_Folders.moving_server_files('bridge', 'bridge_server')
Moving_Server_Folders.moving_server_files('bridge.cfg', 'bridge_server')
Moving_Server_Folders.moving_server_files('bridge.service', 'bridge_server')
#Compliance Server Files
Moving_Servers_Folders.moving_server_files('compliance', 'compliance_server')
Moving_Server_Folders.moving_server_files('compliance.cfg', 'compliance_server')
Moving_Server_Folders.moving_server_files('compliance.service', 'compliance_server')
#Federation Server Files
Moving_Server_Folders.moving_server_files('federation', 'federation_server')
Moving_Server_Folders.moving_server_files('federation.cfg', 'federation_server')
Moving_Server_Folders.moving_server_files('federation.service', 'federation_server')




