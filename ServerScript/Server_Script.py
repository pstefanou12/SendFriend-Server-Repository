import os
import shutil
import Creating_Folders
import Moving_Server_Folders
import Symlink

#downloading the given servers 
os.system('env GIT_TERMINAL_PROMPT=1 go get github.com/SendFriend/stellar-backend/tree/master/bridge-server') #retrieving the bridge server 
os.system('env GIT_TERMINAL_PROMPT=1 go get github.com/SendFriend/stellar-backend/tree/master/compliance-server') #retreving the compliance server 
os.system('env GIT_TERMINAL_PROMPT=1 go get github.com/SendFriend/stellar-backend/tree/master/federation-server') #retrieving the federation server 

#Creating three folders in the current directory for the servers 
Creating_Folders.create_folder('./bridge_server/')
Creating_Folders.create_folder('./compliance_server/')
Creating_Folders.create_folder('./federation_server/')

#Move the files of of interest to the corresponding directories
#Bridge Server Files
Moving_Server_Folders.moving_server_files('bridge', 'bridge-server', 'bridge_server')
Moving_Server_Folders.moving_server_files('bridge.cfg', 'bridge-server', 'bridge_server')
Moving_Server_Folders.moving_server_files('bridge.service', 'bridge-server', 'bridge_server')
#Compliance Server Files
Moving_Server_Folders.moving_server_files('compliance', 'compliance-server', 'compliance_server')
Moving_Server_Folders.moving_server_files('compliance.cfg', 'compliance-server', 'compliance_server')
Moving_Server_Folders.moving_server_files('compliance.service','compliance-server', 'compliance_server')
#Federation Server Files
Moving_Server_Folders.moving_server_files('federation', 'federation-server', 'federation_server')
Moving_Server_Folders.moving_server_files('federation.cfg', 'federation-server', 'federation_server')
Moving_Server_Folders.moving_server_files('federation.service', 'federation-server', 'federation_server')

#Making symlinks between the service files and the location where systemctl files are stored in Ubuntu
Symlink.symlink_files("bridge_server/bridge.service", "/lib/systemd/system/") #symlink bridge.service file
Symlink.symlink_files("compliance_server/compliance.service", "/lib/systemd/system/") #symlink compliance.service file
Symlink.symlink_files("federation_server/federation.service", "/lib/systemd/system/") #symlink federation.service file



