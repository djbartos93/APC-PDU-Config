import time
import serial
import os

#before we start here are some functinos that will be useful


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyS0')
ser.portstr
#ser.open()
ser.isOpen()

#login first
defaultuser = raw_input('Enter the Default User (usually apc): ')
print ('you entered' , defaultuser)
defaultpass = raw_input('Enter the Default Password (usually apc): ')
print ('you entered' , defaultpass)

ser.write(defaultuser + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
time.sleep(1)
ser.write(defaultpass + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
time.sleep(1)
ser.write(defaultpass + '\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
if out != '':
    print ">>" + out
time.sleep(2)
#the next step is to set a default IP for firmware updates
tempip = "172.16.0.57"
tempnetmask = "255.255.254.0"
tempgateway = "172.16.0.1"

#some variables to test wit

one = 1
two = 2
three = 3
four = 4


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
ser.close()