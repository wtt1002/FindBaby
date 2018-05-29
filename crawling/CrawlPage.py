# -*- coding: UTF-8 -*-
# by Wtting

from urllib import request,error
from crawling import UseProxys
def getPage(url):
    # 访问网址
    #url = 'http://www.baobeihuijia.com/list.aspx?tid=1'
    #获取proxy 和 agent
    proxy = UseProxys.get_Proxy()
    user_agent = UseProxys.get_Agent()
    # 使用选择的代理构建代理处理器对象
    proxyHandler = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxyHandler)
    # 添加头部
    opener.addheaders = [('User-Agent', user_agent)]
    # 安装Opener
    request.install_opener(opener)

    try:
        # 使用自己安装好的Opener
        response = request.urlopen(url)
    except error.URLError as e:
        print(e.reason)

    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)
    # 关闭response
    response.close()
    return html