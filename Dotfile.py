import os
import re

class dotfile:
    vals = {}
    def __init__(self):
        info = open(os.path.join(os.path.expanduser('~'),'.nickrc'))
        regex = re.compile("^.*=.*$")
        for line in info:
            if(regex.match(line)):
                line = line.rstrip("\r\n")
                results = line.split("=")
                self.vals[results[0]] = results[1]
        info.close()

    def getVal(self, valKey):
        return self.vals[valKey]
