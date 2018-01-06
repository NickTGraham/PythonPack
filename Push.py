#!/usr/bin/env python2

from pushbullet import Pushbullet
import re
from Dotfile import dotfile
import requests
import sys
import datetime
import os

PBKEY = ""

def getDefaults():
    global PBKEY
    info = dotfile()
    PBKEY = info.getVal("pushbullet")

getDefaults()
pb = Pushbullet(PBKEY)

if (len(sys.argv) > 1):
    pb.push_note("Command", " ".join(sys.argv))
else:
    pb.push_note("Command", "\n".join(sys.stdin.readlines()))
