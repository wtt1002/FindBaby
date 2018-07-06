# -*- coding: UTF-8 -*-
"""
@Time: 2018/7/5 16:56
@Author: TingTing W
"""

import xlrd

"""
    初始化map
"""
# 地区与编码对应表
district_maps = {}
# 省份与编码对应表
province_maps = {}


def init_map():
    # 读取excel
    src_book = xlrd.open_workbook(r'E:\districtCode.xlsx')
    ws_src = src_book.sheet_by_name('Sheet')
    for i in range(0, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取地址
        district_name = row_values[1]
        # 获取编码
        district_code = row_values[0]
        # print(district_name)
        # print(district_code)
        province_maps.update({district_name: district_code})
    print(province_maps)


if __name__ == '__main__':
    init_map()