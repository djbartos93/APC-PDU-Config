#!/usr/bin/python
import serial
import time
import string
import random

#nexcess PDU config script

print "this script will reset defaults and set a temp IP to do firmware updates on the PDU."
print "in be sure to use minicom to check the firmware version after update!!"
print "if firmware update fials check web config settings"
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

#before we continue any furthr we need to reset to defualts

ser.write('3\r\n')
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

ser.write('YES\r\n')
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
ser.write(chr(27))
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out

time.sleep(1)

#ser.write('4\r\n')
#out = ''
#time.sleep(1)
#while ser.inWaiting() > 0:
#    out += ser.read(1)
#
#if out != '':
#    print ">>" + out
#time.sleep(60)


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

