# scarpy.contrib 模块在1.6版本移除。
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule


# 拓展CrawlSpider类
class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    # 将文件类型与非文件类型分开
    rules = [Rule(LinkExtractor(allow=r'^(/wiki/)((?!:).)*$'),
                  callback='parse_items', follow=True,
                  cb_kwargs={'is_article': True}),
             Rule(LinkExtractor(allow='.*'),
                  callback='parse_item',
                  cb_kwargs={'is_article': False})
             ]

    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('h1::text').extract_first()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ', '')
            # print('URL is: {}'.format(url))
            print('title is: {} '.format(title))
            print('text is: {}'.format(text))
            print('Last updated: {}'.format(lastUpdated))
        else:
            print('This is not an article:{}'.format(title))
