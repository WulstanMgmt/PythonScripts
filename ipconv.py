#!/usr/bin/env python

import sys
if len(sys.argv) < 2:
    print "Enter IP address as first argument: python %s 127.0.0.1"%sys.argv[0]
    sys.exit(1)

ip = sys.argv[1]
ips = ip.split('.')
iph = '0x{:02X}.0x{:02X}.0x{:02X}.0x{:02X}'.format(*map(int, ips))
ipi = reduce(lambda a, b: (a << 8) + b, map(int, ips), 0)
ipo = '{:04o}.{:04o}.{:04o}.{:04o}'.format(*map(int, ips))
ipbb = '{:08b}.{:08b}.{:08b}.{:08b}'.format(*map(int, ips))

print "Long: %s"%ipi
print "Hex: %s"%iph
print "Octal: %s"%ipo
print "Binary: %s"%ipbb

for j in range(1,3):
    ipb = int(ips[j])
    
    for i in range(j,len(ips)-1):
        ipb = ipb*256+int(ips[i+1])
    
    fstring = "{:d}."*j
    print "Mixed long: "+(fstring.format(*map(int, ips[:j])))+str(ipb)
    print "Mixed long (hex): "+(fstring.format(*map(int, ips[:j])))+"0x{:02X}".format(ipb)
