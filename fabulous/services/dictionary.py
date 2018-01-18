"""~dict <search_term> will return the meaning and usage of <search_term>"""
import requests
import re

DICTIONARY_BASEURL = "http://api.urbandictionary.com/v0/define?" 
ERROR_MSG = "Sorry, this word doesn't exist!!"
def dict(word):
    payload = {'term':word}

    response = requests.get(DICTIONARY_BASEURL, params=payload)
    data = response.json()

    try:
        example = data["list"][0]["example"]
        definition = data["list"][0]["definition"]
    except:
        return ERROR_MSG

    answer = "definition : " + definition + "\n" + "example : " + example

    return answer


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~dict (.*)", text)
    if not match:
        return

    return dict(match[0].encode("utf8"))

on_bot_message = on_message
