"""~yt <search term> will return the top search result """

import re
import requests
from random import shuffle

YT_BASEURL = "https://www.youtube.com/results?"
def yt(searchterm):
    payload = {'search_query': searchterm}
    r = requests.get(YT_BASEURL, params=payload)
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
