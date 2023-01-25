import scrapy


class BukuSpider(scrapy.Spider):
    name = 'buku'
    allowed_domains = ['bukukita.com']
    start_urls = ['http://bukukita.com/']

    def parse(self, response):
        pass
