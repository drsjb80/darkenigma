Don't use privoxy as it only intercepts http, not https.

Install tor and run it:

    brew install tor
    tor

On debian/ubuntu, see https://2019.www.torproject.org/docs/debian.html.en

Install torsocks
    brew install torsocks

Run the simple example.com spider:

    torsocks scrapy crawl examplecom

https://docs.scrapy.org/en/latest/topics/broad-crawls.html
https://docs.scrapy.org/en/latest/topics/link-extractors.html

https://www.mikulskibartosz.name/how-to-use-scrapy-to-follow-links-on-the-scraped-pages/

        custom_settings = { 'DEPTH_LIMIT': 2 }

        # ...

        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
