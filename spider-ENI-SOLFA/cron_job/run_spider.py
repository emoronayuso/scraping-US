#/usr/bin/python
# -*- coding: utf-8 -*-

import os

root_directory = '/home/kike/scraping-US/spider-ENI-SOLFA/'

os.chdir(root_directory+'scraper')
os.system("scrapy crawl documents_spider -o documents.json ")

