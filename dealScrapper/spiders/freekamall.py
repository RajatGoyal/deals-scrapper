from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from dealScrapper.items import ContentItem


class SaveMoneyIndia(CrawlSpider):
    name = "freekamall"
    allowed_domains = ["freekamall.com"]

    start_urls = ["http://freekaamaal.com/"]

    rules = (Rule(SgmlLinkExtractor(allow=(r'freekaamaal.*\/page\/\d+\/', )), callback='parse_start_url', follow=True),
    )

    def parse_start_url(self, response):
        items = []
        for selection in response.xpath("//div[@class='contentpagination']"):
            item = ContentItem()
            item['title'] = selection.xpath("div[@class='exp_detail']/a/h2/text()").extract()
            item['link'] = selection.xpath("a[@class='shpnw']/@href").extract()
            item['desc'] = selection.xpath("div[@class='exp_detail']/span/text()").extract()
            item["category"] = ""
            items.append(item)

        return items