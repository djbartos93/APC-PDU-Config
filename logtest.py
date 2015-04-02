import string
import random
import time

#in this section we will define all of the variables for the final steps of config
#we need a function for random passwords
def pwgen(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#config values that will not change
currentpw = "apc"
username = "nexcess"
adminpw = pwgen(8)
ntpip = "10.13.37.20"
ntpoffset = 14
ntpupdate = 2
ac1name = pwgen(10)
ac2name = "m4xn3x"

#config values that will change and or need input
sysipin = raw_input("Enter the new IP (found in the spreadsheet): ")
netmask = "255.255.292"
gateway = "10.192.128.1"
location = raw_input("Enter the location (Rack Name): ")
pduname = raw_input("Enter the name found in the spreadsheet minus '.mel-01.dtw.nexcess.net': ")

#for debugging we can look at the variables by printing them all (uncomment to use)
#print currentpw
#print username
#print adminpw
#print ntpip
#print ntpoffset
#print ntpupdate
#print ac1name
#print ac2name
#print sysipin
#print netmask
#print gateway
#print location
#print pduname

print ('new username is' ,  username)
print ('new password is' , adminpw)
print ('new SNMP Community name 1 is' , ac1name)
time.sleep(10)


#lets write thoes names and passwords to a file so we dont forget!
log = "admin password for PDU", pduname, "is", adminpw, "SNMP Community name 1:", ac1name
print log
f = open('/Users/ericbartos/pdu-config.log', 'a+')
s = str(log)
f.write("\r")
f.write(s)