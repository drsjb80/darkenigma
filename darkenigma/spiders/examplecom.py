# -*- coding: utf-8 -*-
import scrapy
import re

with open('phrases') as p:
    phrases = [line.strip('\n') for line in p]

class ExamplecomSpider(scrapy.Spider):
    name = 'examplecom'
    custom_settings = { 'DEPTH_LIMIT': 0 }

    with open('URLs') as u:
        start_urls = [line.strip('\n') for line in u]

    def parse(self, response):
        # print("Looking at " + response.url)

        for phrase in phrases:
            p = r'\b' + phrase + r'\b'
            for header in response.headers:
                if re.search(p, str(response.headers[header]), re.IGNORECASE):
                    print(phrase + ' found in headers of ' + response.url, flush=True)
                    break

            if re.search(p, response.text, re.IGNORECASE):
                print(phrase + ' found in body of ' + response.url, flush=True)

        for href in response.css('a::attr(href)'):
            href = re.sub(r'#.*', '', response.urljoin(href.get()))
            if re.search('http:\/\/.*\.onion.*', href, re.IGNORECASE):
                # print('Following ' + href)
                yield response.follow(href, self.parse)

