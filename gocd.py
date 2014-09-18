import os
import requests
import xml.etree.ElementTree as ET

from requests.auth import HTTPBasicAuth

def _cctray(server):
    res = requests.get("%s/go/cctray.xml" % server,
                       auth=HTTPBasicAuth(os.environ['CCUSER'], os.environ['CCPASS']),
                       timeout=1)
    return ET.fromstring(res.text)

def stages_for_pipeline(projects, name):
    return [p for p in projects if p.attrib['name'].startswith(name)]

def activities_for_pipeline(server, pipeline):
    xml = _cctray(server)
    projects = xml.findall(".//Project")

    return [s.attrib['activity'] for s in stages_for_pipeline(projects, pipeline)]

def statuses_for_pipeline(server, pipeline):
    xml = _cctray(server)
    projects = xml.findall(".//Project")

    return [s.attrib['lastBuildStatus'] for s in stages_for_pipeline(projects, pipeline)]

def is_building(server, pipeline):
    activities = activities_for_pipeline(server, pipeline)

    return reduce(lambda m, i: m or (i == "Building"), activities, False)

def is_failed(server, pipeline):
    statuses = statuses_for_pipeline(server, pipeline)

    return reduce(lambda m, i: m or (i == "Failure"), statuses, False)

