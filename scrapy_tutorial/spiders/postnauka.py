import scrapy
import itertools

class Postnauka(scrapy.Spider):
    name="postnauka"

    start_urls = list(itertools.chain.from_iterable([
        ['https://postnauka.ru/api/v1/posts?page={0}&term={1}'.format(i,term) for i in range(500)]
        for term in ["video", "faq", "longreads"]
        ]))

    def parse(self, response):
        tmpl = 'https://postnauka.ru/api/v1/posts/{0}?expand=content'

        for id in response.css('item > id::text').extract():
            yield response.follow(tmpl.format(id), callback=self.parse_content)

    def parse_content(self, response):
        yield {
                'id': response.css('id::text').extract_first(),
                'content': response.css('content::text').extract_first()
                }
