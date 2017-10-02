"""~scores <sport> return the live scores for <sport>"""
from bs4 import BeautifulSoup as bs
import requests
import re

def cricket():
    url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    r = requests.get(url)
    data = r.text
    soup = bs(data, "html.parser")
    if len(soup.find_all('match')) == 0:
        return "No matches is in progress right now!"
    result = ""
    for mat in soup.find_all('match'):
        state = mat.find('state')
        mscr = mat.find('mscr')
        if state['mchstate'] == "inprogress" or state['mchstate'] == "complete" or state['mchstate'] == "stump":
            result += "\n" + mat['mchdesc'] + " (" + state['addnstatus'] + ")"
            result += "\n" + state['status']
            bttm = mscr.find('bttm')
            blgtm = mscr.find('blgtm')
            result += "\n" + bttm['sname'] + ": "
            for innings in bttm.find_all('inngs'):
                result += "\n" + innings['desc'] + ": " + innings['r'] + "/" + innings['wkts']
            result += "\n" + blgtm['sname'] + ": "
            if len(blgtm.find_all('inngs')) == 0:
                result += "\n" + "Yet to bat.\n"
            for innings in blgtm.find_all('inngs'):
                result += "\n" + innings['desc'] + ": " + innings['r'] + "/" + innings['wkts'] + "\n"
    return result

def football():
    return "\nWe're currently working on this!\n"

def scores(sport):
    if sport == "cricket":
        return cricket()
    elif sport == "football":
        return football()
    else:
        return "Sorry we currently do not support "+sport+"!\n"

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~scores (.*)", text)
    if not match:
        return
    return scores(match[0].encode("utf8"))

on_bot_message = on_message
