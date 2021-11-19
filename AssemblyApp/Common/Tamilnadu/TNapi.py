from urllib.request import urlopen
import xmltodict
import json
from pathlib import Path


def get_districts():
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'RevDistrict.json'
    with open(file_location, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        data.sort(key=lambda x: x.get('Display'))
        return data


def get_taluk(districtCode):
    file = urlopen(f'https://eservices.tn.gov.in/eservicesnew/land/ajax.html?page=taluk&districtCode={districtCode}')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    r = json.dumps(data)
    jsonResult = json.loads(r)['root']['taluk']
    return jsonResult

def get_villages(districtCode, talukCode):
    file = urlopen(f'https://eservices.tn.gov.in/eservicesnew/land/ajax.html?page=village&districtCode={districtCode}&talukCode={talukCode}')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    r = json.dumps(data)
    jsonResult = json.loads(r)['root']['village']
    return jsonResult


def get_subdiv(districtCode, talukCode, villageCode, surveyno):
    file = urlopen(
        f'https://eservices.tn.gov.in/eservicesnew/land/ajax.html?page=getSubdivNo&districtCode={districtCode}&talukCode={talukCode}&villageCode={villageCode}&surveyno={surveyno}')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    d = []
    for x in data['root']['subdiv']:
        d.append(x['subdivcode'])
    return d
