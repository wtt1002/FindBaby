# -*- coding: UTF-8 -*-
# by Wtting

import json
import re
from crawling import CrawlPage
def parse_total_page(html):
    patten = re.compile('<input id="(.+?)-hid" value=.*? />',re.S)
    items = re.findall(patten,html)
    for item in items:
        #print(item)
        yield {
            'id':item
       }

def write_to_file(content):
    with open('test1.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
'''
if __name__ == '__main__':
    url = 'http://www.baobeihuijia.com/list.aspx?tid=1'
    html = CrawlPage.getPage(url)
    for item in parse_total_page(html):
        print(item)
        write_to_file(item)
'''