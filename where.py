#!/usr/bin/env python
import Locate
import Connections
import DomainLookup
import sys
import subprocess
import re

def where(loc):
    try:
      return (Locate.Locate(loc))
    except:
      dom = DomainLookup.Domain_to_IP(loc)
      return (Locate.Locate(dom))
def where_users():
    return (Connections.LocalUsers())

def where_traceroute(loc):
    ip = re.compile("\d+\.\d+\.\d+\.\d+")
    cmd = 'traceroute ' + loc
    path = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell = True ).communicate()[0]
    ips = ip.findall(path)
    for i in ips:
        print (where(i) + '\n')

if (len(sys.argv) > 2):
    if (sys.argv[1] == '-tr'):
        where_traceroute(sys.argv[2])

else:
    try:
        print(where(sys.argv[1]))
    except:
        print(where_users())
