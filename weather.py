#!/usr/bin/env python3

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import sys

def getForcast(zipcode):
    w="http://xml.weather.yahoo.com/forecastrss?p=" + zipcode
    return urlopen(w)

def parseWeather (urlData):
    data = ET.parse(urlData)
    root = data.getroot()
    
    location = (getLocation(root))
    condition = (getCondition(root))
    units = (getUnits(root))
    wind = (getWind(root))
    atm = (getAtmosphere(root))
    ast = (getAstronomy(root))

    city = location[0]
    state = location[1]

    weather = condition[0]
    temp = condition[1]
    date = condition [2]

    degree = units[0]
    speed = units[1]

    windchill = wind[0]
    windspeed = wind[1]

    humidity = atm[0]

    sunrise = ast[0]
    sunset = ast[1]

    report = "{0}, {1}\n{2} {3}º{4}\nWindchill: {5}º{4} \t Windspeed: {6} {7}\nHumidity: {8}%\nSunrise: {9} \t Sunset: {10}".format(city, state, weather, temp, degree, windchill, windspeed, speed, humidity, sunrise, sunset)
    print(report)

def getLocation (root):
    location = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}location')
    result = []
    result.append(location[0].get('city'))
    result.append(location[0].get('region'))
    return (result);
def getCondition (root):
    condition = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}condition')
    result = []
    result.append(condition[0].get('text'))
    result.append(condition[0].get('temp'))
    result.append(condition[0].get('date'))
    return(result)
def getUnits (root):
    units = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}units')
    result = []
    result.append(units[0].get('temperature'))
    result.append(units[0].get('speed'))
    return (result)
def getWind (root):
    wind = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}wind')
    result = []
    result.append(wind[0].get('chill'))
    result.append(wind[0].get('speed'))
    return (result)
def getAtmosphere (root):
    atm = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}atmosphere')
    result = []
    result.append(atm[0].get('humidity'))
    return (result)
def getAstronomy (root):
    ast = root.findall('.//{http://xml.weather.yahoo.com/ns/rss/1.0}astronomy')
    result = []
    result.append(ast[0].get('sunrise'))
    result.append(ast[0].get('sunset'))
    return (result)

if (len(sys.argv) > 1):
    parseWeather(getForcast(sys.argv[1]))
