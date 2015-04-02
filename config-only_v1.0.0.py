#!/usr/bin/python
import serial
import time
import string
import random

#nexcess PDU config script

print "This script will help configure the 0U PDU's in any MEL Rack."
print "Be sure you have all of the tools needed before starting this script."
print "WARNING! THIS WILL CHANGE ALL SETTINGS ON THE PDU!!"
print ""
raw_input ("Press Enter to continue...")
#getting some basic stuff out of the way, a loading bar...
def progressbar(it, prefix = "", size = 60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()
    
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()


#here we go, this is how we are going to conenct to the serial port and talk to the PDU
ser = serial.Serial('/dev/ttyS0')
ser.portstr
#ser.open()
ser.isOpen()
time.sleep(1)
#now that we are connected lets get logged in to reset everything

defaultuser = raw_input('Enter the Default User (usually apc): ')
print ('you entered' , defaultuser)
defaultpass = raw_input('Enter the Default Password (usually apc): ')
print ('you entered' , defaultpass)

#now lets get log in!
#sending the username
ser.write(defaultuser + '\r\n')
out = ''
time.sleep(1)
#to debug uncomment this section
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#sending the password
ser.write(defaultpass + '\r\n')
out = ''
time.sleep(1)
ser.write(defaultpass + '\r\n')
out = ''
time.sleep(1)
#to debug uncomment this secion
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out

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
contact = "dc-support-dept@nexcess.net"

#config values that will change and or need input
sysipin = raw_input("Enter the new IP (found in the spreadsheet): ")
netmask = "255.255.292.0"
gateway = "10.192.128.1"
location = raw_input("Enter the location (Rack Name): ")
pduname = raw_input("Enter the name found in the spreadsheet minus '.mel-01.dtw.nexcess.net': ")

#for debugging we can look at the variables by printing them all (uncomment to use)
print currentpw
print username
print adminpw
print ntpip
print ntpoffset
print ntpupdate
print ac1name
print ac2name
print sysipin
print netmask
print gateway
print location
print pduname

print ('new username is' ,  username)
print ('new password is' , adminpw)
print ('new SNMP Community name 1 is' , ac1name)
time.sleep(10)

#lets write thoes names and passwords to a file so we dont forget!
log = "admin password for PDU", pduname, "is", adminpw, "SNMP Community name 1:", ac1name
print log
f = open('/root/pdu-config.log', 'a+')
s = str(log)
f.write("\r")
f.write(s)

#now we are ready for the hard work part, putting all those values into a PDU. Here we go!

#lets put those variables somehwere

#change admin username and password
ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(currentpw + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(username + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(adminpw + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(adminpw + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)


time.sleep(1)
ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#identifcation
ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(pduname + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(contact + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(location + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)


ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)


ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#ntp info
ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(ntpip + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('14\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('5\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('6\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#network setup

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)
ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
time.sleep(1)
ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
time.sleep(1)
ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
time.sleep(1)

if out != '':
    print ">>" + out
time.sleep(1)
ser.write(sysipin + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(netmask + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(gateway + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#disable ftp

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('3\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#dissable web/ssl/tls
ser.write('6\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('6\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

#snmp 1
if out != '':
    print ">>" + out
time.sleep(1)

ser.write('8\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(ac1name + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#snmp2

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('1\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(ac2name + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('2\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)

#now we log out! and we will be DONE!

ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(5)

ser.close()

print "you are now done with the PDU config. make sure the passwords were recorded into the file and move on!"
raw_input("press enter to exit")

