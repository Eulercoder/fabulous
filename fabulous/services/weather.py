import requests
import re
import json
from bs4 import BeautifulSoup
from secret_example import WEATHER_API


def weather(searchcity):
    payload = {"q":searchcity, "appid":"ee3f34d4ef85aac3ec402dbe6af8bf0f", "units":"metric"}

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        r = requests.get(base_url, params=payload)
        data = json.loads(r.text)
        if data["cod"] == 200:
            return "The temperature in " + searchcity.upper() + "," + data["sys"]["country"] + " is " + \
                    str(data["main"]["temp"]) + u'\N{DEGREE SIGN}' + "C with " + data["weather"][0]["description"] + \
                    "\nThe minimum and maximum expected temperatures are " + str(data["main"]["temp_min"]) + \
                    u'\N{DEGREE SIGN}' + "C and " + str(data["main"]["temp_max"]) + u'\N{DEGREE SIGN}' + "C"
        elif data["cod"] == "404":
            return "Please enter a valid city"
        else:
            return "Something went wrong"
    except:
        return "Something went wrong"


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~weather (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return weather(searchterm.encode("utf8"))


on_bot_message = on_message
