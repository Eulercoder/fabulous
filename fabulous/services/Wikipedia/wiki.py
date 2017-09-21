import wikipedia
import re





def wikiSearch(searchItem):
    try:
        searchList  =  wikipedia.search(searchItem)
        for  item in searchList: 
            try:
                content_page = wikipedia.page(item)
                content_Url  =  content_page.url
                content_title  =  content_page.title
                #print("Okk u have searched for:",content_title)
                #print("The url of the page:",content_Url)
                return content_Url
            except wikipedia.exceptions.DisambiguationError as e:
                print("can't find your searchItem in wiki ......use specific term dude....it is not a Ai still ...now :-p")
    except Exception as e:
        return ("can't find your item man")




def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~wiki (.*)", text)
    if not match:
        return

    searchterm = str(match[0])
    return wikiSearch(searchterm)

on_bot_message = on_message

