"""~gif <search term> return a random result from the  google gif search result for <search term>"""

import re
import requests
from random import shuffle

GIF_BASEURL = "https://www.google.com/search"

def unescape(url):
    # for unclear reasons, google replaces url escapes with \x escapes
    return url.replace(r"\x", "%")


def gif(searchterm):
    payload = {'tbs':'itp:animated', 'tbm':'isch', 'q':searchterm}

    # this is an old iphone user agent. Seems to make google return good results.
    useragent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Versio  n/4.0.5 Mobile/8A293 Safari/6531.22.7"

    result = requests.get(GIF_BASEURL, params=payload, headers={"User-agent": useragent}).text

    gifs = list(map(unescape, re.findall(r"var u='(.*?)'", result)))
    shuffle(gifs)

    if gifs:
        return gifs[0]
    else:
        return ""


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~gif (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return gif(searchterm.encode("utf8"))

on_bot_message = on_message
