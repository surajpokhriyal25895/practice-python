#! /usr/bin/python
import sys,getpass
from imapclient import IMAPClient

ser = IMAPClient("imap.gmail.com",use_uid=True,ssl=True)
try:
    ser.login("mayuroks","darkchaos")
except ser.Error, e:
    print "shit happened", e
    sys.exit(1)
ser.select_folder("inbox")
data = ser.fetch("1:*",['BODY[HEADER.FIELDS (FROM)]'])

akey = 'BODY[HEADER.FIELDS (FROM)]'
string = ""
output=[]
for key in data:
    string = data[key][akey]
    if "@" in string:
        i1 = string.index("@")
    if ">" in string:
        i2 = string.index(">")
    try:
        output.append(string[i1+1:i2])
    except TypeError, e:
        continue

for count,elem in sorted(((output.count(e),e) for e in set(output)), reverse=True):
    print '%s (%d)' % (elem,count)
ser.logout()
