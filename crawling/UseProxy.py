# -*- coding: UTF-8 -*-
# by Wtting

from urllib import request

if __name__ == '__main__':
    #访问网址
    url = 'http://www.cip.cc/'
    #代理IP
    proxy = {'http':'203.174.112.13:3128'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User-Agent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装Opener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)
    #关闭response
    response.close()