#!/usr/bin/env python
import os
import subprocess
import re
import socket

def Domain_to_IP(d): #find the IP to a given domain name
    ans = socket.gethostbyname(d) #find the ip address
    try: #return ip
        return ans
    except: #if finding ip failed, then return a null address
        return '0.0.0.0'
def IP_to_Domain(ip): #convert ip to domain
    ans = socket.gethostbyaddr(ip) #find domain
    return ans[0] #return result

       
