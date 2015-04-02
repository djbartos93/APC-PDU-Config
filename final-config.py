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

ser.write(ntpupdate + '\r\n')
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

print "We are now DONE configuring the PDU!! Make sure all the vaules are correct and the passwords work if this is the first time you have run this script.
print "otherwise you are finished with this one, move onto the next. if you have issues connecting"
print "try launching minicom and then resetting the modem. this will be intnigrated into a later vesrion"