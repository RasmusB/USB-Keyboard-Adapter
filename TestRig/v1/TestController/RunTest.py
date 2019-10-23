import ArduinoHandler

from pymata_aio.constants import Constants
from time import sleep

used_pins_MASTER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 18, 19, 20, 21, 22, 23]
used_pins_DUT = [23, 22, 21, 20, 19, 18, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def run_test():
    boards = ArduinoHandler.get_all_boards()

    set_all_pins_as_input(boards["DUT"], used_pins_DUT)
    set_all_pins_as_output(boards["MASTER"], used_pins_MASTER)

    print("No pins high:", read_all_used_digital_pins(boards["DUT"], used_pins_DUT))

    for pin in range(0, 30):

        boards["MASTER"].digital_pin_write(pin, 1)

        sleep(0.25)
        print("With pin", pin, "high:", read_all_used_digital_pins(boards["DUT"], used_pins_DUT))

        boards["MASTER"].digital_pin_write(pin, 0)

    print("done")


def set_all_pins_as_input(board, pins):
    for pin in range(0, 31):
        board.set_pin_mode(pin, Constants.INPUT)
    return


def set_all_pins_as_output(board, pins):
    for pin in range(0, 31):
        board.set_pin_mode(pin, Constants.OUTPUT)
    return


def read_all_used_digital_pins(board, used_pins):

    result = []

    for pin in used_pins:
        result.append(board.digital_read(pin))

    return result


if __name__ == "__main__":
    run_test()
