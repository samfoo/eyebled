import sys
import time
import requests
import serial

import xml.etree.ElementTree as ET

url = "http://whatever"
current_build_state = "green"

def connect_to_serial():
    port = "/dev/ttyACM0"
    print "connecting to serial port %s" % port

    leds = serial.Serial(port, 9600)
    leds.write("!")
    handshake = leds.read()

    if handshake != "?":
        print sys.stderr, "Invalid handshake"
        sys.exit(1)

def update_led_state():
    commands = {
        "green": "G",
        "building": "B",
        "building-after-red": "C",
        "red": "R"
    }
    
    leds.write(comands[current_build_state])

def find_status_by_project(xml, proj):
    return activity_from_cctray

def activity_from_cctray(xml, proj):
    project_node = xml.findall(".//*[@name='%s']" % proj)
    activities = {
        'Sleeping',
        'Building'
    }
    return project_node.attrib['activity']

def cctray_xml():
    # TODO: Replace with your cctray location
    # res = requests.get("%s/go/cctray.xml" % url)
    return """<?xml version="1.0" encoding="utf-8"?>
<Projects>
  <Project name="convoy :: Build-Unit-Test" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T18:53:05" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/convoy/2600/Build-Unit-Test/1" />
  <Project name="convoy :: Build-Unit-Test :: rspec-unit" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T18:53:05" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2600/Build-Unit-Test/1/rspec-unit" />
  <Project name="convoy :: Build-Unit-Test :: js" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T18:48:58" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2600/Build-Unit-Test/1/js" />
  <Project name="convoy :: Build-Unit-Test :: code-smells" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T18:50:01" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2600/Build-Unit-Test/1/code-smells" />
  <Project name="convoy :: Functional-Test" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T19:02:33" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/convoy/2600/Functional-Test/1" />
  <Project name="convoy :: Functional-Test :: cucumber" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2600" lastBuildTime="2010-08-06T19:02:33" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2600/Functional-Test/1/cucumber" />
  <Project name="convoy :: Manual-Deploy-To-UAT" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2596" lastBuildTime="2010-08-06T15:26:42" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/convoy/2596/Manual-Deploy-To-UAT/1" />
  <Project name="convoy :: Manual-Deploy-To-UAT :: Deploy-Migrate-Seed" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2596" lastBuildTime="2010-08-06T15:26:42" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2596/Manual-Deploy-To-UAT/1/Deploy-Migrate-Seed" />
  <Project name="convoy :: Manual-Deploy-To-Pacifico" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2596" lastBuildTime="2010-08-06T15:28:59" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/convoy/2596/Manual-Deploy-To-Pacifico/1" />
  <Project name="convoy :: Manual-Deploy-To-Pacifico :: Deploy-Migrate-Seed" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="2596" lastBuildTime="2010-08-06T15:28:59" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/convoy/2596/Manual-Deploy-To-Pacifico/1/Deploy-Migrate-Seed" />
  <Project name="Regression :: Setup" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="122" lastBuildTime="2010-08-07T10:02:09" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/Regression/122/Setup/1" />
  <Project name="Regression :: Setup :: run-setup-tests" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="122" lastBuildTime="2010-08-07T10:02:09" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/Regression/122/Setup/1/run-setup-tests" />
  <Project name="Regression :: Regression" activity="Sleeping" lastBuildStatus="Failure" lastBuildLabel="122" lastBuildTime="2010-08-07T10:56:50" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/Regression/122/Regression/1" />
  <Project name="Regression :: Regression :: run-all-functional-tests" activity="Sleeping" lastBuildStatus="Failure" lastBuildLabel="122" lastBuildTime="2010-08-07T10:56:50" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/Regression/122/Regression/1/run-all-functional-tests" />
  <Project name="release-candidate :: Build-Unit-Test" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:36:18" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/release-candidate/350/Build-Unit-Test/1" />
  <Project name="release-candidate :: Build-Unit-Test :: rspec-unit" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:36:18" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Build-Unit-Test/1/rspec-unit" />
  <Project name="release-candidate :: Build-Unit-Test :: javascript-specs" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:33:15" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Build-Unit-Test/1/javascript-specs" />
  <Project name="release-candidate :: Build-Unit-Test :: code-smells" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:30:48" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Build-Unit-Test/1/code-smells" />
  <Project name="release-candidate :: Functional-Test" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:47:53" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/release-candidate/350/Functional-Test/1" />
  <Project name="release-candidate :: Functional-Test :: cucumber" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-04T19:47:53" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Functional-Test/1/cucumber" />
  <Project name="release-candidate :: Manual-Deploy-To-UAT" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-05T09:56:25" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/release-candidate/350/Manual-Deploy-To-UAT/1" />
  <Project name="release-candidate :: Manual-Deploy-To-UAT :: Deploy-Migrate-Seed" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-05T09:56:25" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Manual-Deploy-To-UAT/1/Deploy-Migrate-Seed" />
  <Project name="release-candidate :: Manual-Deploy-To-Pacifico" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-05T12:39:10" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/release-candidate/350/Manual-Deploy-To-Pacifico/1" />
  <Project name="release-candidate :: Manual-Deploy-To-Pacifico :: Deploy-Migrate-Seed" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="350" lastBuildTime="2010-08-05T12:39:10" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/release-candidate/350/Manual-Deploy-To-Pacifico/1/Deploy-Migrate-Seed" />
  <Project name="branch-regression :: Setup" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="76" lastBuildTime="2010-08-05T10:28:10" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/branch-regression/76/Setup/1" />
  <Project name="branch-regression :: Setup :: run-setup-tests" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="76" lastBuildTime="2010-08-05T10:28:10" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/branch-regression/76/Setup/1/run-setup-tests" />
  <Project name="branch-regression :: Regression" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="76 :: 2" lastBuildTime="2010-08-05T12:28:46" webUrl="http://10.12.1.65:8153/cruise/tab/stage/detail/branch-regression/76/Regression/2" />
  <Project name="branch-regression :: Regression :: run-all-functional-tests" activity="Sleeping" lastBuildStatus="Success" lastBuildLabel="76 :: 2" lastBuildTime="2010-08-05T12:28:46" webUrl="http://10.12.1.65:8153/cruise/tab/build/detail/branch-regression/76/Regression/2/run-all-functional-tests" />
</Projects>"""

def parse_cctray(xml):
    return ET.fromstring(xml)

def get_build_state(proj):
    xml = cctray_xml()
    root = parse_cctray(xml)

    return find_status_by_project(root, proj)

def poll_for_build_state(proj):
    while True:
        new_build_state = get_build_state(proj)

        if new_build_state != current_build_state:
            current_build_state = new_build_state
            update_led_state()

        time.sleep(30)

if __name__ == "__main__":
    connect_to_serial()
    poll_for_build_state("onboardingwebclient")

