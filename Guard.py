#!/usr/bin/env python
import Locate
import Connections
import DomainLookup
import GMail
import os
import subprocess
import re
import sys


locations = ''

def Guard(): #checks were current connections are, and if not approved locations, reports it.
    global locations
    ip_con = Connections.Connections('ip') #find the ip connections
    ip_dom = Connections.Connections('domain') #find domain connections
    ip_loc = ''
    for ip in ip_con: #get locations of ip connections
        ip_loc = ip_loc + Locate.Locate(ip) + '\n'
    dom_loc = ''
    for d in ip_dom: #get locations of domain connections
        dom_loc = dom_loc + Locate.Locate(DomainLookup.Domain_to_IP(d)) + '\n'
    locations = ip_loc + '\n' + dom_loc
    states = Locate.FindStates(locations) #finds the states of the connections
    for s in states: #check to see if in approved locaitons
        if (s == 'RI' or s == 'NY'):
            continue
        else:
            return True #if there is a problem, returns true
    return False #otherwise returns false

def CleanUp(): #deletes file generated when there is a problem
    os.remove('LocationReport')
if(Guard()): #if there is a problem
    try: #open file
        file = open('LocationReport', 'rb+')
    except:#or create it
        file = open('LocationReport', 'wb+')
    results = file.read()
    if(results == 'We Have a Problem'): #if the problem has been delt with, ignore it
        print('Already Handled')
        #already been dealt

    else: #otherwise
        file.seek(0,0)
        file.write('We Have a Problem') #log the problem in the file
        GMail.email('From', ['to'], 'Intruder', 'We have an issue\n' + locations) #send email about the problem
