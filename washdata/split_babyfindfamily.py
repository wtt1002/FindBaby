# -*- coding: UTF-8 -*-
"""
@Time: 2018/7/5 20:38
@Author: TingTing W
"""
# import openpyxl
import xlrd
import xlwt
import json
#import gc


# 错误信息
def write_to_file(content):
    with open('FailString.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()


# str转int
def str_to_int(str):
    return int(str)


# 地址分解
def split_double_address(address):
    index = 0
    try:
        address_splits = address.split(u',')
    except AttributeError:
        return None
    for addr in address_splits:
        index += 1
    for i in range(index, 4):
        address_splits.append('kong')
    return address_splits


# 时间分解
def split_double_time(time):
    #index = 0
    if '0'<=time[0]<='9':
        time_splits = ['', '', '']
        try:
            time_splits[0] = time.split('年')[0]  # year
            time_splits[1] = time.split('年')[1].split('月')[0]  # month
            time_splits[2] = time.split('年')[1].split('月')[1].split('日')[0]  # day
        except AttributeError:
            return None

        time_splits[0] = str_to_int(time_splits[0])
        time_splits[1] = str_to_int(time_splits[1])
        time_splits[2] = str_to_int(time_splits[2])


    return time_splits


if __name__ == '__main__':

    # 源数据集文件
    src_path = r'E:\20180703.xlsx'
    src_book = xlrd.open_workbook(src_path)
    ws_src = src_book.sheet_by_name('Sheet')
    # 目的数据文件
    des_book = xlwt.Workbook(encoding='utf-8')
    ws_des = des_book.add_sheet('Worksheet')
    # ws_des.append(['失踪人所在省份', '失踪人所在城市', '详细', '空白', '失踪省份', '失踪城市', '详细', '空白'])
    # ws_des.append(['寻亲类别', '寻亲编号', '姓名', '性别', '出生年份', '出生月份', '出生日', '失踪时身高', '失踪年份', '失踪月份', '失踪日', '失踪省份', '失踪城市', '失踪人现在省份', '失踪人现在城市', '描述', '其他信息'])
    i = 0
    ws_des.write(i, 0, '寻亲类别')
    ws_des.write(i, 1, '寻亲编号')
    ws_des.write(i, 2, '姓名')
    ws_des.write(i, 3, '性别')
    ws_des.write(i, 4, '出生年份')
    ws_des.write(i, 5, '出生月份')
    ws_des.write(i, 6, '出生日')
    ws_des.write(i, 7, '失踪时身高')
    ws_des.write(i, 8, '失踪年份')
    ws_des.write(i, 9, '失踪月份')
    ws_des.write(i, 10, '失踪日')
    ws_des.write(i, 11, '失踪人现在省份')
    ws_des.write(i, 12, '失踪人现在城市')
    ws_des.write(i, 13, '失踪省份')
    ws_des.write(i, 14, '失踪城市')
    ws_des.write(i, 15, '描述')
    ws_des.write(i, 16, '其他信息')
    des_book.save('demo1.xls')
    sum = 0 #计数
    for i in range(1, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取地址
        # 寻亲类别
        searchClass = row_values[0]
        #寻亲编号
        searchNumber = row_values[1]
        #姓名
        name = row_values[2]
        #性别
        gender = row_values[3]
        if gender != '男' and gender != '女':
            gender = '不明'
        # 出生日期
        birthInfo = row_values[4]
        birthDay = split_double_time(birthInfo)
        if birthDay is None:
            write_to_file(birthInfo)

        #失踪时身高
        height = row_values[5]
        # 失踪日期
        lostInfo = row_values[6]
        lostDay = split_double_time(lostInfo)
        if lostDay is None:
            birthDay = ['空', '空', '空']
            write_to_file(lostInfo)

        # 现在的地址信息
        now_addr_info = row_values[7]
        nowAddr = split_double_address(now_addr_info)
        if nowAddr is None:
            nowAddr = ['空', '空']
            write_to_file(now_addr_info)

        # 失踪地的地址信息
        pre_addr_info = row_values[8]
        preAddr = split_double_address(pre_addr_info)
        if preAddr is None:
            preAddr = ['空', '空']
            write_to_file(pre_addr_info)

        #描述
        discription = row_values[9]

        # 其他信息
        other_info = row_values[10]

        # 数据拼接
        '''
        for time in lostDay:
            birthDay.append(time)
        for addr in preAddr:
            birthDay.append(addr)
        for addr in nowaddr:
            birthDay.append(addr)
        '''
        sum += 1
        # 写入excel
        # ws_des.append([searchClass, searchNumber, name, gender, birthDay[0], birthDay[1], birthDay[2], height, lostDay[0], lostDay[1], lostDay[2], nowAddr[0], nowAddr[1], preAddr[0], preAddr[1], discription, other_info])
        ws_des.write(i, 0, searchClass)
        ws_des.write(i, 1, searchNumber)
        ws_des.write(i, 2, name)
        ws_des.write(i, 3, gender)
        ws_des.write(i, 4, birthDay[0])
        ws_des.write(i, 5, birthDay[1])
        ws_des.write(i, 6, birthDay[2])
        ws_des.write(i, 7, height)
        ws_des.write(i, 8, lostDay[0])
        ws_des.write(i, 9, lostDay[1])
        ws_des.write(i, 10, lostDay[2])
        ws_des.write(i, 11, nowAddr[0])
        ws_des.write(i, 12, nowAddr[1])
        ws_des.write(i, 13, preAddr[0])
        ws_des.write(i, 14, preAddr[1])
        ws_des.write(i, 15, discription)
        ws_des.write(i, 16, other_info)

        print(sum)
        des_book.save('demo1.xls')
        '''
        del searchClass
        del searchNumber
        del name
        del gender
        del birthInfo
        del birthDay
        del height
        del lostDay
        del now_addr_info
        del nowAddr
        del pre_addr_info
        del preAddr
        del discription
        del other_info
        gc.collect()
        '''

