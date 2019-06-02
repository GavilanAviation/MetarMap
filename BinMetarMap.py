#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MetarMapBin.py

Bin for MetarMap
General info for MetarMap application

written by Herb Spenner
rev. 04/06/2019
"""
#Import Config File
import ConfigMetarMap

#Import URL Librarys
import urllib3

#Disable security warning since only accessing aviationweather.gov
#Not needed with raspberry pi
urllib3.disable_warnings()

#Import XML Library
from lxml import etree

#Import LED functions
import neopixel

def Get_Flight_Category(airport):
    """
    function:   Get_Flight_Category - get flight_category for aiport
                uses Metar info from aviationweather.com
    
    input:      airport - four charactor airport abbreviation
    
    return:     flight category
                returns None if it can not be found
    """
    try:
        url = ConfigMetarMap.CONSTANT_URLflight_category + airport
        r = Get_URL_General(url)
        if r == None:
            return None       
        root = etree.fromstring(r.data)
        flight_category = root.find('./data/METAR/flight_category')
        if flight_category == None:
            return None
        return flight_category.text
    except:
        return None
    #end of Get_Flight_Category
    
    
def Get_Airport_Name(airport):
    """
    function:   Get_Airport_Name - get airport name(site) for aiport
                uses STATION INFO info from aviationweather.com
    
    input:      airport - four charactor airport abbreviation
    
    return:     airport name
                returns None if it can not be found
    """
    try:
        url = ConfigMetarMap.CONSTANT_URLairport_name + airport
        r = Get_URL_General(url)
        if r == None:
            return None
        root = etree.fromstring(r.data)
        airportName = root.find('./data/Station/site')
        if  airportName == None:
             return None
        return airportName.text
    except:
            return None
    #end of Get_Airport_Name

def Get_URL_General(url):
    """
    function:   General Get URL
                Centralize error handling
    
    input:      url
    
    return:     http get of url
                returns None if error
    """
    http = urllib3.PoolManager()
    try:
        return http.request('GET', url)
    except urllib3.exceptions.exceptions.NewConnectionError:
        print('Connection failed.')
    return None
    #end of Get_URL_General
    
def Light_Flight_Category_LED(strip):
    """
    function:   Turn on Flight Category LEDS
    
    input:      strip - neopixel object
    
    return:     none
    """
    color_array=ConfigMetarMap.FlightCatDef['LIFR']
    strip.setPixelColorRGB(ConfigMetarMap.LIFR_LED_Num - 1,color_array['red'],color_array['green'],
                           color_array['blue'])
    color_array=ConfigMetarMap.FlightCatDef['IFR']
    strip.setPixelColorRGB(ConfigMetarMap.IFR_LED_Num - 1,color_array['red'],color_array['green'],
                           color_array['blue'])
    color_array=ConfigMetarMap.FlightCatDef['MVFR']
    strip.setPixelColorRGB(ConfigMetarMap.MVFR_LED_Num - 1,color_array['red'],color_array['green'],
                           color_array['blue'])
    color_array=ConfigMetarMap.FlightCatDef['VFR']
    strip.setPixelColorRGB(ConfigMetarMap.VFR_LED_Num - 1,color_array['red'],color_array['green'],
                           color_array['blue'])
    strip.show()
    if ConfigMetarMap.PrintDebug:
        print("Flight Category LEDs turned on")
    return
    #end of Light_Flight_Category_LED

