#!/usr/bin/env python
# coding: utf-8
"""
__   __         _    _ _
\ \ / /__ _ __ | | _(_) |_
 \ V / _ \ '_ \| |/ / | __|
  | |  __/ |_) |   <| | |_
  |_|\___| .__/|_|\_\_|\__|
		 |_| http://yepkit.com/

Yepkit YKUSH Python API and command line tool

This application supports hidapi and hidapi-cffi, please choose
according to your preference:
  https://pypi.python.org/pypi/hidapi
	or
  https://pypi.python.org/pypi/hidapi-cffi

We invite you to visit the YKUSH product page for more information:
	https://www.yepkit.com/products/ykush

Copyright 2015, 2013 Yepkit Lda and other contributors
Released under the MIT license, please read the file LICENSE.txt
	https://github.com/Yepkit/pykush/blob/master/LICENSE

Date: 2016-10-01

# added YKUSHXS By Alber Saber
# Date: 2019-01-31

Command line usage:

	usage: pykush_hidapi.py [-h] [-s SERIAL]
							(-l | -u [UP [UP ...]] | -d [DOWN [DOWN ...]] | -p)

	Yepkit YKUSH command line tool.

	optional arguments:
	  -h, --help            show this help message and exit
	  -s SERIAL, --serial SERIAL
							specify the serial number string of the YKUSH to be
							listed or managed
	  -l, --list            list YKUSH devices
	  -u [UP [UP ...]], --up [UP [UP ...]]
							the downstream port numbers to power up, none means
							all
	  -d [DOWN [DOWN ...]], --down [DOWN [DOWN ...]]
							the downstream port numbers to power down, none
							means all
	  -p, --persist         make the current running configuration persistent
							across reboots (only supported on devices with
							firmware v2.0 and above)

Command line sample usage:

	$ python pykush.py -l
	listing YKUSH family devices
	  found a YKUSH release 2 device with serial number YK20001
		system device path 0001:000a:00, vendor id 0x04d8, product id 0xf2f7
		the device is running a v1.2 firmware and has 3 downstream ports
		downstream running power states, port 1 to 3: UP, UP, UP

	$ python pykush.py -d 1 2
	managing YKUSH family devices
	  found a YKUSH release 2 device with serial number YK20001
		system device path 0001:000a:00, vendor id 0x04d8, product id 0xf2f7
		the device is running a v1.2 firmware and has 3 downstream ports
		powering DOWN port 1... done
		powering DOWN port 2... done

	Note: depending on your system you may need priviledge elevation to access
		  the USB device:
			$ sudo python pykush.py -l
		  this can be avoided if you configure your machine to allow the
		  access, for more information please visit:
			https://github.com/Yepkit/pykush

Module sample usage:

	$ python
	>>> import pykush
	>>> yk = pykush.YKUSH()
	>>> yk.set_allports_state_up()
	True
	>>> yk.get_downstream_port_count()
	3
	>>> yk.set_port_state(2, pykush.YKUSH_PORT_STATE_DOWN)
	True
	>>> yk.get_port_state(2)
	0
	>>> yk.get_port_state(2) == pykush.YKUSH_PORT_STATE_DOWN
	True
	>>>

Notes:
  * None
  
Alber 31-01-2019 00:45am

YkushXs : 0xF0CD
Ykush3  : 0xF11B
Ykush2  : 0xEFED Legacy 0x0042
Ykush   : 0xF2F7  Legacy 0x0042

Sugest :
1.1.Add 0xf0cd in YKUSH_USB_PID_LIST[] ,and YKUSHXS mode
2.1.Delete 0xf0cd in YKUSH_USB_PID_BL_LIST[]
2.2.Add PreValue 0xffff
3.1.Find YKUSH_USB_PID_BL_LIST[] then check it in or == 
-incase of YKUSH_USB_PID_BL_LIST[] have only one value for bootloader mode, i suggest to add a prevalue
3.2.Add device is 0xf0cd
3.3.check if 0xf0cd:YKUSHXS Make it have 1 port
For 1.get_downstream_port_count()
    2.’has %i downstream’
    3.get_allports_state()
    4.’powering UP the downstream port’
    5.’powering DOWN the downstream port’
4.test
4.1.test (3.2).Test and End… ;)

New :
YKUSHXS
YKUSH_USB_PID_LIST = (0x0042, 0xf2f7, 0xf11b, 0xf0cd)
# YKUSH PIDs when in bootloader mode: YKUSH3, PreValue!!
YKUSH_USB_PID_BL_LIST = (0xf11c, 0xffff)

"""

from __future__ import unicode_literals
from __future__ import print_function
import sys
import struct
_usingHid = False
try:
	import hid
	_usingHid = True
except (ImportError, OSError):
	try:
		import hidapi
	except (ImportError, OSError):
		print('Please ensure that you have hidapi or hidapi-cffi installed,')
		print('any of them are supported.')
		print('If you are confortable with Python, it should be as simple as:')
		print('\tpip install --user hidapi')
		print('For more information please visit:')
		print('\thttps://github.com/Yepkit/pykush')
		raise

__version__ = '0.3.6'

# YKUSH device USB VID
YKUSH_USB_VID = 0x04d8
# YKUSH PIDs when in normal operation mode: YKUSH beta, YKUSH, YKUSH3, YKUSHXS (Alber1.1)
YKUSH_USB_PID_LIST = (0x0042, 0xf2f7, 0xf11b, 0xf0cd)
# YKUSH PIDs when in bootloader mode: YKUSH3!!, ABCD (Alber2.1.2)
YKUSH_USB_PID_BL_LIST = (0xf11c, 0xffff)

# YKUSH device USB comm declarations
YKUSH_USB_TIMEOUT = 1000  # timeout in ms
YKUSH_USB_PACKET_SIZE = 64
YKUSH_USB_PACKET_PAYLOAD_SIZE = 20

# YKUSH device protocol status declarations
YKUSH_PROTO_OK_STATUS = 1

# YKUSH port state meaning declarations
YKUSH_PORT_STATE_UP = 1
YKUSH_PORT_STATE_DOWN = 0
YKUSH_PORT_STATE_ERROR = 255
YKUSH_PORT_STATE_DICT = {0: "DOWN", 1: "UP", 255: "ERROR"}


def hid_enumerate(vid=0, pid=0):
	'''HID enumerate wrapper function'''
	for info in hid.enumerate(vid, pid) if _usingHid else hidapi.enumerate(vid, pid):
		if _usingHid:
			ret = info
		else:
			# unfortunately there is no __dict__ attr in the cffi DeviceInfo object
			ret = dict([(p, getattr(info, p)) for p in info.__slots__])
		yield ret


class YKUSHNotFound(Exception):
	'''YKUSH not found exception'''

	def __str__(self):
		return 'YKUSH device not found'


class YKUSH(object):

	'''YKUSH hidapi based interface class'''

	def __init__(self, serial=None, path=None):
		'''Constructor, the algorithm will connect to the first YKUSH found if a path or serial number is not provided'''
		self._devhandle = None
		self._firmware_major_version = None
		self._firmware_minor_version = None
		self._downstream_port_count = None
		#Alber3.2 add self._proudct_id
		self._proudct_id = None
		if path:
			# open the provided path
			if _usingHid:
				# blocking by default
				self._devhandle = hid.device()
				self._devhandle.open_path(path)
			else:
				# also blocking by default but ensure it is
				self._devhandle = hidapi.Device(path=path, blocking=True)
		else:
			# otherwise try to locate a device
			for device in hid_enumerate(0, 0):
				if device['vendor_id'] == YKUSH_USB_VID and device['product_id'] in YKUSH_USB_PID_LIST:
					if serial is None or serial == device['serial_number']:
						#Alber3.1 3.2 object attribute for YKUSHXS
						self._proudct_id = device['product_id']
						return self.__init__(path=device['path'])
		if self._devhandle is None:
			raise YKUSHNotFound()

	def __del__(self):
		'''Destructor, release the device'''
		if self._devhandle:
			self._devhandle.close()

	def get_product_string(self):
		'''Returns the device product string'''
		return self._devhandle.get_product_string()

	def get_serial_number_string(self):
		'''Returns the device serial number string'''
		return self._devhandle.get_serial_number_string()

	def get_firmware_version(self):
		'''Returns a tuple with YKUSH firmware version in format (major, minor)'''
		if self._firmware_major_version is None:
			status, major, minor = self._raw_sendreceive([0xf0])[:3]
			if status == YKUSH_PROTO_OK_STATUS:
				self._firmware_major_version, self._firmware_minor_version = (major, minor)
			else:
				# early devices will not recognize it, figure it out from serial
				self._firmware_major_version = 1
				self._firmware_minor_version = 2 if 'YK2' in self.get_serial_number_string() else 255 if 'YKD2' in self.get_serial_number_string() else 0
		return self._firmware_major_version, self._firmware_minor_version


	def get_downstream_port_count(self):
		'''Returns the YKUSH downstream port count'''
		if self._downstream_port_count is None:
			status, count = self._raw_sendreceive([0xf1])[:2]
			# hardware identifier 1 devices will not recognize the operation
			if status == YKUSH_PROTO_OK_STATUS:
				# YKUSH recognized the request
				self._downstream_port_count = count
			else:
				# original YKUSH 1,3 port count
				self._downstream_port_count = 3
			#Alber3.3 check if 0xf0cd:YKUSHXS Make it have 1 port
			if self._proudct_id == 0xf0cd:
				self._downstream_port_count = 1

		return self._downstream_port_count

	def get_port_state(self, port_number):
		'''Returns a specific downstream port state; returns 0 (port down), 1 (port up) or 255 (error)'''
		if port_number in range(1, self.get_downstream_port_count() + 1):
			status, port_state = self._raw_sendreceive([0x20 | port_number])[:2]
			if status == YKUSH_PROTO_OK_STATUS:
				return YKUSH_PORT_STATE_UP if port_state > 0x10 else YKUSH_PORT_STATE_DOWN
		return YKUSH_PORT_STATE_ERROR

	def get_allports_state(self):
		'''Returns all downstream port states; an array filled with 1 (port up), 0 (port down) or 255 (port error) in port order'''
		if self.get_firmware_version()[0] > 1:
			recvbytes = self._raw_sendreceive([0x2a])[:self.get_downstream_port_count() + 1]
			if recvbytes[0] == YKUSH_PROTO_OK_STATUS:
				return [YKUSH_PORT_STATE_UP if p > 0x10 else YKUSH_PORT_STATE_DOWN for p in recvbytes[1:self.get_downstream_port_count() + 1]]
			else:
				return [YKUSH_PORT_STATE_ERROR] * self.get_downstream_port_count()
		else:
			# firmware glitch workaround
			return [self.get_port_state(p) for p in range(1, self.get_downstream_port_count() + 1)]

	def get_allports_persistent_state(self):
		'''Returns all downstream persistent port states; an array filled with 1 (port up), 0 (port down) or 255 (port error) in port order'''
		recvbytes = self._raw_sendreceive([0x3a])[:self.get_downstream_port_count() + 1]
		if recvbytes[0] == YKUSH_PROTO_OK_STATUS:
			return [YKUSH_PORT_STATE_UP if p > 0x10 else YKUSH_PORT_STATE_DOWN for p in recvbytes[1:self.get_downstream_port_count() + 1]]
		elif self.get_firmware_version()[0] == 1:
			return [YKUSH_PORT_STATE_UP] * self.get_downstream_port_count()
		else:
			return [YKUSH_PORT_STATE_ERROR] * self.get_downstream_port_count()

	def set_port_state(self, port_number, new_state):
		'''Set a specific downstream port Up (1) or Down (0), returns True if the operation suceeded'''
		if port_number in range(1, self.get_downstream_port_count() + 1) and new_state in range(2):
			recvbytes = self._raw_sendreceive([(new_state == YKUSH_PORT_STATE_UP and 0x10 or 0x0) | port_number])
			return recvbytes[0] == YKUSH_PROTO_OK_STATUS
		else:
			return False

	def set_allports_state_down(self):
		'''Power down all YKUSH downstreams ports, returns True if the operation suceeded'''
		return self._raw_sendreceive([0x0a])[0] == YKUSH_PROTO_OK_STATUS

	def set_allports_state_up(self):
		'''Power up all YKUSH downstreams ports, returns True if the operation suceeded'''
		return self._raw_sendreceive([0x1a])[0] == YKUSH_PROTO_OK_STATUS

	def set_running_configuration_persistent(self):
		'''Make persistent the current device configuration, returns True if the operation suceeded'''
		if self.get_firmware_version()[0] > 1:
			return self._raw_sendreceive([0x3b])[0] == YKUSH_PROTO_OK_STATUS
		else:
			# unsupported on early firmware versions
			return False

	def _raw_sendreceive(self, packetarray):
		'''Internal method, submit a command and read the response from YKUSH'''
		# build the packet according to the report packet size
		# note: no buffer optimization was made for the sake of simplicity
		if _usingHid:
			packetarray = [0x00] + packetarray + [0x00] * (YKUSH_USB_PACKET_SIZE - len(packetarray))
			self._devhandle.write(packetarray)
			recvpacket = self._devhandle.read(max_length=YKUSH_USB_PACKET_SIZE + 1, timeout_ms=YKUSH_USB_TIMEOUT)
		else:
			packetarray = packetarray + [0x00] * (YKUSH_USB_PACKET_SIZE - len(packetarray))
			packet = struct.pack('<%dB' % YKUSH_USB_PACKET_SIZE, *packetarray)
			self._devhandle.write(packet)
			recvpacket = self._devhandle.read(length=YKUSH_USB_PACKET_SIZE + 1, timeout_ms=YKUSH_USB_TIMEOUT)
		# if not None return the bytes we actually need
		if recvpacket is None or len(recvpacket) < YKUSH_USB_PACKET_PAYLOAD_SIZE:
			return [0xff] * YKUSH_USB_PACKET_PAYLOAD_SIZE
		return recvpacket[:YKUSH_USB_PACKET_PAYLOAD_SIZE] if _usingHid else struct.unpack('<%iB' % YKUSH_USB_PACKET_PAYLOAD_SIZE, recvpacket[:YKUSH_USB_PACKET_PAYLOAD_SIZE])


def main():
	'''Just in case all you need is a command line tool'''
	from argparse import ArgumentParser

	# argument parser description
	parser = ArgumentParser(description='Yepkit YKUSH command line tool.')
	parser.add_argument('-s', '--serial', default=None, help='specify the serial number string of the YKUSH to be listed or managed')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-l', '--list', help='list YKUSH devices', action='store_true')
	group.add_argument('-u', '--up', type=int, nargs='*',
					   help='the downstream port numbers to power up, none means all')
	group.add_argument('-d', '--down', type=int, nargs='*',
					   help='the downstream port numbers to power down, none means all')
	group.add_argument('-p', '--persist', default=None,
					   help='make the current running configuration persistent across reboots (only supported on devices with firmware v2.0 and above)',
					   action='store_true')
	args = parser.parse_args()

	# say hello
	print('%s YKUSH family devices%s' %
		  (args.list and 'listing' or 'managing',
		   args.serial is None and ' ' or ' with serial number %s' % (args.serial)))
	try:
		ykush_found = False
		for device in hid_enumerate(0, 0):
			if device['vendor_id'] == YKUSH_USB_VID and device['product_id'] in YKUSH_USB_PID_LIST + YKUSH_USB_PID_BL_LIST:
				if args.serial is None or args.serial == device['serial_number']:
					ykush_found = True
					print('  found a %s release %s device with serial number %s' %
						  (device['product_string'], device['release_number'], device['serial_number']))
					print('    system device path %s, vendor id 0x%.4x, product id 0x%.4x' % (device['path'].decode(), device['vendor_id'], device['product_id']))
					if device['product_id'] in YKUSH_USB_PID_BL_LIST:
						print('    control functions are not available, the device is working in bootloader mode')
					else:
						ykush = None
						try:
							ykush = YKUSH(path=device['path'])
							#Alber3.3 check if YKUSHXS make it 1 port
							if  device['product_id'] == 0xf0cd:
								print('    the device has 1 downstream port')
							else:
								print('    the device is running a v%i.%i firmware and has %i downstream ports' % (ykush.get_firmware_version() + (ykush.get_downstream_port_count(),)))
						except IOError:
							if args.list:
								print('    warning: could not communicate, the device may be in use or')
								print('    your user do not have access rights to do so, in the latter')
								print('    case you may work around the by using sudo, for example:')
								print('      sudo python pykush.py -l')
								print('    if you are using the binary version:')
								print('      sudo pykush -l')
							else:
								raise
						if ykush:
							cmds = []
							if args.list:
								# list requested, attempting to get all port states
								t = ykush.get_allports_state()
								#Alber3.3 check if YKUSHXS the make it 1 port--
								if device['product_id'] == 0xf0cd:
									tt = t[0]
									print('    Checking running power state, port 1 : ' + YKUSH_PORT_STATE_DICT[tt])
								else:
									print('    downstream running power states, port 1 to %i: %s' %
										(ykush.get_downstream_port_count(), ', '.join([YKUSH_PORT_STATE_DICT[s] for s in t])))
									# YKUSH firmware below v2 does not support persistence functions
									if ykush.get_firmware_version()[0] > 1:
										t = ykush.get_allports_persistent_state()
										if t[0] != YKUSH_PORT_STATE_ERROR:
											print('    downstream startup/persistent power states, port 1 to %i: %s' %
												  (ykush.get_downstream_port_count(), ', '.join([YKUSH_PORT_STATE_DICT[s] for s in t])))
							if args.up is not None:
								if len(args.up) == 0:
									#Alber3.3 check if YKUSHXS the make it 1 port--
									if device['product_id'] == 0xf0cd:
										print('    powering UP the downstream port... ', end='')
										print('done' if ykush.set_allports_state_up() else 'unexpected error')
									else:
										print('    powering UP all downstream ports... ', end='')
										print('done' if ykush.set_allports_state_up() else 'unexpected error')
								else:
									cmds += zip(args.up, [YKUSH_PORT_STATE_UP for _ in range(len(args.up))])
							if args.down is not None:
								if len(args.down) == 0:
									#Alber3.3 check if YKUSHXS the make it 1 port--
									if device['product_id'] == 0xf0cd:
										print('    powering DOWN the downstream port... ', end='')
										print('done' if ykush.set_allports_state_down() else 'unexpected error')
									else :
										print('    powering DOWN all downstream ports... ', end='')
										print('done' if ykush.set_allports_state_down() else 'unexpected error')
								else:
									cmds += zip(args.down, [YKUSH_PORT_STATE_DOWN for _ in range(len(args.down))])
							for cfg in cmds:
								print('    powering %s port %i... ' % (YKUSH_PORT_STATE_DICT[cfg[1]], cfg[0]), end='')
								print('done' if ykush.set_port_state(cfg[0], cfg[1]) else 'error, could not configure the specified port number')
							if args.persist:
								if ykush.get_firmware_version()[0] > 1:
									print('    making running device configuration persistent... ', end='')
									print('done' if ykush.set_running_configuration_persistent() else 'unexpected error')
								else:
									print('    error, command only supported on devices with firmware v2.0 and above')
		if not ykush_found:
			print('no YKUSH devices found')
	except (ValueError, IOError, OSError) as e:
		print('communication error, exception details:')
		print('  error "%s"' % e.message)
		sys.exit(1)


if __name__ == '__main__':
	main()

