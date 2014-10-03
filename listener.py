#!/usr/bin/env python

import serial
from time import sleep
import requests
import json

def main(): 
  print 'hello'
  ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
  highs = 0
  lows = 0
  flag = 0
  headers = {'content-type': 'application/json'}
  AUTH_TOKEN = "4b2d547ec08efb04fbf341bb947a7ae0"
  CR_URL = "http://darna-app.herokuapp.com/api/p/cr"

  while True:
    sleep(0.1)
    state = ser.readline()
    if 'HIGH' in state:
      lows = 0
      highs += 1
    if 'LOW' in state:
      high = 0
      lows += 1

    print "high -> %s  :: lows -> %s :: last -> %s" % (highs, lows,'aaa') 

    maytaoba = False
    if lows > 10:
      maytaoba = True
      highs = 0
    if maytaoba and highs > 5:
      maytaoba = False


    if lows == 11:
      print 'Wala to Meron'
      payload = {"auth_token": AUTH_TOKEN, "name": "maytaoba", "value": {"maytaoba":"meron"}}
      r = requests.post(CR_URL, data=json.dumps(payload), headers=headers)
      print r.text

    if highs == 5:
      print "Meron to Wala"
      payload = {"auth_token": AUTH_TOKEN, "name": "maytaoba", "value": {"maytaoba":"wala"}}
      r = requests.post(CR_URL, data=json.dumps(payload), headers=headers)
      print r.text
      

    print 'Meron' if maytaoba else "Wala"

if __name__ == '__main__': 
  main()
