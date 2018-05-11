#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MetarMapMain.py

Metar Map Main Code

Get flight category inforation from aviationweather.gov and control LED map

written by Herb Spenner
rev. 05/10/2018

"""

#Import Config File
import ConfigMetarMap

#Import Bin File
import BinMetarMap

#Import LED functions
import neopixel

# Create NeoPixel object with appropriate configuration.
strip = neopixel.Adafruit_NeoPixel(ConfigMetarMap.LED_COUNT, ConfigMetarMap.LED_PIN, 
                                   ConfigMetarMap.LED_FREQ_HZ, ConfigMetarMap.LED_DMA, 
                                   ConfigMetarMap.LED_INVERT, ConfigMetarMap.LED_BRIGHTNESS, 
                                   ConfigMetarMap.LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

AirportError = False
#Process Airports
for i in range(ConfigMetarMap.CycleRetries + 1):
	for airportInfo in ConfigMetarMap.CONSTANT_airportsArray:
		if ConfigMetarMap.PrintDebug:
			print(airportInfo[0])
		airportName = BinMetarMap.Get_Airport_Name(airportInfo[0])
		if airportName == None:
			AirportError = True
			strip.setPixelColorRGB(airportInfo[1] - 1,0,0,0)
			strip.show()
			if ConfigMetarMap.PrintDebug:
				print(airportInfo[0] + " can't be found")
				print("LED set to black")
		else:
			flight_category = BinMetarMap.Get_Flight_Category(airportInfo[0])
			if flight_category == None:
				AirportError = True
				strip.setPixelColorRGB(airportInfo[1]- 1,0,0,0)
				strip.show()
				if ConfigMetarMap.PrintDebug:
					print("Airport: " + airportName + "; ID: " + airportInfo[0] + "; Flight Category: failed; LED #: " + str(airportInfo[1]))
					print("LED set to black")
			else:          
				color_array=ConfigMetarMap.FlightCatDef[flight_category]
				strip.setPixelColorRGB(airportInfo[1] - 1,color_array['red'],color_array['green'],
									   color_array['blue'])
				strip.show()
				if ConfigMetarMap.PrintDebug:
					print("Airport: " + airportName + "; ID: " + airportInfo[0] + "; Flight Category: " + flight_category + "; LED #: " + str(airportInfo[1]))
					print("red %d, green %d, blue %d" % (color_array['red'],color_array['green'],
						  color_array['blue'] ))
	if AirportError == False:
		exit()
