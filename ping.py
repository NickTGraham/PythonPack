import socket
import time
import struct
import sys
import DomainLookup
#from time import time

class Pinger(object):
    
    def __init__ (self, domain):
        self.domain = domain
        self.finished = False
        self.ip = DomainLookup.Domain_to_IP(domain)
        self.icmp = socket.getprotobyname('icmp')
        self.udp = socket.getprotobyname('udp')
        self.counter = 0
        self.port = 33434
        self.times = []
        
    def ping(self, count):
        self.recieve = socket.socket(socket.AF_INET, socket.SOCK_RAW, self.icmp)
        self.send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, self.udp)
        self.send.setsockopt(socket.SOL_IP, socket.IP_TTL, 35)
        timeout = struct.pack("ll", 5, 0)
        self.recieve.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)
        self.recieve.bind(('0.0.0.0', self.port))
        self.send.sendto('', (self.domain, self.port))
        current_location = None
        current_ip = None
        t1 = time.time()
        try:
            _, current_ip = self.recieve.recvfrom(512)
        except socket.error:
            pass
        finally:
            t2 = time.time()
            self.send.close()
            self.recieve.close()
        #print data
        if current_ip is not None:
            t = float("{0:.3f}".format((t2 - t1) * 1000))
            self.times.append(t)
            current = '%s (%s ms)' %(self.domain, str(self.times[self.counter]))
            self.counter+=1
        else:
            current = '*'
        print(str(self.counter) + '\t' + current)
        
        #break once done
        if self.counter > count - 1:
            print ('ForceStopped')
            p.finished = True

    def stats(self):
        minimum = min(self.times)
        maximum = max(self.times)
        s = sum(self.times)
        avg = s/len(self.times)
        results = 'min: %.3f\tmax: %.3f\tavg: %.3f' %(minimum, maximum, avg)
        print (results)
        
if (len(sys.argv) == 2):
    p = Pinger(sys.argv[1])
    while not p.finished:
        p.ping(5)
    p.stats()
elif (len(sys.argv) == 3):
    p = Pinger(sys.argv[1])
    while not p.finished:
        p.ping(int(sys.argv[2]))
    p.stats()
