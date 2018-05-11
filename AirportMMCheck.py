#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AirportMMCheck.py

Check Airport config in MetarMapConfig.py

Get flight category inforation from aviationweather.gov and control LED map

written by Herb Spenner
rev. 05/08/2018

"""

#Import Config File
import ConfigMetarMap

#Import Bin File
import BinMetarMap

#Process Airports
for airportInfo in ConfigMetarMap.CONSTANT_airportsArray:
	#Print airport abbreviation
    print(airportInfo[0])
    airportName = BinMetarMap.Get_Airport_Name(airportInfo[0])
    if airportName == None:
    	#Airport not found
        print(airportInfo[0] + " can't be found. Check the configuration in ConfigMetarMap.py")
    else:
        flight_category = BinMetarMap.Get_Flight_Category(airportInfo[0])
        if flight_category == None:
        	#Airport found but weather not available
            print("Airport: " + airportName + "; ID: " + airportInfo[0] + "; Flight Category: failed; LED #: " + str(airportInfo[1]))
        else:
        	#Airport show airport weather         
            print("Airport: " + airportName + "; ID: " + airportInfo[0] + "; Flight Category: " + flight_category + "; LED #: " + str(airportInfo[1]))
