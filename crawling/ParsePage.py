# -*- coding: UTF-8 -*-
# by Wtting

import json
import re


def parse_total_page(html):
    if html == 'fail':
        print('parse_one_page_fail')
        return 'fail'
    patten = re.compile('<input id="(.+?)-hid" value=.*? />',re.S)
    items = re.findall(patten, html)
    '''
    for item in items:
        # print(item)
        yield {
            'id': item
       }
    '''
    return items


def get_detail_info(html):
    if html == 'fail':
        print('get_detail_info_fail')
        return 'fail'
    pattern = re.compile('<li><span>.*?</span>(.*?)</li>', re.S)
    info_items = re.findall(pattern, html)  # 解析详情页的数据
    print('  宝贝详情: ' + str(info_items))
    print('——————————————————————————————————————————————————————————————————————————————————————————————————————')
    return info_items


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