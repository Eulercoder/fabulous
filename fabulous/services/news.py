"""~news <location> <category> <language>will fetch news from news API
1. news
2. news <au, de, gb, in, it, us>
3. news <au, de, gb, in, it, us> <business, entertainment, gaming, general, music, politics, science-and-nature, sport, technology>
4. news <au, de, gb, in, it, us> <business, entertainment, gaming, general, music, politics, science-and-nature, sport, technology> <en,  de,  fr>"""
import requests
import json
from secret_example import NEWS_API


SOURCE_ERR = "Failed to fetch sources"
NEWS_ERR = "Failed to fetch news"
INTERNAL_ERR = "Some unknown error occured"
sourceBaseURL = "https://newsapi.org/v1/sources"
articleBaseURL = "https://newsapi.org/v1/articles"


def fetchNews(newsParams):
    language = 'en'
    category = 'general'
    country = 'in'

    availCountries = ['au', 'de', 'gb', 'in', 'it', 'us']
    availCategories = ['business', 'entertainment', 'gaming', 'general', 'music', 'politics', 'science-and-nature', 'sport', 'technology']
    availLanguages = ['en', 'de', 'fr']

    if len(newsParams)>1 and newsParams[1] in availCountries:
	    country = newsParams[1]
    if len(newsParams)>2 and newsParams[2] in availCategories:
	    category = newsParams[2]
    if len(newsParams)>3 and newsParams[3] in availLanguages:
	    language = newsParams[3]
    
    sourceQuery = {
	'language':language,
	'country':country,
	'category':category
    }

    sourceJsonData = requests.get(sourceBaseURL, params=sourceQuery).json()
    sourceList = []
    try:
        if sourceJsonData['status'] == 'ok':
            for sourceInfo in sourceJsonData['sources']:
                sourceList.append([sourceInfo['id'], sourceInfo['name']])
        else:
            print(sourceBaseURL)
            return SOURCE_ERR
    except KeyError:
        print("Invalid data(key missing)")
        return INTERNAL_ERR

    newsData = "\n"
    
    newsQuery = {
	'source':'',
	'apiKey':NEWS_API
    }
    
    try:
        for source in sourceList:
            newsQuery['source'] = source[0]
            articleJsonData = requests.get(articleBaseURL, newsQuery).json()
            if articleJsonData['status'] == 'ok':
                for article in articleJsonData['articles']:
                    title, publishedAt, description, url, author, sourceName = [(i if i else "Not available") for i in [article['title'], article['publishedAt'], article['description'], article['url'], article['author'], source[1]]]
                    newsData += title + '\n\n' + publishedAt + '\n' + description + '\nRead further at: ' + url + '\nAuthor: ' + author + '\nSource: ' + sourceName + '\n\n\n\n'
            else :
                print(articleBaseURL)
                return NEWS_ERR
    except KeyError:
        print("Key error")
        return INTERNAL_ERR
    return newsData



def on_message(msg, server):
    text = msg.get("text", "").split()
    if text[0] == "~news":
        return fetchNews(text)
    return

on_bot_message = on_message
