import scrapy

class GraphicsSpider(scrapy.Spider):
    name="graphics"

    start_urls = ['http://mathematichka.ru/school/functions/Function_Graph_Table.html']

    def parse(self, response):
        def text(tds, i):
            return tds[i].css('::text').extract_first()
        for tr in response.css('p ~ table > tr'):
            if len(tr.css('td.formula')) == 0:
                continue
            tds = tr.css('td')
            yield {
                    'funcname': text(tds, 0),
                    'formula': "".join(tds[1].css('td > *, td::text').extract()),
                    'src': '/img/math/' + tds[2].css('img::attr(src)').extract_first(),
                    'graphname': text(tds, 3),
                    }

