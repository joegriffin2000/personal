#This is a comment 
#
#
#

import socket 
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("IP Address: " + IPAddr)

