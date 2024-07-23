# IpAddressFinder.py
# by Joe Griffin
# found some code online and copied it into my own file

import socket 
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("IP Address: " + IPAddr)

