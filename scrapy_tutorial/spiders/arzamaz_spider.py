import scrapy


class ArzamasSpider(scrapy.Spider):
    name = 'arzamas'

    start_urls = ['http://arzamas.academy/materials/{0}'.format(i) for i in range(1400)]

    def parse(self, response):
        if (response.status != 200):
            return;
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
          'title': extract_with_css('h1::text'),
          'subtitle': extract_with_css('h1 ~ p::text'),
          'ps': response.css('h1 ~ p::text').extract()[1:],
        }

