from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from tutorial.utils import key_lookup
from tutorial.items import ContentItem


class SaveMoneyIndia(CrawlSpider):
    name = "savemoney"
    allowed_domains = ["savemoneyindia.com"]
    categories = {
        "http://www.savemoneyindia.com/category/computers-laptops/" : "Computer & Laptops",
        "http://www.savemoneyindia.com/category/mobiles/": "Mobiles",
        "http://www.savemoneyindia.com/category/mobile-dth-data-card-recharge/": "Recharge",
        "http://www.savemoneyindia.com/category/clothing-shoes-bags-lifestyle/": "Clothing",
        "http://www.savemoneyindia.com/category/footwear/": "Footwear",
        "http://www.savemoneyindia.com/category/electronics-gadgets/": "Electronics",
    }
    start_urls = categories.keys()

    rules = (Rule(SgmlLinkExtractor(allow=(r'www.savemoneyindia.com\/category.*\/page\/\d+\/', )), callback='parse_start_url', follow=True),
    )

    def parse_start_url(self, response):
        items = []
        for selection in response.xpath("//div[contains(@id, 'post-')]"):
            item = ContentItem()
            item['title'] = selection.xpath("h2[@class='entry-title']/a/text()").extract()
            item['link'] = selection.xpath("div[@class='entry']//a/@href").extract()
            item['desc'] = selection.xpath("div[@class='entry']/p/text()").extract()
            item["category"] = key_lookup(self.categories, response.url)
            items.append(item)

        return items