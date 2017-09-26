"""~translate <text> will return the goslate transalte result for <text> in English"""

import goslate, re

def translate(text):
    gs = goslate.Goslate()
    id = text.split()
    return gs.translate(text[3:], id[0])

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~translate (.*)", text)
    if not match:
        return

    return translate(match[0].encode("utf8"))

on_bot_message = on_message