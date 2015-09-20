from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from dailyClog.items import blogItem

class MySpider(CrawlSpider):
    name = "clog"
    allowed_domains = ["dailycal.org"]
    start_urls = ["http://www.dailycal.org/section/blogs/clog/"]
    rules = [Rule(LinkExtractor(allow=('/section/blogs/clog'), restrict_xpaths=("//nav[@id='nav-below']"))),
             Rule(LinkExtractor(restrict_xpaths=("//div[@id='blog-posts-main']")), callback='articleData', follow='False')
            ]

    def articleData(self, response):
        post = blogItem()
        url = response.url
        title = response.xpath("//h2[@class='entry-title']/text()").extract()
        content = response.xpath("//div[@class='entry-content']").extract()
        post["title"] = title
        post["link"] = url
        post["content"] = content
        print "ANSWER: "+str([sentence + '.' for sentence in str(content).split('.') if 'You' in sentence])
        return post