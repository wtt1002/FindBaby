# -*- coding: UTF-8 -*-
"""
@Time: 2018/6/8 15:38
@Author: TingTing W
"""
"""
利用高德地图api实现地址和经纬度的转换
"""

import random
import time

import requests
import xlrd
import xlwt


def read_excel():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Worksheet')
    # 读取excel
    ExcelFile = xlrd.open_workbook(r'E:\city_info.xlsx')
    # 获取目标EXCEL文件sheet名
    # print(ExcelFile.sheet_names())
    # 获取sheet内容【1.根据sheet索引2.根据sheet名称】
    # sheet=ExcelFile.sheet_by_index(1)
    sheet = ExcelFile.sheet_by_name('city_info')
    print(sheet.nrows)
    # sheet.nrows
    for row_number in range(1, sheet.nrows + 1):
        row_values_new = []  # 将要写入excel的一行数据保存在一个字典里
        row_values = sheet.row_values(row_number)  # 获取原excel中的一行数据
        # 失踪人现在所在地
        now_location = row_values[0]  # 将省和市拼接在一起
        geocode_result = geocode(now_location)
        if geocode_result is not None:
            now_location_latlng = geocode_result.split(',')
        else:
            print('\033[1;31;m' + 'None' + '\033[0m')
            continue
        # 将数据添加到row_values_new中
        row_values_new.append(now_location)
        row_values_new.append(now_location_latlng[0])
        row_values_new.append(now_location_latlng[1])
        # 控制台输出row_values_new
        print(row_values_new)
        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(row_number, 0, row_values_new[0])  # 往第row_number行第0列写入数据row_values_new[0]
        worksheet.write(row_number, 1, row_values_new[1])
        worksheet.write(row_number, 2, row_values_new[2])
        # 保存excel
        workbook.save('城市经纬度.xls')
        print('\033[1;32;m' + '写入成功: 第' + str(
            row_number) + '个' + '\033[0m')


def geocode(address):
    random_sleep_time = random.uniform(0.200002, 0.5000001)
    time.sleep(random_sleep_time)
    count = 20
    while count > 0:
        try:
            parameters = {'address': address, 'key': 'a5717efe281fea54c2a03cc00310ae08'}
            base = 'http://restapi.amap.com/v3/geocode/geo'
            # 响应请求
            response = requests.get(base, parameters, timeout=2)
            answer = response.json()
            print(answer)
            if answer is not None:
                # print(answer['geocodes'][0]['location'])
                return answer['geocodes'][0]['location']
            else:
                return None
        except:
            count -= 1
            print('\033[1;31;m' + 'error' + '\033[0m')
    return None


if __name__ == '__main__':
    read_excel()
    # geocode("潮汕地区")
