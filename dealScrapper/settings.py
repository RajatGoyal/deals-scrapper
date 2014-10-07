# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DealScrapper'

SPIDER_MODULES = ['DealScrapper.spiders']
NEWSPIDER_MODULE = 'DealScrapper.spiders'
FEED_FORMAT = 'json'
FEED_URI = 'file:///test/test.json'

ITEM_PIPELINES = {
    'DealScrapper.pipelines.CleanItemPipeline': 200,
    'DealScrapper.pipelines.DumpItemPipeLine': 300
}
#


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
