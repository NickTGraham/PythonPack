#!/usr/bin/python2.7

import requests
import pickle
import sys
import os
from pushbullet import Pushbullet
from Dotfile import dotfile
from difflib import SequenceMatcher

PBKEY = ""
websitelist = ""

def getDefaults():
    global PBKEY, websitelist
    info = dotfile()
    PBKEY = info.getVal("pushbullet")
    websitelist = os.path.expanduser(info.getVal("sites"))

def main():
    getDefaults()
    pb = Pushbullet(PBKEY)

    websites = open(websitelist, 'rb+')
    status = pickle.load(websites)

    for site in status:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(site, headers=headers)

        comp = SequenceMatcher(None, status[site][0], response.text)
        print(site, comp.ratio())
        if comp.ratio() < status[site][1]:
            pb.push_note("Shiba Alert", site + " has updated!" + str(comp.ratio()))
            status[site] = [response.text, comp.ratio()]
        #status[site] = [response.text, comp.ratio()]
    
    websites.seek(0)
    pickle.dump(status, websites)
    websites.close()

def addSite(url):
    websites = open(websitelist, 'r+b')
    try:
        status = pickle.load(websites)
    except:
        status = {}

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    status[url] = response.text
    websites.seek(0)
    pickle.dump(status, websites)


if __name__ == '__main__':
    getDefaults()
    if (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            addSite(sys.argv[i])
    else:
        main()
