# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from elasticsearch import Elasticsearch

count = 0

class DarkenignmaSpider(scrapy.Spider):
    name = 'darkenignma'
    # custom_settings = { 'DEPTH_LIMIT': 0 }

    es = Elasticsearch()

    with open('URLs') as u:
        start_urls = [line.strip('\n') for line in u]

    def parse(self, response):
        print("Looking at " + response.url)
        global count
        count += 1
        if (count % 10000) == 0:
            print(count, flush=True)

        for location in locations:
            tosave = { 'url': response.url,
                'text': response.text,
                'timestamp': datetime.now(),
            }

            res = es.index(index="darkenigma", body=tosave)
            print(res['result'])

            for href in response.css('a::attr(href)'):
                href = re.sub(r'#.*', '', response.urljoin(href.get()))
                if re.search('https?:\/\/.*\.onion.*', href, re.IGNORECASE):
                    print('Following ' + href)
                    yield response.follow(href, self.parse)

