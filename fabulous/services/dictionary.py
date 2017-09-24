"""~dict <search_term> will return the meaning and usage of <search_term>"""
import urllib, json
import requests
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re

def dict(word):
    query =  quote(word)
    url = "http://api.urbandictionary.com/v0/define?term={0}".format(query)

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    try:
        example = data["list"][0]["example"]
        definition = data["list"][0]["definition"]
    except:
        return "Sorry, this word doesn't exist!!"

    answer = "definition : " + definition + "\n" + "example : " + example

    return answer


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~dict (.*)", text)
    if not match:
        return

    return dict(match[0].encode("utf8"))

on_bot_message = on_message
