# -*- coding: utf-8 -*-
import scrapy
import re

with open('phrases') as p:
    phrases = [line.strip('\n') for line in p]

class ExamplecomSpider(scrapy.Spider):
    name = 'examplecom'

    with open('URLs') as u:
        start_urls = [line.strip('\n') for line in u]

    def parse(self, response):
        for phrase in phrases:
            for header in response.headers:
                if re.search(phrase, str(response.headers[header]), re.IGNORECASE):
                    print(phrase + ' found in headers of ' + response.url)
                    break

            if re.search(phrase, response.text, re.IGNORECASE):
                print(phrase + ' found in body of ' + response.url)
