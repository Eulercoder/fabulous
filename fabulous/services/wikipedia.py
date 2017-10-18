"""~wiki <search term> will return three results from the wikipedia search for <search term>"""

import re
import requests

def wiki_search(query, results=3, suggestion=True):
    params = {
        'format': 'json',
        'action': 'query',
        'list': 'search',
        'srprop': 'snippet',
        'srlimit': results,
        'srsearch': query,
        'generator': 'search',
        'gsrlimit': results,
        'gsrsearch': query,
        'prop': 'info',
        'inprop': 'url',
    }
    if suggestion:
        params['srinfo'] = 'suggestion'

    r = requests.get('http://en.wikipedia.org/w/api.php', params=params)

    raw_results = r.json()

    if 'error' in raw_results:
        if raw_results['error']['info'] in ('HTTP request timed out.', 'Pool queue is full'):
            return u"Searching for \"{0}\" resulted in a timeout. Try again in a few seconds.".format(self.query)
        else:
            return "An unknown error occured: \"{0}\".".format(raw_results['error']['info'])

    try:
        # Python 2.6-2.7 
        from HTMLParser import HTMLParser
    except ImportError:
        # Python 3
        from html.parser import HTMLParser
    h = HTMLParser()

    search_results = list(
            (d['title'],
            h.unescape(re.sub('^Play media\s*', '', re.sub('<[^<]+?>', '', d['snippet']))),
            raw_results['query']['pages'][str(d['pageid'])]['fullurl'])
        for d in raw_results['query']['search'])

    if suggestion and not search_results:
        if raw_results['query'].get('searchinfo'):
            return [u'Did you mean: {}?'.format(raw_results['query']['searchinfo']['suggestion'])]
        return [u'Found nothing :(']

    return list(u'{} {}\n{}...'.format(x, z, y) for (x, y, z) in search_results)

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"~wiki (.*)", text)
    if not match:
        return

    searchterm = match[0]
    return "\n\n".join(wiki_search(searchterm))


on_bot_message = on_message