"""~sof <your question> > will return the the result """
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re
import requests
import json


def sof(searchterm):
    json_data = []
    searchurl="https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q={0}&accepted=True&site=stackoverflow".format(searchterm)
    result=requests.get(searchurl)
    json_data=result.json()
    for dct in json_data["items"]:
        links=dct["link"]
        if not links:
            return "sorry, no answer found"
        return links

    
def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~sof (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return sof(searchterm)

on_bot_message = on_message