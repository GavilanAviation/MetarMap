#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MetarMapConfig.py

Config File for MetarMapMain

written by Herb Spenner
rev. 05/10/2018

"""

"""
Airport Area Array
List of the airports to be displayed
First element - the four letter airport abbreviation - station_id
Second element - which LED represents the airport

"""
CONSTANT_airportsArray =[
        ["KMRY",1],
        ["KSNS",2],
        ["KWVI",3],
        ["KCVH",4],
        ["KE16",5],
        ["KRHV",6],
        ["KSJC",7],
        ["KPAO",8],
        ["KSQL",9],
        ["KSFO",10],
        ["KHAF",11],
        ["KOAK",12],
        ["KAPC",13],
        ["KO69",14],
        ["KLVK",15],
        ["KCCR",16]
        ]
"""
LED Strip Configuration

Change LED_COUNT to the number of LEDs in your string

Normally, the other parameters will not need to be changed. 
"""
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

"""
Debugging Switch

Set to True if you would like to print debug messages
Set to False for normal operation

"""
PrintDebug = True

"""
Flight category definitions

LIFR (Low Instrument Flight Rules) - Magenta
IFR (Instrument Flight Rules) - Red
MVFR (Marginal Visual Flight Rules) - Blue
VFR (Visual Flight Rules) - Green
"""
FlightCatDef = {'LIFR':{'red': 255, 'green': 0, 'blue': 255},
                'IFR' :{'red': 255, 'green': 0, 'blue': 0},
                'MVFR':{'red': 0, 'green': 0, 'blue': 255},
                'VFR' :{'red': 0, 'green': 255, 'blue': 0}
                }

"""
URL information to access the aviationweather.com information

Adjust these constants if aviationweather.com makes changes
"""
#flight category URL
CONSTANT_URLflight_category = "https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=2&mostRecent=true&stationString="

#airport name URL
CONSTANT_URLairport_name = "https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=stations&requestType=retrieve&format=xml&fields=site&stationString="
CONSTANT_secondPartURLflight_category = "&hoursBeforeNow=2&mostRecent=true&fields=flight_category"

"""
Constant for the number of error cycles

The Metar website generates random errors. This counts the number of
retries to correct the errors
"""
CycleRetries = 1

