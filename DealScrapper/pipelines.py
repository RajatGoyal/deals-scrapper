# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from DealScrapper.utils import removeNonAscii

class CleanItemPipeline(object):
    def __init__(self):
        self.file = open('test.json', 'wb')

    def process_item(self, item, spider):
        for key, value in item.iteritems():
            if key not in ['link']:
                # Convert list to string and Remove special characters
                value = removeNonAscii("".join(value)).replace('|', "").replace('?',"")
                # Remove extra white spaces
                value = ' '.join(value.split())
                item[key] = value
            else:
                values = []
                for link in value:
                    values.append(link.replace('http://www.savemoneyindia.com/url.php?go=', '').replace('http://freekaamaal.com/links?', ''))
                item[key] = values

        return item

class DumpItemPipeLine(object):

    def process_item(self, item, spider):
        # conn = MySQLdb.connect(host='127.0.0.1',
        #                user='shopsense',
        #                passwd='captureretail',
        #                db='dealado')
        # cur = conn.cursor()
        # command = """INSERT INTO deals (title, link, description, category, image_url, deal_timestamp, approved) VALUES ("{}","{}","{}","{}","{}","{}",0);""".format(item.get('title', ""), "|||".join(item.get('link', [])), item.get("desc", ""), item.get('category', ""), item.get('image_url', ""), item.get('timestamp', 0), item.get('approved', 0))
        # cur.execute(command)
        # conn.commit()
        # return item
        pass