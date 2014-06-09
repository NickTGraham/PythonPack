import socket
import struct
import DomainLookup

def main (domain):
    finished = False
    ip = DomainLookup.Domain_to_IP(domain)
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    counter = 0
    port = 33434
    while not finished:
        #get data
        recieve = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send.setsockopt(socket.SOL_IP, socket.IP_TTL, counter)
        timeout = struct.pack("ll", 5, 0)
        recieve.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)
        recieve.bind(('0.0.0.0', port))
        send.sendto('', (domain, port))
        current_location = None
        current_ip = None
        try:
            _, current_ip = recieve.recvfrom(512)
            current_ip = current_ip[0]
            try:
                current_location = DomainLookup.IP_to_Domain(current_ip)
            except socket.error:
                current_location = 'Not Found'
        except socket.error:
            pass
        finally:
            send.close()
            recieve.close()
        
        #print data
        if current_ip is not None:
            current = '%s (%s)' % (current_location, current_ip)
        else:
            current = '*'
        print(str(counter) + '\t' + current)

        counter+=1
        
        #break once done
        if current_ip == ip:
            finished = True
if __name__ == '__main__':
    main('www.google.com')
