# -*- coding: UTF-8 -*-
"""
@Time: 2018/6/29 9:53
@Author: TingTing W
"""

import logging.handlers


class MyLog:

    def __init__(self, name):
        self.name = name
        print(name)

    @staticmethod
    def init_logger():

        LOG_FILE = r'tst.log'

        # 实例化handler
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
        fmt = '%(asctime)s - %(levelname)s - %(message)s'

        # 实例化formatter
        formatter = logging.Formatter(fmt)
        # 为handler添加formatter
        handler.setFormatter(formatter)

        # 获取名为tst的logger
        logger = logging.getLogger('tst')
        # 为logger添加handler
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger;
    """
    if __name__ == '__main__':
        logger = init_logger()
        logger.info("王婷婷")
    """
