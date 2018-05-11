#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CheckLEDColor.py

Check LED Color

written by Herb Spenner
rev. 04/22/2018

"""
#Import Config File
import ConfigMetarMap

#Import LED functions
import neopixel

def Get_Int_Keyboard(txt_question,low_limit,upper_limit):
    """
    function:   Get_Int_Keyboard - Gets an int for the keyboard
                Continues to asks until int
    
    input:      txt_question - question to be asked
    
    return:     int entered
    """
    while True:
        try:
            enter_str = input(txt_question)
            in_int = int(enter_str)
            if in_int >= low_limit and in_int <= upper_limit:  
                return in_int
            print ("%s is invalid" % enter_str)    
        except ValueError:
            print ("%s is invalid" % enter_str)    


   
LED_number = Get_Int_Keyboard("Enter which LED to light: ",1,ConfigMetarMap.LED_COUNT)
red_color = Get_Int_Keyboard("Enter the red value(0 to 255): ",0,255)
green_color = Get_Int_Keyboard("Enter the green value(0 to 255): ",0,255)
blue_color = Get_Int_Keyboard("Enter the blue value(0 to 255): ",0,255)
print ("Turning on LED# %d with red: %d, green: %d, blue: %d" % (LED_number, red_color, green_color, blue_color))
         
# Create NeoPixel object with appropriate configuration.
strip = neopixel.Adafruit_NeoPixel(ConfigMetarMap.LED_COUNT, ConfigMetarMap.LED_PIN, 
                                   ConfigMetarMap.LED_FREQ_HZ, ConfigMetarMap.LED_DMA, 
                                   ConfigMetarMap.LED_INVERT, ConfigMetarMap.LED_BRIGHTNESS, 
                                   ConfigMetarMap.LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
#Turn off all the LEDs
for i in range(strip.numPixels()):
    strip.setPixelColorRGB(i,0,0,0)
strip.show()
#Set LED and color
strip.setPixelColorRGB(LED_number - 1, red_color, green_color, blue_color)
#Write data to LED string
strip.show()
print("LED should be on!")
