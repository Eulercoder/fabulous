"""~google <search term> return a first result from the  google search result for <search term>"""
from bs4 import BeautifulSoup
try:
    from urllib import quote,unquote
except ImportError:
    from urllib.request import quote,unquote
import re
import requests
from random import shuffle


def unescape(url):
    # for unclear reasons, google replaces url escapes with \x escapes
    return url.replace(r"\x", "%")


def google(searchterm, unsafe=False):

    searchterm = quote(searchterm)
    url = "https://www.google.com/search?q={0}".format(searchterm)
    result = requests.get(url).text
    soup = BeautifulSoup(result, "html5lib")

    answer = soup.findAll("h3", attrs={"class": "r"})
    if not answer:
        return "Try Again!"

    try:
        searches = list(map(unescape,re.findall(r"q=(.*?)&", str(answer[0]))))
        if searches:
            return searches[0]
            
        return "Try Again!"

    except IndexError:
        return ' '.join(answer[0].stripped_strings)


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~google (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return google(searchterm.encode("utf8"))


on_bot_message = on_message
