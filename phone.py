import subprocess
import re
import urllib
from urllib.request import urlopen
import requests

def landline(phonenumber):
    info = urlopen('http://www.yellowpages.com/reversephonelookup?phone=' + phonenumber)
    html = info.read()
    names = re.compile('(?<=\"fullname\">)([\w\s]+)(?=</a>)')
    lis = names.findall(str(html))
    print(lis)

def mobile(phonenumber):
    print('Not Done Yet. ' + phonenumber + ' cannot be found')
    url = "https://m.facebook.com/login/identify?ctx=recover"
    phone = { "email": phonenumber }
    req = requests.post(url, data=phone)
    data = req.text.encode("utf8")
    person = re.compile('(?<=<div class="mfsl fcb"><strong>)([\w\s]+)(?=</strong>)')
    name = person.findall(str(data))
    print (name)

