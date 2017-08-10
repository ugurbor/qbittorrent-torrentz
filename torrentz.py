#VERSION: 1.00
#AUTHOR: Teemu Pajarinen (manakeri@enomeno.com)
#Public Domain

import re

try:
    from novaprinter import prettyPrinter
    from helpers import retrieve_url, download_file
except:
    pass

class torrentz2(object):
    url = 'http://torrentz2.eu'
    name = 'torrentz2'
    supported_categories = {
            'all': 0}
    
    def __init__(self):

    def download_torrent(self, info):
        print(download_file(info))

    def search(self, what, cat='all'):
        i = 0
        while i<11:
            res = 0
            page = retrieve_url(self.url+'/search?f=%s&p=%d/'%(what, i))
            p = re.compile('<a href="/(?P<link>[0-9a-f]{40})">(?P<name>.*?)</a>.*?'+
                              '<span title="(\d+)">.*?(?P<size>\d+ MB)</span>.*?'+
                              '<span>(?P<seeds>(\d+,)?\d+)</span>.*?'+
                              '<span>(?P<leech>(\d+,)?\d+)</span>')

            for match in p.finditer(page):
                    m = p.search( match.group(0))
                    if m:
                            t = m.groupdict()
                            t['name'] = re.sub('<.*?>', '', t['name'])
                            t['desc_link'] = self.url + "/" + t['link']
                            t['link'] = 'magnet:?xt=urn:btih:'+t['link']
                            t['engine_url'] = self.url
                            t['seeds'] = t['seeds'].replace(',', '')
                            t['leech'] = t['leech'].replace(',', '')
                            prettyPrinter(t)
                            res = res + 1
            if res == 0:
                    break
            i += 1
