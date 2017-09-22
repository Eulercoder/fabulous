try:
    from urllib import quote
    from urllib import urlopen
except ImportError:
    from urllib.request import quote
import re
import requests
import json

access_token = ''

def shorten(longUrl):
    if len(access_token)==0:
        return 'Access Token Missing: Please add your bit.ly access token to shorten.py file'
    mainUrl = 'https://api-ssl.bitly.com/v3/shorten?access_token={0}&longUrl={1}'
    longUrl=quote(longUrl, safe='')
    mainUrl = mainUrl.format(access_token,longUrl);
    data = urlopen(mainUrl).read();
    data = json.loads(data)
    return data[u'data'][u'url']

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~shorten (.*)", text)
    if not match:
        return
    searchterm = match[0]
    return shorten(searchterm.encode("utf8"));

on_bot_message = on_message
