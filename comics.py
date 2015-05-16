# -*- coding: cp1252 -*-
import urllib2, cookielib
from html.parser import HTMLParser

class MyParse(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="img":
            imageURL = (dict(attrs)["src"])
            if "http://s3.roosterteeth.com/assets/media/9_4" in imageURL:
                imageURL = imageURL.replace("t.jpg", ".jpg")
                print imageURL

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site= "http://roosterteeth.com/comics/?page=2"

req = urllib2.Request(site, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

h = MyParse()
content = page.read()
h.feed(content)
