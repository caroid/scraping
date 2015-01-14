# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from tutorial.items import TutorialItem
from selenium import webdriver

def removeUnicodes(strData):
        if(strData):
            strData = strData.encode('utf-8').strip()
            strData = re.sub(r'[\n\r\t]',r' ',strData.strip())
        return strData

class PamarillasSpider(BaseSpider):
    name = "pamarillas"
    allowed_domains = ["paginasamarillas.com.co"]
    start_urls = ['http://www.paginasamarillas.com.co/busqueda/empresas-bogota?match=empresas']

    driver = webdriver.Firefox()
    driver.get('http://www.paginasamarillas.com.co/busqueda/empresas-bogota?match=empresas')
    next_btn = driver.find_element_by_css_selector('.arrow-results.aw-rtl02.pager-link')
    links = driver.find_elements_by_css_selector('.send.show-contact-window')

    f = open('db.dat')

    for link in links:
        email = link.get_attribute('data-email')
        company = link.get_attribute('data-namecmp')

    driver.quit()