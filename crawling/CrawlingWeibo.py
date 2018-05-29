# -*- coding: UTF-8 -*-
# by Wtting

import urllib
import sys

def login(user_name, password, opener):
    LOGGER.info(user_name + ' login')
    args = {
        'username': user_name,
        'password': password,
        'savestate': 1,
        'ec': 0,
        'pagerefer': 'https://passport.weibo.cn/signin/'
                     'welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'hff': '',
        'hfp': ''
    }

    '''
        # 访问网址
        #url = "http://www.baobeihuijia.com/list.aspx?tid=1"
        #随机选择一个代理
        proxy = random.choice(proxy_list)
        print(proxy)
        #随机选择一个头部
        user_agent = random.choice(user_agent_list)
        print(user_agent)
        #使用选择的代理构建代理处理器对象
        proxyHandler = request.ProxyHandler(proxy)
        #创建opener
        opener = request.build_opener(proxyHandler)
        #添加头部
        opener.addheaders = [('User-Agent',user_agent)]
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
        '''
    post_data = urllib.parse.urlencode(args).encode()
    try_time = 0
    while try_time < constants.TRY_TIME:
        try:
            resp = opener.open(constants.LOGIN_URL, post_data)
            resp_json = json.loads(resp.read().decode())
            if 'retcode' in resp_json and resp_json['retcode'] == '20000000':
                LOGGER.info("%s login successful" % user_name)
                break
            else:
                LOGGER.warn('login fail:%s' % str(resp_json))
                sleep(10)
                try_time += 1
        except :
            LOGGER.error("login failed")
            LOGGER.error(traceback.print_exc())
            sleep(10)
            try_time += 1
            LOGGER.info('try %d time' % try_time)