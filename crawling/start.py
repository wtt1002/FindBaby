# -*- coding: UTF-8 -*-
# create by WangTingTing
from crawling import CrawlPage
from crawling import ParsePage
import time
import random


def execute(page):
    url = 'http://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=&page='+str(page)
    print(url)
    html = CrawlPage.getPage(url)
    for item in ParsePage.parse_total_page(html):
        print(item)
        ParsePage.write_to_file(item)


if __name__ == '__main__':

    for i in range(86, 100):
        execute(i)
        time.sleep(random.random() * 10)




