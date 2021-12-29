import os
import sys
import time
import serial
import serial.tools.list_ports
import pykush

serialPorts = []

serialPort_testRig = ""
serialPort_avrISP = ""
serialPort_DUTs = [None, None, None, None]
passed_DUTs = [None, False, False, False]

testPatternGPIO = []
testPatternGPIO.append("00000000000000000000")
testPatternGPIO.append("00000000000000000001")
testPatternGPIO.append("00000000000000000010")
testPatternGPIO.append("00000000000000000100")
testPatternGPIO.append("00000000000000001000")
testPatternGPIO.append("00000000000000010000")
testPatternGPIO.append("00000000000000100000")
testPatternGPIO.append("00000000000001000000")
testPatternGPIO.append("00000000000010000000")
testPatternGPIO.append("00000000000100000000")
testPatternGPIO.append("00000000001000000000")
testPatternGPIO.append("00000000010000000000")
testPatternGPIO.append("00000000100000000000")
testPatternGPIO.append("00000001000000000000")
testPatternGPIO.append("00000010000000000000")
testPatternGPIO.append("00000100000000000000")
testPatternGPIO.append("00001000000000000000")
testPatternGPIO.append("00010000000000000000")
testPatternGPIO.append("00100000000000000000")
testPatternGPIO.append("01000000000000000000")
testPatternGPIO.append("10000000000000000000")
testPatternGPIO.append("00000000000000000000")

serialDelay = 0.1

eraseFlashCommand = "avrdude -C avrdude.conf -patmega32u4 -cstk500v2 -e -B50 -V "
fuseFlashCommand = "avrdude -C avrdude.conf -patmega32u4 -cstk500v2 -e -Uefuse:w:0xcb:m -Uhfuse:w:0xd8:m -Ulfuse:w:0xff:m -B50 -V "
bootFlashCommand = "avrdude -C avrdude.conf -patmega32u4 -cstk500v2 -Uflash:w:Caterina-Leonardo.hex:i -B0.5 -D -V "
arduinoFlashCommand = "avrdude -C avrdude.conf -patmega32u4 -cavr109 -b57600 -D "


class TestRig:
    """Contains the state of the test rig"""
    lastRX = ""

    def __init__(self, serialPortName):
        self.serialPort = serial.Serial(serialPortName)
        self.serialPort.flushInput()

    def _serialCMDResponse(self, cmdString):
        self.serialPort.reset_input_buffer()
        self.serialPort.write(cmdString.encode('ascii'))

        time.sleep(serialDelay)
        # Drop reaction line
        temp = self.serialPort.readline()

        resultString = self.serialPort.readline()
        self.serialPort.reset_input_buffer()
        return resultString

    def _serialCMDOnly(self, cmdString):
        self.serialPort.reset_input_buffer()
        self.serialPort.write(cmdString.encode('ascii'))
        time.sleep(serialDelay)
        self.serialPort.reset_input_buffer()
        return

    def setDUT(self, dutNo):
       if 0 < dutNo < 4:
            result = self._serialCMDResponse('dut ' + chr(dutNo+0x30) + '\n')
            if result == b'OK\r\n':
                pass
                # print("Selected DUT", dutNo)
            else:
                print("ERROR! Failed to select DUT", dutNo)
                print("Got response:", result)
       else:
           print("ERROR: DUT", dutNo, "does not exist!")

    def getDUT(self):
        result = self._serialCMDResponse('dut\n')
        return int(result)

    def measureVbus(self):
        # Read serial data
        result = self._serialCMDResponse('vbus\n')
        tokens = result.split()

        return int(tokens[0])

    def ledOn(self, ledNo):
        self._serialCMDOnly('led on ' + chr(0x30 + ledNo) + '\n')
        return

    def ledOff(self, ledNo):
        self._serialCMDOnly('led off ' + chr(0x30 + ledNo) + '\n')
        return

    def ledOffAll(self):
        for dutNo in range(1, 4):
            self.setDUT(dutNo)
            for ledNo in range(1, 5):
                self._serialCMDOnly('led off ' + chr(0x30 + ledNo) + '\n')
        return

    def readPin(self, pinNo=None):
        if pinNo is None:
            result = self._serialCMDResponse('read_pin\n')
        else:
            result = self._serialCMDResponse('read_pin ' + pinNo + '\n')

        return str(result.decode())

    def testGPIO(self, patterns, dutSerialPort):
        result = True
        for i, pattern in enumerate(patterns):
            dutSerialPort.write(pattern.encode('ascii'))
            dutSerialPort.write('\n'.encode('ascii'))
            time.sleep(serialDelay)
            response = self.readPin()
            if response[:20] != pattern:
                print("Mismatch on pattern no.", str(i) + '.', "Expected", pattern, "but got", response[:20])
                result = False
        return result

    def eraseDUTFlash(self):
        command = eraseFlashCommand + "-P" + serialPort_avrISP
        result = os.system(command)
        if result == 0:
            return True
        else:
            return False
        pass

    def flashFuses(self):
        command = fuseFlashCommand + "-P" + serialPort_avrISP
        result = os.system(command)
        if result == 0:
            return True
        else:
            return False
        pass

    def flashBootloader(self):
        command = bootFlashCommand + "-P" + serialPort_avrISP
        result = os.system(command)
        if result == 0:
            return True
        else:
            return False
        pass

    def _enterArduinoBootloader(self, arduinoSerialPort):
        dutResetPort = serial.Serial(port=arduinoSerialPort.device, baudrate=1200)
        time.sleep(0.1)
        dutResetPort.close()
        return

    def flashApplication(self, arduinoSerialPort, applicationFile):
        # This serves as a test of the arduino bootloader
        # Force reset by opening/closing serial port at 1200 baud
        initialComports = serial.tools.list_ports.comports()
        # print("Trying to reset DUT on port", arduinoSerialPort.device, "(", arduinoSerialPort.description, ")")
        self._enterArduinoBootloader(arduinoSerialPort)

        # Wait for DUT to reset
        while arduinoSerialPort in initialComports:
            time.sleep(0.1)
            initialComports = serial.tools.list_ports.comports()

        # Wait for bootloader to start
        while len(initialComports) == len(serial.tools.list_ports.comports()):
            time.sleep(0.1)

        for comport in serial.tools.list_ports.comports():
            if comport not in initialComports:
                dutBootloaderPort = comport
                break

        command = arduinoFlashCommand + "-P" + dutBootloaderPort.device + " -Uflash:w:" + applicationFile + ":i"
        # print("Trying to flash DUT on port", dutBootloaderPort.device, "(", dutBootloaderPort.description, ")")
        result = os.system(command)
        if result == 0:
            return True
        else:
            return False
        pass


# Start by listing all serial ports and figuring out which is which
# Before any DUT is powered on, we should see the test rig and also the AVR-ISP
for comport in serial.tools.list_ports.comports():

    # Identify the test rig
    if comport.vid == 1155 and comport.pid == 22336:
        if serialPort_testRig == "":
            serialPort_testRig = comport.device
            print("Test rig found on", serialPort_testRig)
            testrig = TestRig(serialPort_testRig)
        else:
            print("ERROR! Found another test rig on", comport.device)

    # Identify the AVR ISP programmer
    if comport.vid == 6790 and comport.pid == 29987:
        if serialPort_avrISP == "":
            serialPort_avrISP = comport.device
            print("AVR ISP found on", serialPort_avrISP)
        else:
            print("ERROR! Found another AVR ISP on", comport.device)

# Turn off all LEDs
testrig.ledOffAll()

# Now, let's power on a DUT
usbhub = pykush.YKUSH()
print("Found hub with", usbhub.get_downstream_port_count(), "ports")

for currentDUTNo in range(1, 4):
    usbhub.set_allports_state_down()
    testrig.setDUT(currentDUTNo)

    # Enable USB port for current dut
    usbhub.set_port_state(currentDUTNo, pykush.YKUSH_PORT_STATE_UP)

    # Wait for power to come on
    time.sleep(0.5)

    # Measure DUT voltage
    dutmV = testrig.measureVbus()
    if not (4500 < dutmV < 5500):
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Vbus out of range, is", dutmV, "mV")
        continue
    else:
        print("DUT", currentDUTNo, "Vbus is OK -", dutmV, "mV")

    # Start the ISP phase
    testrig.ledOn(2)

    # Erase everything
    result = testrig.eraseDUTFlash()
    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Erasing flash failed")
        continue
    else:
        print("DUT", currentDUTNo, "flash memory erased")

    # Flash the fuses
    result = testrig.flashFuses()
    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Flashing fuses failed")
        continue
    else:
        print("DUT", currentDUTNo, "fuses programmed")

    # Flash the bootloader
    result = testrig.flashBootloader()
    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Flashing bootloader failed")
        continue
    else:
        print("DUT", currentDUTNo, "bootloader programmed")

    # See if the DUT enumerates over USB after a power cycle
    print("DUT", currentDUTNo, "rebooting, please wait...")
    usbhub.set_port_state(currentDUTNo, pykush.YKUSH_PORT_STATE_DOWN)
    time.sleep(1)
    serialPorts = serial.tools.list_ports.comports()
    usbhub.set_port_state(currentDUTNo, pykush.YKUSH_PORT_STATE_UP)
    time.sleep(1)

    for comport in serial.tools.list_ports.comports():
        if comport not in serialPorts:
            if comport.vid == 9025 and comport.pid == 32822:
                serialPort_DUTs[currentDUTNo] = comport

    if serialPort_DUTs[currentDUTNo] is None:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! USB did not enumerate after reboot")
        continue
    else:
        print("DUT", currentDUTNo, "USB back online")

    # ISP phase finished
    testrig.ledOff(2)

    # Arduino phase started
    testrig.ledOn(3)

    # Let's try to flash the test FW
    result = testrig.flashApplication(serialPort_DUTs[currentDUTNo], "testrigFW.ino.hex")
    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Could not flash test FW over USB")
        continue
    else:
        print("DUT", currentDUTNo, "application programmed")


    # Wait for DUT USB serial to come back
    while serialPort_DUTs[currentDUTNo] not in serial.tools.list_ports.comports():
        time.sleep(0.1)

    print("DUT", currentDUTNo, "GPIO test started...")

    dutSerialPort = serial.Serial(serialPort_DUTs[currentDUTNo].device)

    # Now let's test the stuff
    result = testrig.testGPIO(testPatternGPIO, dutSerialPort)
    dutSerialPort.close()

    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! GPIO test failed!")
        continue
    else:
        print("DUT", currentDUTNo, "GPIO test PASS")

    # Flash the shipping FW
    print("DUT", currentDUTNo, "flashing final application...")
    result = testrig.flashApplication(serialPort_DUTs[currentDUTNo], "Psion-Keyboard-Firmware.ino.hex")
    if result is False:
        testrig.ledOn(1)
        print("DUT", currentDUTNo, "ERROR! Could not flash production FW over USB")
        continue
    else:
        print("DUT", currentDUTNo, "final appliaction programmed")

    # Disable USB port for current dut
    usbhub.set_port_state(currentDUTNo, pykush.YKUSH_PORT_STATE_DOWN)
    testrig.ledOff(3)
    testrig.ledOn(4)

    print("DUT", currentDUTNo, "all tests PASSED!")
    passed_DUTs[currentDUTNo] = True

# Turn off power for all DUTs
usbhub.set_allports_state_down()

# Print the complete results
for currentDUTNo in range(1, 4):
    if passed_DUTs[currentDUTNo] == True:
        print("DUT", currentDUTNo, "PASS")
    else:
        print("DUT", currentDUTNo, "FAIL")

pass