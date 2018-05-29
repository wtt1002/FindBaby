# -*- coding: UTF-8 -*-
# by Wtting
from crawling import CrawlPage
from crawling import ParsePage


def execute(page):
    url = 'http://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=&page='+str(page)
    print(url)
    html = CrawlPage.getPage(url)
    for item in ParsePage.parse_total_page(html):
        print(item)
        ParsePage.write_to_file(item)

if __name__ == '__main__':
    for i in range(3):
        execute(i)




