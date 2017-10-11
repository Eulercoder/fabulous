"""~google <search term> will return three results from the google search for <search term>"""

import re
import requests
from random import shuffle
from googleapiclient.discovery import build
import logging

my_api_key = "Your API Key(Link: https://console.developers.google.com/apis/dashboard)"
my_cse_id = "Your Custom Search Engine ID(Link: https://cse.google.co.in/cse/)"

"""fuction to fetch data from Google Custom Search Engine API"""
def google(searchterm, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key, cache_discovery=False)
    res = service.cse().list(q=searchterm, cx=cse_id, **kwargs).execute()
    return res['items']

"""fuction to return first three search results"""
def google_search(searchterm):
    results = google(searchterm, my_api_key, my_cse_id, num=10)
    length = len(results)
    retval = ""
    if length < 3:
        for index in range(length):
            retval += results[index]['link'] + "\n"
    else:
        for index in range(3):
            retval += results[index]['link'] + "\n"
    return retval


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~google (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return google_search(searchterm)


on_bot_message = on_message
