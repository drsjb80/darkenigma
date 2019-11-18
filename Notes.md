Install privoxy:

    brew install privoxy

Configure privoxy; uncomment the one line:

    forward-socks5t   /               127.0.0.1:9050 .

Run it:

    privoxy --no-daemon /usr/local/etc/privoxy/config

Install tor and run it:

    brew install tor
    tor

Run the simple example.com spider:

    scrapy crawl examplecom
