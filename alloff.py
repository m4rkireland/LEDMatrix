# alloff.py - turns off all LEDs on a WS2811 string
# Useful if your real program crashes and you need
# to turn off the LEDs. By Andrew Oakley aoakley.com
#
# Based on NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)

import time

from neopixel import *

# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
#LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
#LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
#LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


def allonecolour(strip,colour):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i,colour)
  strip.show()

def colour(r,g,b):
  # Fix for Neopixel RGB->GRB, also British spelling
  return Color(g,r,b)

def initLeds(strip):
  # Intialize the library (must be called once before other functions).
  strip.begin()
  # Initialise LEDs by briefly setting them all to white
  allonecolour(strip,colour(255,255,255))
  time.sleep(0.01)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
initLeds(strip)

# All off
allonecolour(strip,colour(0,0,0))

