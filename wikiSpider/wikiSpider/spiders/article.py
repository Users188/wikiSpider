import scrapy


class AritcleSpider(scrapy.Spider):
    name = "article"

    # Scrapy 定义的程序入口，生成抓取网站的Request对象
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse)
                for url in urls]

    def parse(self, response, **kwargs):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is : {}', format(url))
        print('Title is : {} '.format(title))
