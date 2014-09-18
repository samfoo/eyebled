import sys
import time
import serial

import gocd

server = "http://10.29.112.178:8153"
def connect_to_serial():
    port = "/dev/ttyACM0"
    print "connecting to serial port %s" % port

    leds = serial.Serial(port, 9600)
    leds.write("!")
    handshake = leds.read()

    if handshake != "?":
        print sys.stderr, "Invalid handshake"
        sys.exit(1)

def update_led_state(state):
    commands = {
        "green": "G",
        "building": "B",
        "building-after-red": "C",
        "red": "R"
    }

    print "updating leds to %s" % commands[state]
    # leds.write(commands[current_build_state])

def poll_for_build_state(proj):
    current_build_state = "green"

    while True:
        if gocd.is_building(server, "onboarding-web-client"):
            new_build_state = "building"
        elif gocd.is_failed(server, "onboarding-web-client"):
            new_build_state = "red"
        else:
            new_build_state = "green"

        if new_build_state != current_build_state:
            current_build_state = new_build_state
            update_led_state(current_build_state)

        time.sleep(5)

if __name__ == "__main__":
    # connect_to_serial()
    poll_for_build_state("onboarding-web-client")

