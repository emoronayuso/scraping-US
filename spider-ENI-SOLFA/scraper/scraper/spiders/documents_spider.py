#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scraper.items import DocumentItem
import urlparse

class Documents_spider(CrawlSpider):
    name = 'documents_spider'
    allowed_domains =['estudiantes.us.es',
            #'doctorado.us.es',
            'investigacion.us.es',
            'vtt.us.es'
            'internacional.us.es',
            'docentes.us.es',
            'sede.us.es',
            'recursoshumanos.us.es',
            'cfp.us.es',
            'sacu.us.es',
            'bib.us.es',
            'sav.us.es',
            'campusdeexcelencia.us.es'
            ]

    start_urls = ['http://estudiantes.us.es',
            #'http://www.doctorado.us.es',
            'http://investigacion.us.es',
            'http://vtt.us.es'
            'http://www.internacional.us.es',
            'http://docentes.us.es',
            'http://sede.us.es',
            'http://recursoshumanos.us.es/',
            'http://www.cfp.us.es/',
            'http://sacu.us.es/',
            #'http://bib.us.es/',
            'http://www.sav.us.es/',
            'http://campusdeexcelencia.us.es/'
            ]
    denied_locations = ['repositorio-tesis', 'sisius',
            'contenido/utils/codigos.php', 'calendario']
    rules = (
              Rule(LxmlLinkExtractor(deny=(denied_locations)),
                  callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DocumentItem()
        lx = LxmlLinkExtractor(
                allow=(r'.*\.xls$|.*\.xlsx$|.*\.doc$|.*\.docx$|.*\.ppt$|.*\.pptx$|.*\.odt$|.*\.ods$|.*\.odg$|.*\.odp$|.*\.pdf$'),
                deny_extensions=())
        for link in lx.extract_links(response):
            if link != {}:
                item['domain'] = urlparse.urlparse(response.url).netloc
                item['link'] = link.url
                item['location'] = response.url
                yield item
