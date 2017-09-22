"""~yt <search term> > will return the top search result """

try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re
import requests
from random import shuffle





def yt(searchterm,unsafe=False):
    searchterm = quote(searchterm)
    safe = "&safe=" if unsafe else "&safe=active"
    url = "https://www.youtube.com/results?search_query={0}".format(searchterm,safe)
    url = url.format(quote(searchterm))

    r = requests.get(url)
    results = re.findall('a href="(/watch[^&]*?)"', r.text)

    if not results:
        return "sorry, no videos found"
    return "https://www.youtube.com{0}".format(results[0])
   


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~yt (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return yt(searchterm.encode("utf8"))

on_bot_message = on_message
