#!/usr/bin/env python3
__author__ = 'RasmusB'

### A script to flash a blank ATmega32U4 with the leonardo bootloader

import os
import sys
import time

comport = sys.argv[1]

command1 = "avrdude -C avrdude.conf -v -patmega32u4 -cstk500v2 -P" + comport + " -e -Uefuse:w:0xcb:m -Uhfuse:w:0xd8:m -Ulfuse:w:0xff:m -B50"
command2 = "avrdude -C avrdude.conf -v -patmega32u4 -cstk500v2 -P " + comport + " -Uflash:w:Caterina-Leonardo.hex:i -B0.5"

result = os.system(command1)

if result == 0:
    print("Fuses set successfully")
    os.system(command2)
else:
    print("Setting fuses failed! Aborting...")
