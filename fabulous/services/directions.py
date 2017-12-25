"""~directions "<start>" "<end>" (in quotes) return a result from the google maps result for directions from <start> to <end>"""

try:
    from urllib import quote, urlencode
except ImportError:
    from urllib.request import quote, urlencode
import re
import requests
import json, urllib
import googlemaps
from googlemaps import Client as GoogleMaps
from secret_example import GOOGLE_DIRECTION_API
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser


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

    url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', end)
    ))
    ur = urllib.urlopen(url)
    result = json.load(ur)

    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
        print strip_tags(j)

    return


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r'~directions \".+?\" \".+?\"', text)
    if not match:
        return

    r = [f[1:-1] for f in re.findall('".+?"', match[0])]

    return directions(r[0].encode("utf8"), r[1].encode("utf8"))

on_bot_message = on_message
