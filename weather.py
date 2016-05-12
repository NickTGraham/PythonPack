#!/usr/bin/env python3

#Remaking my weather script to use forcast.io now that Yahoo weather is gone

import requests
import sys
import datetime
import os
from geopy import geocoders
from pushbullet import Pushbullet
import re
from Dotfile import dotfile

gn = geocoders.Nominatim()

APIKEY = ""
Long, Lat = "",""
PBKEY = ""
commonName = ""

def getDefaults():
    global APIKEY, Long, Lat, PBKEY, commonName
    info = dotfile()
    APIKEY = info.getVal("forcast.io")
    Long = info.getVal("long")
    Lat = info.getVal("lat")
    commonName = info.getVal("location")
    PBKEY = info.getVal("pushbullet")

def coordinatesFromZipcode(zipcode):
    global Long, Lat, commonName
    location = gn.geocode(zipcode)
    commonName = location.address.split(",")[0]
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
    rain = "{0:.0f}".format(float(daily["precipProbability"]) * 100)
    report = '{5}\t{3}\n{0}\nHigh: {1} \t Low: {2}\n{4}% Chance of Rain'.format(summary, high, low, day, rain, commonName)
    return report

def weeklyResults(response):
    information = response["daily"]["data"]
    report = ""
    for dayReport in information:
        time = dayReport["apparentTemperatureMaxTime"]
        day = datetime.datetime.utcfromtimestamp(time).date()
        day = formatDate(day)
        summary = dayReport["summary"]
        high = dayReport["temperatureMax"]
        low = dayReport["temperatureMin"]
        rain = "{0:.0f}".format(float(dayReport["precipProbability"]) * 100)
        sample = '{5}\t{3}\n{0}\nHigh: {1} \t Low: {2}\n{4}% Chance of Rain\n\n'.format(summary, high, low, day, rain, commonName)
        report = report + sample
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
weekly = False
regex = re.compile("^\d{5}$")
for arg in sys.argv:
    if arg == "push":
        push = True
    elif regex.match(arg):
        coordinatesFromZipcode(arg)
    elif arg == "weekly":
        weekly = True
#if (len(sys.argv) > 1):
#    coordinatesFromZipcode(sys.argv[1])

results = getForcast(APIKEY, Long, Lat)

if weekly:
    weather = weeklyResults(results)
else:
    weather = todaysResults(results)

if push:
    pb.push_note("Weather", weather)
else:
    print (weather)
