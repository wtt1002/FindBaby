# -*- coding: UTF-8 -*-
"""
@Time: 2018/7/5 14:19
@Author: TingTing W
"""
import xlrd
import xlwt
from markdata import dicts

district_maps = dicts.district_maps
province_maps = dicts.province_maps


def code_pro_dis():

    src_book = xlrd.open_workbook(r'E:\标签化测试.xlsx')
    ws_src = src_book.sheet_by_name('Sheet')
    # 书写目的文件
    # 创建一个workbook 设置编码
    des_book = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    ws_des = des_book.add_sheet('Worksheet')
    for i in range(0, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取地址
        src_province_name = row_values[7].replace(' ', '')
        src_distinct_name = row_values[8].replace(' ', '')
        now_province_name = row_values[9].replace(' ', '')
        now_distinct_name = row_values[10].replace(' ', '')
        """
        print("========================")
        print("1111")
        print(province_maps.get(src_province_name))
        print("2222")
        print(district_maps.get(src_distinct_name))
        print("3333")
        print(province_maps.get(now_province_name))
        print("4444")
        print(district_maps.get(now_distinct_name))
        """
        ws_des.write(i, 0, province_maps.get(src_province_name))
        ws_des.write(i, 1, district_maps.get(src_distinct_name))
        ws_des.write(i, 2, province_maps.get(now_province_name))
        ws_des.write(i, 3, district_maps.get(now_distinct_name))
        des_book.save('demo.xls')


if __name__ == '__main__':
    code_pro_dis()




    """
    # 读取excel
    src_book = xlrd.open_workbook(r'E:\districtCode.xlsx')
    ws_src = src_book.sheet_by_name('Sheet1')
    for i in range(2, ws_src.nrows):
        # 获取原excel中的一行数据
        row_values = ws_src.row_values(i)
        # 获取地址
        district_name = row_values[1]
        # 获取编码
        district_code = row_values[0]
        print(district_name)
    """
"""
1301,石家庄市,13
1302,唐山市,13
1303,秦皇岛市,13
1304,邯郸市,13
1305,邢台市,13
1306,保定市,13
1307,张家口市,13
1308,承德市,13
1309,沧州市,13
1311,衡水市,13
1401,太原市,14
1402,大同市,14
1403,阳泉市,14
1404,长治市,14
1405,晋城市,14
1406,朔州市,14
1407,晋中市,14
1408,运城市,14
1409,忻州市,14
1411,吕梁市,14
1501,呼和浩特市,15
1502,包头市,15
1503,乌海市,15
1504,赤峰市,15
1505,通辽市,15
1506,鄂尔多斯市,15
1507,呼伦贝尔市,15
1508,巴彦淖尔市,15
1509,乌兰察布市,15
1522,兴安盟,15
1525,锡林郭勒盟,15
1529,阿拉善盟,15
2101,沈阳市,21
2102,大连市,21
2103,鞍山市,21
2104,抚顺市,21
2105,本溪市,21
2106,丹东市,21
2107,锦州市,21
2108,营口市,21
2109,阜新市,21
2111,盘锦市,21
2112,铁岭市,21
2113,朝阳市,21
2114,葫芦岛市,21
2201,长春市,22
2202,吉林市,22
2203,四平市,22
2204,辽源市,22
2205,通化市,22
2206,白山市,22
2207,松原市,22
2208,白城市,22
2224,延边朝鲜族自治州,22
2301,哈尔滨市,23
2302,齐齐哈尔市,23
2303,鸡西市,23
2304,鹤岗市,23
2305,双鸭山市,23
2306,大庆市,23
2307,伊春市,23
2308,佳木斯市,23
2309,七台河市,23
2311,黑河市,23
2312,绥化市,23
2327,大兴安岭地区,23
3201,南京市,32
3202,无锡市,32
3203,徐州市,32
3204,常州市,32
3205,苏州市,32
3206,南通市,32
3207,连云港市,32
3208,淮安市,32
3209,盐城市,32
3211,镇江市,32
3212,泰州市,32
3213,宿迁市,32
3301,杭州市,33
3302,宁波市,33
3303,温州市,33
3304,嘉兴市,33
3305,湖州市,33
3306,绍兴市,33
3307,金华市,33
3308,衢州市,33
3309,舟山市,33
3311,丽水市,33
3401,合肥市,34
3402,芜湖市,34
3403,蚌埠市,34
3404,淮南市,34
3405,马鞍山市,34
3406,淮北市,34
3407,铜陵市,34
3408,安庆市,34
3411,滁州市,34
3412,阜阳市,34
3413,宿州市,34
3415,六安市,34
3416,亳州市,34
3417,池州市,34
3418,宣城市,34
3501,福州市,35
3502,厦门市,35
3503,莆田市,35
3504,三明市,35
3505,泉州市,35
3506,漳州市,35
3507,南平市,35
3508,龙岩市,35
3509,宁德市,35
3601,南昌市,36
3602,景德镇市,36
3603,萍乡市,36
3604,九江市,36
3605,新余市,36
3606,鹰潭市,36
3607,赣州市,36
3608,吉安市,36
3609,宜春市,36
3611,上饶市,36
3701,济南市,37
3702,青岛市,37
3703,淄博市,37
3704,枣庄市,37
3705,东营市,37
3706,烟台市,37
3707,潍坊市,37
3708,济宁市,37
3709,泰安市,37
3711,日照市,37
3712,莱芜市,37
3713,临沂市,37
3714,德州市,37
3715,聊城市,37
3716,滨州市,37
3717,菏泽市,37
4101,郑州市,41
4102,开封市,41
4103,洛阳市,41
4104,平顶山市,41
4105,安阳市,41
4106,鹤壁市,41
4107,新乡市,41
4108,焦作市,41
4109,濮阳市,41
4111,漯河市,41
4112,三门峡市,41
4113,南阳市,41
4114,商丘市,41
4115,信阳市,41
4116,周口市,41
4117,驻马店市,41
4201,武汉市,42
4202,黄石市,42
4203,十堰市,42
4205,宜昌市,42
4206,襄阳市,42
4207,鄂州市,42
4208,荆门市,42
4209,孝感市,42
4211,黄冈市,42
4212,咸宁市,42
4213,随州市,42
4228,恩施土家族苗族自治州,42
4290,仙桃市
4290,潜江市
4290,天门市
4290,神农架林区
4301,长沙市,43
4302,株洲市,43
4303,湘潭市,43
4304,衡阳市,43
4305,邵阳市,43
4306,岳阳市,43
4307,常德市,43
4308,张家界市,43
4309,益阳市,43
4311,永州市,43
4312,怀化市,43
4313,娄底市,43
4331,湘西土家族苗族自治州,43
4401,广州市,44
4402,韶关市,44
4403,深圳市,44
4404,珠海市,44
4405,汕头市,44
4406,佛山市,44
4407,江门市,44
4408,湛江市,44
4409,茂名市,44
4412,肇庆市,44
4413,惠州市,44
4414,梅州市,44
4415,汕尾市,44
4416,河源市,44
4417,阳江市,44
4418,清远市,44
4419,东莞市,44
4420,中山市
4451,潮州市,44
4452,揭阳市,44
4453,云浮市,44
4501,南宁市,45
4502,柳州市,45
4503,桂林市,45
4504,梧州市,45
4505,北海市,45
4506,防城港市,45
4507,钦州市,45
4508,贵港市,45
4509,玉林市,45
4511,贺州市,45
4512,河池市,45
4513,来宾市,45
4514,崇左市,45
4601,海口市,46
4602,三亚市,46
4603,三沙市
4604,儋州市
4690,五指山市
4690,琼海市
4690,文昌市
4690,万宁市
4690,东方市
4690,定安县
4690,屯昌县
4690,澄迈县
4690,临高县
4690,白沙黎族自治县
4690,昌江黎族自治县
4690,乐东黎族自治县
4690,陵水黎族自治县
4690,保亭黎族苗族自治县
4690,琼中黎族苗族自治县
5101,成都市,51
5103,自贡市,51
5104,攀枝花市,51
5105,泸州市,51
5106,德阳市,51
5107,绵阳市,51
5108,广元市,51
5109,遂宁市,51
5111,乐山市,51
5113,南充市,51
5114,眉山市,51
5115,宜宾市,51
5116,广安市,51
5117,达州市,51
5118,雅安市,51
5119,巴中市,51
5120,资阳市
5132,阿坝藏族羌族自治州,51
5133,甘孜藏族自治州,51
5134,凉山彝族自治州,51
5201,贵阳市,52
5202,六盘水市,52
5203,遵义市,52
5204,安顺市,52
5205,毕节市,52
5206,铜仁市,52
5223,黔西南布依族苗族自治州,52
5226,黔东南苗族侗族自治州,52
5227,黔南布依族苗族自治州,52
5301,昆明市,53
5303,曲靖市,53
5304,玉溪市,53
5305,保山市,53
5306,昭通市,53
5307,丽江市,53
5308,普洱市,53
5309,临沧市,53
5323,楚雄彝族自治州,53
5325,红河哈尼族彝族自治州,53
5326,文山壮族苗族自治州,53
5328,西双版纳傣族自治州,53
5329,大理白族自治州,53
5331,德宏傣族景颇族自治州,53
5333,怒江傈僳族自治州,53
5334,迪庆藏族自治州,53
5401,拉萨市,54
5402,日喀则市
5403,昌都地区,54
5404,林芝市
5405,山南市,54
5424,那曲地区,54
5425,阿里地区,54
6101,西安市,61
6102,铜川市,61
6103,宝鸡市,61
6104,咸阳市,61
6105,渭南市,61
6106,延安市,61
6107,汉中市,61
6108,榆林市,61
6109,安康市,61
6110,商洛市
6201,兰州市,62
6202,嘉峪关市,62
6203,金昌市,62
6204,白银市,62
6205,天水市,62
6206,武威市,62
6207,张掖市,62
6208,平凉市,62
6209,酒泉市,62
6211,定西市,62
6212,陇南市,62
6229,临夏回族自治州,62
6230,甘南藏族自治州
6301,西宁市,63
6302,海东市,63
6322,海北藏族自治州,63
6323,黄南藏族自治州,63
6325,海南藏族自治州,63
6326,果洛藏族自治州,63
6327,玉树藏族自治州,63
6328,海西蒙古族藏族自治州,63
6401,银川市,64
6402,石嘴山市,64
6403,吴忠市,64
6404,固原市,64
6405,中卫市,64
6501,乌鲁木齐市,65
6502,克拉玛依市,65
6504,吐鲁番地区,65
6505,哈密地区,65
6523,昌吉回族自治州,65
6527,博尔塔拉蒙古自治州,65
6528,巴音郭楞蒙古自治州,65
6529,阿克苏地区,65
6530,克孜勒苏柯尔克孜自治州
6531,喀什地区,65
6532,和田地区,65
6540,伊犁哈萨克自治州
6542,塔城地区,65
6543,阿勒泰地区,65
6590,石河子市
6590,阿拉尔市
6590,图木舒克市
6590,五家渠市
6590,铁门关市
"""
