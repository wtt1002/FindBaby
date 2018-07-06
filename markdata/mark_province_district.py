# -*- coding: UTF-8 -*-
"""
@Time: 2018/7/5 14:19
@Author: TingTing W
"""
import xlrd
import xlwt
from markdata import dicts
from log import MyLog
district_maps = dicts.district_maps
province_maps = dicts.province_maps
city = 1
province = 0


# 1：城市  0：省份
def get_code(type, name):
    if type == 1:
        code_city = district_maps.get(name)
        if code_city is None:
            return name
        else:
            return code_city
    elif type == 0:
        code_prov = province_maps.get(name)
        if code_prov is None:
            return name
        else:
            return code_prov
    else: return 'NONE'


def code_pro_dis():

    # 源文件
    src_book = xlrd.open_workbook(r'E:\标签化测试.xlsx')
    ws_src = src_book.sheet_by_name('Sheet')
    # 书写目的文件
    # 创建一个workbook 设置编码
    des_book = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    ws_des = des_book.add_sheet('Worksheet')
    # 日志文件
    log = MyLog.MyLog("test")
    logger = log.init_logger()
    for i in range(0, ws_src.nrows):
        try:
            # 获取原excel中的一行数据
            row_values = ws_src.row_values(i)
            # 获取地址
            src_province_name = row_values[7].replace(' ', '')
            src_distinct_name = row_values[8].replace(' ', '')
            now_province_name = row_values[9].replace(' ', '')
            now_distinct_name = row_values[10].replace(' ', '')

            ws_des.write(i, 0, get_code(province, src_province_name))
            ws_des.write(i, 1, get_code(city, src_distinct_name))
            ws_des.write(i, 2, get_code(province, now_province_name))
            ws_des.write(i, 3, get_code(city, now_distinct_name))

            des_book.save('demo.xls')
        except IOError:
            logger.error(i+"行出错")
        logger.info(i)


if __name__ == '__main__':
    code_pro_dis()
