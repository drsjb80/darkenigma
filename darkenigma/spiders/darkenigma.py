# -*- coding: utf-8 -*-
import scrapy
import re

with open('phrases') as p:
    phrases = [line.strip('\n') for line in p]

with open('locations') as l:
    locations = [line.strip('\n') for line in l]

count = 0

class DarkenignmaSpider(scrapy.Spider):
    name = 'darkenignma'
    # custom_settings = { 'DEPTH_LIMIT': 0 }

    with open('URLs') as u:
        start_urls = [line.strip('\n') for line in u]

    def parse(self, response):
        # print("Looking at " + response.url)
        global count
        count += 1
        if (count % 10000) == 0:
            print(count, flush=True)

        for location in locations:
            l = r'\b' + location + r'\b'
            if re.search(l, response.text, re.IGNORECASE):
                # print(location + ' found in body of ' + response.url, flush=True)
                for phrase in phrases:
                    p = r'\b' + phrase + r'\b'
                    if re.search(p, response.text, re.IGNORECASE):
                        print(phrase + ' and ' + location + ' found in ' + response.url, flush=True)

                for href in response.css('a::attr(href)'):
                    href = re.sub(r'#.*', '', response.urljoin(href.get()))
                    if re.search('http:\/\/.*\.onion.*', href, re.IGNORECASE):
                        # print('Following ' + href)
                        yield response.follow(href, self.parse)

