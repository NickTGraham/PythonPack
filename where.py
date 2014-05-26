#!/usr/bin/env python
import Locate
import Connections
import DomainLookup
import sys

if (len(sys.argv) > 1):
    try:
        print (Locate.Locate(sys.argv[1]))
    except:
            dom = DomainLookup.Domain_to_IP(sys.argv[2])
            print (Locate.Locate(dom))

else:
    print(Connections.LocalUsers())
