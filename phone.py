#!/usr/bin/env python
import re
import urllib
import sys
if (sys.version_info < (3, 0)):
    from urllib import urlopen
else:
    from urllib.request import urlopen
import requests


def landline(phonenumber):
    info = urlopen('http://www.yellowpages.com/reversephonelookup?phone=' + phonenumber)
    html = info.read()
    names = re.compile('(?<=\"fullname\">)([\w\s]+)(?=</a>)')
    lis = names.findall(str(html))
    return(lis)

def mobile(phonenumber):
    url = "https://m.facebook.com/login/identify?ctx=recover"
    phone = { "email": phonenumber }
    req = requests.post(url, data=phone)
    data = req.text.encode("utf8")
    person = re.compile('(?<=<div class="mfsl fcb"><strong>)([\w\s]+)(?=</strong>)')
    name = person.findall(str(data))
    return (name)

def newMobile(phone):
       url = "https://www.facebook.com/search/top/?q=" + str(phone)
       req = requests.post(url)
       data = req.text.encode("utf8")
       print(data)

if (len(sys.argv) > 1):
    phone = re.compile('\d{10,11}')
    if (phone.match(sys.argv[1])):
        landresults = landline(sys.argv[1])
        cellresults = mobile(sys.argv[1])
        if (landresults != []):
            print ('Landline info found:')
            print (landresults)
        if(cellresults != []):
            print('Mobile info found:')
            print(cellresults)
        if(landresults == [] and cellresults == []):
            print('No results found.')
    else:
        print('invalid phone input')
        
