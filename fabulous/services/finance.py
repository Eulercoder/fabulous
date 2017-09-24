"""~stock <search_term> will return the real time result of that stock."""
import urllib, json
import requests

try:
    from urllib import quote
except ImportError:
    from urllib.request import quote
import re

def stock(name):
    query = quote(name)
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey=96LBSRJWWKHLLIWI".format(query)
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    try:
        index = data["Meta Data"]["3. Last Refreshed"]
        answer = data["Time Series (1min)"][index]
        result = data["Meta Data"]["2. Symbol"] + "\n" + "Last Refreshed : " + index + "\n" + "Time Zone : " + data["Meta Data"]["6. Time Zone"] + "\n" + "1. open : " + answer["1. open"] + "\n" + "2. close : " + answer["4. close"] + "\n" + "3. high : " + answer["2. high"] + "\n" + "4. low : " + answer["3. low"] + "\n" + "5. volume : " + answer["5. volume"]
    except:
        return ":crying_cat_face: Sorry, something went wrong :crying_cat_face:"

    return result

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~stock (.*)", text)
    if not match:
        return

    return stock(match[0].encode("utf8"))

on_bot_message = on_message