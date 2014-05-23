#!/usr/bin/env python
import os
import subprocess
import re
import sys

def Connections(connection_type): #Find Locations of users that are logged in
    cmd = ['pinky'] #try to run the pinky command
    cmd2 = ['who'] #if pinky fails run who command
    if (connection_type == 'ip'): #if the user is looking for ip connections
        c = re.compile("\d+\.\d+\.\d+\.\d+")
    elif (connection_type == 'domain'): #if they're looking for domain name connections
        c = re.compile("\S+\.\S+")
    else: #otherwise input error
        print("ERROR")
        return
    try: #try to find connections using pinky
        output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
        ips = c.findall(str(output))
    except: #try to find connections using who if pinky fails
        output = subprocess.Popen( cmd2, stdout=subprocess.PIPE ).communicate()[0]
        ips = c.findall(str(output))
    result=[]
    for x in ips: #this removes extra characters picked up
        result.append(x.replace('\\t','').replace("\\n'", '').replace('(', '').replace(')', ''))
    return result
