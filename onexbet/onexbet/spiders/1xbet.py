import scrapy

class Bet365(scrapy.Spider):
    name = "1xbet"
    start_urls = [
        "https://1xbet.com/cn",
        "https://1xbet.com/tw",
        "https://1xbet.com/my",
        "https://1xbet.com/en",
        "https://1xbet.com/ko",
        "https://1xbet.com/ja",
        "https://1xbet.com/id",
    ]

    def parse(self, response):
        title = response.css('#page_title span::text')[0].extract()
        sport_types = response.css('.sports-slider__wrapper a').extract()
        print('LOGG :: ', sport_types)
        yield {'group': title, 'sport_types': sport_types}
        # elements = response.xpath("//div[contains(@class, 'sports-slider__wrapper')]//div[contains(@class, 'b-filters__slide')]//a[contains(@class, 'b-filters__sport')").extract()
        # print('parents :: ', elements)
        # # for element in elements:
        #     url = element.xpath("//a[contains(@class, 'b-filters__sport')").xpath('@href').extract()
        #     print('LOGG :: ', url)