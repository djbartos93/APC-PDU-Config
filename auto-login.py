import time
import serial

#before we start here are some functinos that will be useful


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('/dev/ttyS0')
ser.portstr
#ser.open()
ser.isOpen()

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
    
if out != '':
    print ">>" + out
time.sleep(1)
ser.write(1'\r\n')
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out
ser.close()