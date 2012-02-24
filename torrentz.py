#VERSION: 1.00
#AUTHOR: Teemu Pajarinen (manakeri@enomeno.com)
#Public Domain

from novaprinter import prettyPrinter
from helpers import retrieve_url, download_file
import re

class torrentz(object):
	url = 'http://torrentz.eu'
	name = 'torrentz'
	supported_categories = {'all': 'all'}

	def download_torrent(self, info):
		print download_file(info)

	def search(self, what, cat='all'):
		i = 0
		while i<11:
			res = 0
			page = retrieve_url(self.url+'/search?f=%s&p=%d/'%(what, i))
                        p = re.compile('<a href="/(?P<link>[0-9a-f]{40})"><b>(?P<name>.*?)</a>.*?'+
                                          '<span class="s">(?P<size>\d+ MB)</span>.*?'+
                                          '<span class="u">(?P<seeds>\d+)</span>.*?'+
                                          '<span class="d">(?P<leech>\d+)</span>')

                        for match in p.finditer(page):
                                m = p.search( match.group(0))
                                if m:
                                        t = m.groupdict()
                                        t['name'] = re.sub('<.*?>', '', t['name'])
                                        t['desc_link'] = self.url + "/" + t['link']
                                        t['link'] = 'magnet:?xt=urn:btih:'+t['link']
                                        t['engine_url'] = self.url
                                        prettyPrinter(t)
                                        res = res + 1
                        if res == 0:
                                break
			i += 1
