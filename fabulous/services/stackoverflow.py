"""~sof <your question> > will return the the result """
import re
import requests


ERROR_MSG = "sorry, no answer found"
KEY_ERROR_MSG = "Sorry, some unknown error occured" 
SOF_BASEURL = "https://api.stackexchange.com/2.2/search/advanced?"

def sof(searchterm):
    json_data = []
    payload = {'order':'desc', 'sort':'relevance', 'q': searchterm, 'accepted':'True', 
    'site':'stackoverflow'}
    # searchurl="https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q={0}&accepted=True&site=stackoverflow".format(searchterm)
    result=requests.get(SOF_BASEURL, params=payload)
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