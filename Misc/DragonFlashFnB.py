#!/usr/bin/env python3
__author__ = 'RasmusB'

### A script to flash a blank ATmega32U4 with the leonardo bootloader

import os
import time

os.system("avrdude -C avrdude.conf -v -p atmega32u4 -c dragon_isp -P usb -e -Uefuse:w:0xcb:m -Uhfuse:w:0xd8:m -Ulfuse:w:0xff:m -B50")

print("Waiting for programmer...")
time.sleep(3)

os.system("avrdude -C avrdude.conf -v -p atmega32u4 -c dragon_isp -P usb -Uflash:w:Caterina-Leonardo.hex:i -B1")
