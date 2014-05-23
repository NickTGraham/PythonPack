#!/usr/bin/env python
import os
import subprocess
import re

def Domain_to_IP(d): #find the IP to a given domain name
    c = re.compile("\d+\.\d+\.\d+\.\d+") #regular expression to find IP
    cmd = ['host ' + d] #using the host command
    #get output of host command
    result = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell = True ).communicate()[0]
    ans = c.findall(str(result)) #find the ip address
    try: #return ip
        return ans[0]
    except: #if finding ip failed, then return a null address
        return '0.0.0.0'
def IP_to_Domain(ip): #convert ip to domain
    i = re.compile('\S+\.\S+')
    cmd = ['host ' + ip] #again with host
    result = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell = True ).communicate()[0]
    ans = i.findall(str(result)) #find domain
    final_ans = ans[1].replace('.\\n\'', '')
    return final_ans #return result
