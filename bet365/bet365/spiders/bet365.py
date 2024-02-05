import scrapy

class Bet365(scrapy.Spider):
    name = "bet365"
    start_urls = ["https://www.bet365.com/#/HO/"]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield { 'title': title }
        # pass