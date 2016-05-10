#!/usr/bin/env python3

#Remaking my weather script to use forcast.io now that Yahoo weather is gone

import requests
import sys
import datetime
import os
from geopy import geocoders
from pushbullet import Pushbullet
import re

gn = geocoders.Nominatim()

APIKEY = ""
Long, Lat = "",""
PBKEY = ""

def getDefaults():
    global APIKEY, Long, Lat, PBKEY
    dotfile = open(os.path.join(os.path.expanduser('~'),'.nickrc'))
    APIKEY = dotfile.readline().rstrip("\r\n")
    Long = dotfile.readline().rstrip("\r\n")
    Lat = dotfile.readline().rstrip("\r\n")
    PBKEY = dotfile.readline().rstrip("\r\n")

def coordinatesFromZipcode(zipcode):
    global Long, Lat
    location = gn.geocode(zipcode)
    Long = "{0:.3f}".format(location.longitude)
    Lat = "{0:.3f}".format(location.latitude)

def getForcast(APIKEY, Long, Lat):
    url = "https://api.forecast.io/forecast/" + APIKEY + "/" + Lat + "," + Long
    response = requests.get(url)
    return response.json()

def todaysResults(response):
    daily = response["daily"]["data"][0]
    time = daily["apparentTemperatureMaxTime"]
    day = datetime.datetime.utcfromtimestamp(time).date()
    day = formatDate(day)
    summary = daily["summary"]
    high = daily["temperatureMax"]
    low = daily["temperatureMin"]
    rain = daily["precipProbability"]
    report = '{3}\n{0}\nHigh: {1} \t Low: {2}\n{4}% Chance of Rain'.format(summary, high, low, day, rain)
    return report

def formatDate(date):
    weekday = {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"
    }[date.weekday()]

    month = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
    }[date.month]

    return '{0} {1} {2}'.format(weekday, month, date.day)

getDefaults()
pb = Pushbullet(PBKEY)
push = False
regex = re.compile("^\d{5}$")
for arg in sys.argv:
    if arg == "push":
        push = True
    elif regex.match(arg):
        coordinatesFromZipcode(arg)
#if (len(sys.argv) > 1):
#    coordinatesFromZipcode(sys.argv[1])

results = getForcast(APIKEY, Long, Lat)
if push:
    pb.push_note("Weather", todaysResults(results))
else:
    print (todaysResults(results))
