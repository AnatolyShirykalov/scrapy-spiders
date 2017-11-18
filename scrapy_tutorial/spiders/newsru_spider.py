import scrapy


class NewsruSpider(scrapy.Spider):
    name = 'newsru'

    start_urls = ['http://www.newsru.com/allnews/']

    def parse(self, response):
        for a in response.css('a.index-news-text'):
            yield response.follow(a, callback=self.parse_news)
        for a in response.css('a.arch-arrows-link-l'):
            yield response.follow(a, callback=self.parse)

    def parse_news(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
                'title': extract_with_css('h1.article-title'),
                'publish_time': extract_with_css('meta[property="article:published_time"]::attr(content)'),
                'ps': response.css('.article-text > p').extract(),
                'imgs': response.css('.article-list-img > .overlay > .big-img::attr(style)').re('^(?:background-image: url\()([^)]+)(?:\))'),
                }

