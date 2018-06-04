# -*- coding: UTF-8 -*-
# by Wtting

from urllib import request,error
import random


# if __name__ == '__main__':


proxy_list = [
    # {'http': '203.174.112.13:3128'},
    # {'http': '218.73.130.59:6675'},
    # {'http': '115.202.233.151:46061'},
    # {'http': '114.238.130.120:22276'},
    # {'http': '218.73.135.170:22617'}
]

user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
        'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'UCWEB7.0.2.37/28/999',
        'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
        'Mozilla/4.0 (compatible; GoogleToolbar 6.1.1518.856; Windows XP 5.1; MSIE 6.0.2900.5512)',
        'Mozilla/4.0 (compatible; IE7 - Provided by www.agileict.co.uk; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)',
        'Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Qtek9090; PPC; 240x320)',
        'Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; SPV M700; OpVer 19.123.1.615)',
        'Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Smartphone; 176x220; i930A; 4.21.1088; 000805614955330)',
        'Mozilla/4.0 (compatible; MSIE 4.01; Windows NT Windows CE)',
        'Mozilla/4.0 (compatible; MSIE 4.01; Windows NT) WebWasher 3.3',
        'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; FunWebProducts; ZangoToolbar 4.8.3; SpamBlockerUtility 4.8.0; HbTools 4.8.4)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; InfoPath.2)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; .NET CLR 2.0.50727)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; .NET CLR 2.0.50727; InfoPath.1; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; Media Center PC 3.0; .NET CLR 1.0.3705)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB6; QQDownload 1.7)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GoogleT5; (R1 1.6); .NET CLR 2.0.50727)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB5; Sky Broadband; .NET CLR 1.1.4322)'
]


def get_Agent():
    # 随机选择一个头部
    user_agent = random.choice(user_agent_list)
    # print(user_agent)
    return user_agent


def get_Proxy():
    # 随机选择一个代理
    proxy = random.choice(proxy_list)
    # print(proxy)
    return proxy


