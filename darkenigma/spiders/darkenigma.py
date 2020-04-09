# -*- coding: utf-8 -*-
import scrapy
import re
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

count = 0
visited = set()

regex = re.compile(r'^https?://.*\.onion.*$', re.IGNORECASE)
rm_anchors = re.compile(r'#.*')
rm_queries = re.compile(r'\?.*$')

class DarkenignmaSpider(scrapy.Spider):
    name = 'darkenignma'

    with open('URLs') as u:
        start_urls = [line.strip('\n') for line in u]

    def parse(self, response):
        print("Looking at " + response.url)

        global count
        count += 1
        if (count % 10000) == 0:
            print(count, flush=True)

        yield { \
            'url': response.url, \
            'text': response.text, \
            'timestamp': datetime.now(), \
        }

        global visited

        for href in response.css('a::attr(href)'):
            # remove anchors
            href = re.sub(rm_anchors, '', response.urljoin(href.get()))
            # remove queries
            href = re.sub(rm_queries, '', href)

            # assuming scrapy will track visited
            if not regex.match(href):
                print('Not following ' + href)
                return
            if href in visited:
                print('Already visited ' + href)
                return

            print('Following ' + href)
            visited.add(href)
            yield response.follow(href, self.parse)
