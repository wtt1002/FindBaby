# -*- coding: UTF-8 -*-
"""
@Time: 2018/7/5 16:56
@Author: TingTing W
"""

import xlrd

"""
    初始化map
    districtCode.xlsx : 省份与城市编码表
"""
# 地区与编码对应表
district_maps = {}
# 省份与编码对应表
province_maps = {}


# 初始化省份map
def init_map_pro():
    # 读取excel
    src_book = xlrd.open_workbook(r'E:\districtCode.xlsx')
    ws_src = src_book.sheet_by_name('Sheet')
    for i in range(0, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取省份地址名称
        district_name = row_values[3]
        # 获取省份编码
        district_code = row_values[2]
        # print(district_name)
        # print(district_code)
        province_maps.update({district_name: district_code})
    print(province_maps)


# 初始化地区map
def init_map_dis():
    # 读取excel
    src_book = xlrd.open_workbook(r'E:\districtCode.xlsx')
    ws_src = src_book.sheet_by_name('Sheet')
    for i in range(0, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取地区城市名称
        district_name = row_values[1]
        # 获取地区城市编码
        district_code = row_values[0]
        # print(district_name)
        # print(district_code)
        district_maps.update({district_name: district_code})
    print(district_maps)


if __name__ == '__main__':
    init_map_pro()
    init_map_dis()