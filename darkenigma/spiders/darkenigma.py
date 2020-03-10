# -*- coding: utf-8 -*-
import scrapy
import re
from datetime import datetime

count = 0

class DarkenignmaSpider(scrapy.Spider):
    name = 'darkenignma'
    allowed_domains = ['onion']

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

        for href in response.css('a::attr(href)'):
            # remove anchors
            href = re.sub(r'#.*', '', response.urljoin(href.get()))
            print('Following ' + href)
            yield response.follow(href, self.parse)

