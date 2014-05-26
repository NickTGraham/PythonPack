#!/usr/bin/env python
import IPAddress
import GMail
import datetime
import re
import sys

results = IPAddress.ExtIP() + '\n' + IPAddress.IntIP() #get the current IP Addresses
now = datetime.datetime.now() #get date & time
ip = re.compile("\d+\.\d+\.\d+\.\d+") #set up regular expresion for ip Address
try: #try to open file containing previous IPs and read them in
    file = open('IPAddress.txt', 'r+')
    old = ip.findall(file.read())
except: #if that fails create the file and set the old ones to 0.0.0.0
    file = open('IPAddress.txt', 'w')
    old = ['0', '0', '0']

new = ip.findall(results) #get the Ips from the formated results
i = 0
needsupdate = False
while (i < len(new)): #compairs current IPs to stored IPs
    if (new[i] == old [i]):
        needsupdate = False
    else:
        needsupdate = True
    i = i + 1
if (len(sys.argv) > 1 and sys.argv[1] == '-s'): #if '-s' force print the results
    print(results)
    
elif (needsupdate or (len(sys.argv) > 1 and sys.argv[1] == '-f' )): # if there is a change or '-f' force email the results
    GMail.email('From', ['To'], 'IP Update', results)
    file.seek(0,0)
    file.write(str(now) + '\n' + results + '\n')

file.close() #close the file
