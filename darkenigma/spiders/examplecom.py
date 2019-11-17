import re
import scrapy

with open('phrases') as p:
    phrases = [line.rstrip('\n') for line in p]

class BlogSpider(scrapy.Spider):
    name = 'darkenigma'

    with open('URLs') as u:
        start_urls = [line.rstrip('\n') for line in u]

    def parse(self, response):
        for phrase in phrases:
            for header in response.headers:
                if re.search(phrase, str(response.headers[header])):
                    print(phrase + ' found in headers of ' + response.url)
                    break

            if re.search(phrase, response.text):
                print(phrase + ' found in body of ' + response.url)
