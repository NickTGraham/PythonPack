#! /usr/bin/env python

from urllib.request import urlopen
import xml.etree.ElementTree as ET

def getForcast(zipcode):
    w="http://xml.weather.yahoo.com/forecastrss?p=" + zipcode
    return urlopen(w)

def parseWeather (urlData):
    data = ET.parse(urlData)
    root = data.getroot()
    print (getLocation(root))
    print (getCondition(root))
    print (getUnits(root))
    print (getWind(root))
    print (getAtmosphere(root))
    print (getAstronomy(root))
    

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

parseWeather(getForcast('02852'))
