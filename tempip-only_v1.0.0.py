#!/usr/bin/python
import serial
import time
import string
import random

print "this script will set a temporary IP on the PDU for a firmware update. only use if you have already been logged in with minicom and HAVE NOT logged out"
print "this script does not log in to the PDU for you!"
print "when done make sure you check the firmware version in minicom, and set the password and username to both be 'apc'"

ser = serial.Serial('/dev/ttyS0')
ser.portstr
#ser.open()
ser.isOpen()

#the next step is to set a default IP for firmware updates
tempip = "172.16.0.57"
tempnetmask = "255.255.254.0"
tempgateway = "172.16.0.1"

#lets apply this, its messy but it gets the job done. here we are going thru the menus and setting the IP
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
ser.write(tempip + '\r\n')
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

ser.write(tempnetmask + '\r\n')
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

ser.write(tempgateway + '\r\n')
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
ser.write('^[')
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
ser.write('4\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(40)
#now we need to close the serial port after the logout becuase it will hang up on us
ser.close()

#alright now that that is done (a lot of work for something so silly...we need to update the frimware, lets tell the guy at the cousle

print "We are now ready to update the frimware on the PDU"
print "In order for this script to work you MUST update the frimware"
print "to update the firmware use the firmware update tool found on the wiki, its a windows only program :'( but it must be done"
print "once the firmware update is done check with mini come and be sure to exit minicom by logging out of the configueration interface"
print "you will also need to be sure you do a ctrl+a, ctrl+x and yes to exit minicom"
raw_input("Press Enter when the firmware is updated...and run the config-only script!")

