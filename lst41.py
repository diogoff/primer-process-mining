import datetime
import xml.etree.ElementTree as ET

tree = ET.parse('financial_log.xes') # get this file from here: https://data.4tu.nl/repository/uuid:3926db30-f712-4394-aebc-75976070e91f
root = tree.getroot()

ns = {'xes': 'http://www.xes-standard.org/'}

for trace in root.findall('xes:trace', ns):
    caseid = ''
    for string in trace.findall('xes:string', ns):
        if string.attrib['key'] == 'concept:name':
            caseid = string.attrib['value']
    for event in trace.findall('xes:event', ns):
        task = ''
        user = ''
        event_type = ''
        for string in event.findall('xes:string', ns):
            if string.attrib['key'] == 'concept:name':
                task = string.attrib['value']
            if string.attrib['key'] == 'org:resource':
                user = string.attrib['value']
            if string.attrib['key'] == 'lifecycle:transition':
                event_type = string.attrib['value']
        timestamp = ''
        for date in event.findall('xes:date', ns):
            if date.attrib['key'] == 'time:timestamp':
                timestamp = date.attrib['value']
                timestamp = datetime.datetime.strptime(timestamp[:-10],
                                                                    '%Y-%m-%dT%H:%M:%S')
        print ';'.join([caseid, task, event_type, user, str(timestamp)])
