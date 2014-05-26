#!/usr/bin/env python
import Locate
import Connections
import DomainLookup
import sys

def where(loc):
    try:
      return (Locate.Locate(loc))
    except:
      dom = DomainLookup.Domain_to_IP(loc)
      return (Locate.Locate(dom))
def where_users():
    return (Connections.LocalUsers())

try:
    print(where(sys.argv[1]))
except:
    print(where_users())
