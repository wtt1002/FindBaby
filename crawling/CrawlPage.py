# -*- coding: UTF-8 -*-
# by Wtting

from urllib import error
from crawling import UseProxys
import requests
from openpyxl.utils.exceptions import IllegalCharacterError
from requests.exceptions import RequestException, ReadTimeout

def getPage(url):

    """
    # 访问网址
    # url = 'http://www.baobeihuijia.com/list.aspx?tid=1'
    # 获取proxy 和 agent
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
    """
    # 获取随机的浏览器代理
    user_agent = UseProxys.get_Agent()
    # print('浏览器代理: ' + user_agent)
    headers = {
        "User-Agent": user_agent
    }
    try:
        # 使用自己安装好的Opener
        # response = request.urlopen(url)
        response = requests.get(url, headers=headers)
        # if response.status_code == 200:
        #   return response.content.decode('utf-8')
        # 读取相应信息并解码
        # html = response.read().decode("utf-8")
    except ReadTimeout:
        print('Timeout')
        return None
    except ConnectionError:
        print('Connection error')
        return None
    except RequestException:
        print('Error')
        return None
    except error.URLError as e:
        return None

    # 打印信息
    # print(html)
    # 关闭response
    response.close()
    return response.content.decode('utf-8')