"""~sof <your question> > will return the the result """
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re
import requests
import json


ERROR_MSG = "sorry, no answer found"
KEY_ERROR_MSG = "Sorry, some unknown error occured" 
def sof(searchterm):
    json_data = []
    searchurl="https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q={0}&accepted=True&site=stackoverflow".format(searchterm)
    result=requests.get(searchurl)
    json_data=result.json()
    try:
            for dct in json_data["items"]:
                links=dct["link"]
                if not links:
                    return ERROR_MSG
                return links
    except KeyError:
        return KEY_ERROR_MSG


    
def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~sof (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return sof(searchterm)

on_bot_message = on_message