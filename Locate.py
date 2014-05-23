from geoip import geolite2 #More info at http://pythonhosted.org/python-geoip/
import os
import subprocess
import re
import sys

def Locate(ip): # get location of an IP Address
    result = geolite2.lookup(ip)
    if (result is not None):
        ans = ''
        ans = ans + 'Country: ' + result.country + '\n'
        ans = ans + 'Continent: ' + result.continent + '\n'
        for country in result.subdivisions:
            ans = ans + 'Region: ' + (country) + '\n'
        ans = ans + str(result.location)
        return(ans)
    else:
        return('None Type')

def FindStates(loc_data): #find the state from the results
    #This has issues and should be redone, right now also returns South America and others as a state
    #but it works for what I need so...
    state = re.compile('[A-Z]{2}')
    found = state.findall(loc_data)
    i = 0
    while (i < len(found)):
        if(found[i] == 'NA' or found[i] == 'US'):
            found.remove(found[i])
            continue
        else:
           i = i+1
    return found
