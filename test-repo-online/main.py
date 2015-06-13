#http://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers&cmtitle=Category:Discourse_analysis&cmlimit=100
#http://en.wikipedia.org/w/api.php?action=parse&page=Text linguistics
#http://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&titles=Text%20linguistics&redirects=true
#http://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&generator=random&redirects=true
#http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&format=json

import urllib.request
import json
import pprint
import sys
import codecs

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def download_json(url):
    f = urllib.request.urlopen(url)
    content = f.read()
    body = content.decode('utf-8')
    result = json.loads(body)
    return result

def json_to_text(pagejson):
    pagejsonkeys = list(pagejson['query']['pages'])
    pagecontent = pagejson['query']['pages'][pagejsonkeys[0]]['extract']
    pagecontent = strip_tags(pagecontent)
    return pagecontent


  #https://secure.wikimedia.org/wikipedia/en/w/index.php?title=Special:Random&printable=yes

def download_random_crap(size):
    accumulated = 0
    file = open('wiki_random_dump.txt', 'a', encoding='utf-8')
    while accumulated < size:
        url = 'http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&format=json'
        pagejson = download_json(url)
        pagecontent = json_to_text(pagejson)
        accumulated += len(pagecontent)
        file.write(pagecontent)
        print(".",flush=True,end='')
    file.close()

def download_category_pages(category_title):
    category_title = category_title.replace(' ','_')
    url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers&cmtitle=Category:'+category_title+'&cmlimit=100'
    
    categoryjson = download_json(url)
    file = open(category_title+ '.txt', 'a', encoding='utf-8')
    for page in categoryjson['query']['categorymembers']:
        title = page['title'].replace(' ','_')

        print(title, flush=True)
        if title[0:9] == "Category:":
            continue
        
        url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&redirects=true&titles='+title
        #print(url)
        
        #print(pagecontent)
        pagejson = download_json(url)
        pagecontent = json_to_text(pagejson)
        
        file.write(pagecontent)
        #break

    file.close()

pp = pprint.PrettyPrinter(indent=4)    
#download_category_pages('Discourse analysis')
download_random_crap(50000)