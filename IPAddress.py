#!/usr/bin/env python
import socket
import os
import re
import sys
if sys.version_info < (3, 0):
    from urllib import urlopen
else:
    from urllib.request import urlopen

def ExtIP(): #Get the computers external IP Address
    ip = re.compile("\d+\.\d+\.\d+\.\d+") #Regular Expression for IP Address
    fqn = os.uname()[1] #Get the computers name
    try: #try to connect to whatsmyip.org
        ext_ip = urlopen('http://whatismyipaddress.com/').read()
    except: #if that fails try private internet access
        print('Failed. Trying again.')
        ext_ip = urlopen('https://www.privateinternetaccess.com/pages/whats-my-ip/').read()
    list = ip.findall(str(ext_ip)) #search through page to get IP
    return (fqn + "\nExternal IP: " + list[0]) #return computer name and IP Address

def IntIP(): #Get Internal (Local) IP Address
    local = ("Internal IP: " + socket.gethostbyname(socket.gethostname())) #get IP through socket.gethostname
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    verified = ("Internal IP: " + s.getsockname()[0]) #get again after connecting to the internet
    s.close() #close the socket
    return (local + '\n' + verified) #return the results
