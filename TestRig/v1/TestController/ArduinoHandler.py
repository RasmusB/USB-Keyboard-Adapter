import os

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


def find_arduinos():

    port_listing = os.popen("list_serial_ports").read()

    temp_ports = str.split(port_listing, "\n")
    available_arduinos = []

    for item in temp_ports:
        temp = str.split(item, ":")
        if temp[0] != '':
            if "Arduino" in temp[1]:
                available_arduinos.append(temp[0])

    return available_arduinos

def check_for_firmata(port_list):

    boards = {}

    for port in port_list:
        temp_board = PyMata3(com_port=port)

        temp_fw_string = temp_board.get_firmware_version()

        if "TestRig-FW.ino" in temp_fw_string :
            boards["MASTER"] = temp_board
        elif "DUT-FW.ino" in temp_fw_string :
            boards["DUT"] = temp_board

    return boards

def get_all_boards():
    return check_for_firmata(find_arduinos())

if __name__ == "__main__":
    boards = check_for_firmata(find_arduinos())
    pass

