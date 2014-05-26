#!/usr/bin/env python
import Locate
import Connections
import DomainLookup

if (len(sys.argv) > 1):
    try:
        print (Locate(sys.argv[1]))
    except:
            dom = Domain_to_IP(sys.argv[2])
            print (Locate(dom))

else:
    print(Connections.LocalUsers())
