# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
FEED_FORMAT = 'json'
FEED_URI = 'file:///test/test.json'

ITEM_PIPELINES = {
    'tutorial.pipelines.CleanItemPipeline': 200,
    'tutorial.pipelines.DumpItemPipeLine': 300
}
#

# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# MONGODB_DATABASE = 'myDatabaseName'
# MONGODB_COLLECTION = 'myCollectionName'
#
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
