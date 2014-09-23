import sys
import time
import serial

import gocd

server = "http://10.29.112.178:8153"
def connect_to_serial():
    leds = serial.Serial("/dev/ttyACM0", 9600)
    time.sleep(2)
    leds.write("!")

    handshake = leds.read()

    if handshake != "?":
        print sys.stderr, "Invalid handshake"
        sys.exit(1)

    print "connected!"

    return leds

def update_led_state(leds, state):
    commands = {
        "green": "G",
        "building": "B",
        "building-after-red": "C",
        "red": "R"
    }

    print "updating leds to %s" % commands[state]
    leds.write(commands[state])

def poll_for_build_state(proj):
    leds = connect_to_serial()

    print "starting to poll for build state"
    current_build_state = "green"

    while True:
        if gocd.is_building(server, proj):
            new_build_state = "building"
        elif gocd.is_failed(server, proj):
            new_build_state = "red"
        else:
            new_build_state = "green"

        if new_build_state != current_build_state:
            current_build_state = new_build_state
            update_led_state(leds, current_build_state)

        time.sleep(1)

if __name__ == "__main__":
    poll_for_build_state("onboarding-web-client")

