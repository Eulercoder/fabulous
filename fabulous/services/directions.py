"""~directions "<start>" "<end>" (in quotes) return a result from the google maps result for directions from <start> to <end>"""

import re
import requests
import googlemaps
from googlemaps import Client as GoogleMaps
from secret_example import GOOGLE_DIRECTION_API
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

ERROR_MSG = "Some unknown error occured"
DIRECTIONS_BASEURL = "http://maps.googleapis.com/maps/api/directions/json"
#to strip HTML tags from the html_instructions string
class MLStripper(HTMLParser):
    def __init__(self):
        try:
            self.reset()
            self.strict = False
            self.convert_charrefs= True
        except:
            self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def unescape(url):
    # for unclear reasons, google replaces url escapes with \x escapes
    return url.replace(r"\x", "%")

def directions(start, end, unsafe=False):

    mapService = GoogleMaps(GOOGLE_DIRECTION_API)

    payload = {'origin':start, 'destination':end}
    result = requests.get(DIRECTIONS_BASEURL, params=payload)
    result = result.json()
    responce = ''

    try:
        if result['status'] == "OK":
            for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
                j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
                responce +=strip_tags(j)+'\n'

            return responce
        else:
            ''' Will be replaced with logging in future'''
            print(result['status'])
            print(result['error_message'])
            return ERROR_MSG
    except KeyError as e:
        ''' Need to be logged'''
        return ERROR_MSG


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r'~directions \".+?\" \".+?\"', text)
    if not match:
        return

    r = [f[1:-1] for f in re.findall('".+?"', match[0])]

    return directions(r[0].encode("utf8"), r[1].encode("utf8"))

on_bot_message = on_message
