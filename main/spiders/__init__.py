from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "main"

    def start_requests(self):
        urls = [
            "https://1xbet.com/cn",
            "https://1xbet.com/en",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"main/scrapes/main-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")