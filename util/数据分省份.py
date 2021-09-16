#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> 数据分省份
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-08-05 16:43
@Desc   ：
=================================================='''

from myJDBC.jdbc import mySqlJdbc
from util.httpTool import MyHttpToolUtil
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

httpTool = MyHttpToolUtil()
tool = MyToolUtil
ioTool = MyIoToolUtil
jdbc = mySqlJdbc()
"""
cahea

"""

# 北京  1
beijing = []
# 天津市 2
tianjin = []
# 上海市 3
shanghai = []
# 重庆市 4
chongqing = []
# 黑龙江 5
heilongjiang = []
# 吉林  6
jilin = []
# 辽宁  7
liaoning = []
# 河北  8
hebei = []
# 山西  9
shanxi = []
# 内蒙古 10
neimenggu = []

# 山东  11
shandong = []
# 江苏  12
jiangshu = []
# 浙江  13
zhejiang = []
# 安徽  14
anhui = []
# 福建  15
fujian = []
# 河南  16
henan = []
# 湖北  17
hubei = []
# 湖南  18
hunan = []
# 江西  19
jiangxi = []
# 四川  20
sichuan = []

# 云南  21
yunnan = []
# 贵州  22
guizhou = []
# 西藏  23
xizhang = []
# 宁夏  24
ningxia = []
# 新疆  25
xijiang = []
# 青海  26
qinhai = []
# 陕西  27
sanxi = []

# 甘肃  28
ganshu = []
# 广东  29
guangdong = []
# 广西  30
guangxi = []
# 海南  31
hunnan = []

sf_lv = {
    "北京": 1,
    "天津": 2,
    "上海": 3,
    "重庆": 4,
    # 黑龙江 5
    "哈尔滨": 5, "大庆": 5, "牡丹江": 5, "齐齐哈尔": 5, "鸡西": 5, "佳木斯": 5, "黑河": 5, "绥化": 5, "伊春": 5, "七台河": 5, "鹤岗": 5, "大兴安岭": 5,
    "双鸭山": 5, "甘南": 5,
    # 吉林  6
    "长春": 6, "吉林": 6, "通化": 6, "延边": 6, "松原": 6, "四平": 6, "白城": 6, "白山": 6, "辽源": 6,
    # 辽宁 7
    "沈阳": 7, "大连": 7, "鞍山": 7, "锦州": 7, '抚顺': 7, "葫芦岛": 7, "丹东": 7, "营口": 7, "辽阳": 7, "本溪": 7, "盘锦": 7, "阜新": 7,
    "铁岭": 7, "朝阳": 7,
    # 河北 8
    '石家庄': 8, '廊坊': 8, '保定': 8, '秦皇岛': 8, '唐山': 8, '邯郸': 8, '邢台': 8, '沧州': 8, '承德': 8, '张家口': 8, '衡水': 8,
    # 山西 9
    '太原': 9, '大同': 9, '临汾': 9, '长治': 9, '晋中': 9, '运城': 9, '晋城': 9, '阳泉': 9, '吕梁': 9, '忻州': 9, '朔州': 9,
    # 内蒙古 10
    '呼和浩特': 10, '包头': 10, '赤峰': 10, '呼伦贝尔': 10, '鄂尔多斯': 10, '通辽': 10, '巴彦淖尔': 10, '锡林郭勒': 10, '乌海': 10, '乌兰察布': 10,
    '兴安盟': 10, '阿拉善': 10,
    #     山东 11
    '青岛': 11, '济南': 11, '烟台': 11, '威海': 11, '潍坊': 11, '淄博': 11, '泰安': 11, '济宁': 11, '临沂': 11, '日照': 11, '东营': 11,
    '德州': 11, '滨州': 11, '聊城': 11, '枣庄': 11, '菏泽': 11,
    # 江苏  12
    '南京': 12, '苏州': 12, '无锡': 12, '常州': 12, '南通': 12, '扬州': 12, '镇江': 12, '徐州': 12, '连云港': 12, '泰州': 12, '淮安': 12,
    '盐城': 12, '宿迁': 12,
    # 浙江 13
    '杭州': 13, '宁波': 13, '嘉兴': 13, '温州': 13, '台州': 13, '金华': 13, '绍兴': 13, '湖州': 13, '舟山': 13, '衢州': 13, '丽水': 13,
    # 安徽 14
    '合肥': 14, '芜湖': 14, '黄山': 14, '蚌埠': 14, '马鞍山': 14, '宿州': 14, '淮南': 14, '安庆': 14, '滁州': 14, '阜阳': 14, '淮北': 14,
    '六安': 14, '巢湖': 14, '宣城': 14, '铜陵': 14, '池州': 14, '亳州': 14,
    # 福建 15
    '福州': 15, '厦门': 15, '泉州': 15, '宁德': 15, '漳州': 15, '南平': 15, '龙岩': 15, '三明': 15, '莆田': 15,
    # 河南    16
    '郑州': 16, '洛阳': 16, '新乡': 16, '许昌': 16, '开封': 16, '焦作': 16, '南阳': 16, '安阳': 16, '平顶山': 16, '商丘': 16, '信阳': 16,
    '濮阳': 16, '三门峡': 16, '周口': 16, '驻马店': 16, '漯河': 16, '鹤壁': 16, '济源': 16,
    # 湖北    17
    '武汉': 17, '宜昌': 17, '荆州': 17, '襄阳': 17, '黄石': 17, '十堰': 17, '孝感': 17, '荆门': 17, '黄冈': 17, '咸宁': 17, '恩施州': 17,
    '随州': 17, '潜江': 17, '鄂州': 17, '仙桃': 17, '天门': 17, '神农架林区': 17,
    # 湖南    18
    '长沙': 18, '湘西': 18, '株洲': 18, '张家界': 18, '衡阳': 18, '湘潭': 18, '岳阳': 18, '常德': 18, '邵阳': 18, '郴州': 18, '怀化': 18,
    '益阳': 18, '娄底': 18, '永州': 18,
    # 江西    19
    '南昌': 19, '赣州': 19, '九江': 19, '上饶': 19, '景德镇': 19, '吉安': 19, '宜春': 19, '新余': 19, '抚州': 19, '萍乡': 19, '鹰潭': 19,
    # 四川    20
    '成都': 20, '绵阳': 20, '乐山': 20, '自贡': 20, '德阳': 20, '南充': 20, '宜宾': 20, '达州': 20, '凉山': 20, '遂宁': 20, '泸州': 20,
    '雅安': 20, '广安': 20, '内江': 20, '阿坝': 20, '攀枝花': 20, '眉山': 20, '广元': 20, '甘孜州': 20, '资阳': 20, '巴中': 20,
    # 云南    21
    '昆明': 21, '丽江': 21, '大理州': 21, '西双版纳': 21, '玉溪': 21, '迪庆': 21, '曲靖': 21, '红河': 21, '保山': 21, '楚雄州': 21, '德宏': 21,
    '昭通': 21, '思茅': 21, '文山州': 21, '临沧': 21, '怒江': 21,
    # 贵州    22
    '贵阳': 22, '遵义': 22, '黔东南': 22, '安顺': 22, '黔西南': 22, '黔南': 22, '六盘水': 22, '铜仁地区': 22, '毕节地区': 22,
    # 西藏    23
    '拉萨': 23, '林芝地区': 23, '日喀则地区': 23, '山南': 23, '阿里': 23, '昌都地区': 23, '那曲': 23,
    # 宁夏    24
    '银川': 24, '石嘴山': 24, '吴忠': 24, '中卫': 24, '固原': 24,
    # 新疆    25
    '乌鲁木齐': 25, '巴音郭楞': 25, '克拉玛依': 25, '喀什地区': 25, '伊犁': 25, '石河子': 25, '昌吉州': 25, '哈密地区': 25, '阿勒泰地区': 25,
    '阿克苏地区': 25, '吐鲁番地区': 25, '塔城地区': 25, '和田地区': 25, '博尔塔拉': 25, '图木舒克': 25, '阿拉尔': 25, '北屯': 25, '五家渠': 25,
    '克孜勒苏': 25,
    # 青海    26
    '西宁': 26, '海西': 26, '海北': 26, '海东': 26, '海南州': 26, '玉树': 26, '果洛': 26, '黄南': 26,
    # 陕西    27
    '西安': 27, '宝鸡': 27, '咸阳': 27, '渭南': 27, '汉中': 27, '延安': 27, '榆林': 27, '安康': 27, '铜川': 27, '商洛': 27,
    # 甘肃    28
    '兰州': 28, '酒泉': 28, '天水': 28, '张掖': 28, '嘉峪关': 28, '庆阳': 28, '白银': 28, '平凉': 28, '武威': 28, '陇南': 28, '金昌': 28,
    '定西': 28, '临夏州': 28,
    # 广东    29
    '深圳': 29, '广州': 29, '佛山': 29, '珠海': 29, '东莞': 29, '汕头': 29, '中山': 29, '江门': 29, '惠州': 29, '阳江': 29, '肇庆': 29,
    '茂名': 29, '清远': 29, '湛江': 29, '韶关': 29, '梅州': 29, '揭阳': 29, '潮州': 29, '河源': 29, '汕尾': 29, '云浮': 29,
    # 广西    30
    '南宁': 30, '桂林': 30, '柳州': 30, '梧州': 30, '北海': 30, '贺州': 30, '钦州': 30, '贵港': 30, '玉林': 30, '百色': 30, '防城港': 30,
    '河池': 30, '崇左': 30, '来宾': 30,
    # 海南    31
    '三亚': 31, '海口': 31, '琼海': 31, '儋州': 31, '万宁': 31, '文昌': 31, '澄迈县': 31, '东方': 31, '陵水': 31, '保亭': 31, '定安县': 31,
    '五指山': 31, '临高县': 31, '乐东': 31, '屯昌县': 31, '琼中': 31, '白沙': 31, '昌江': 31,
}


def runHQList(sj_data_jg_list):
    for data in sj_data_jg_list:
        dz = data[7]
        for k in sf_lv:
            # print(k, "   ", sf_lv[k])
            if dz.find(k) > -1:
                idx = sf_lv[k]

            if idx != 0:
                if idx == 1:
                    print("beijing  1   ", k)
                    beijing.append(data)
                elif idx == 2:
                    print("tianjin  2   ", k)
                    tianjin.append(data)
                elif idx == 3:
                    print("shanghai 3   ", k)
                    shanghai.append(data)
                elif idx == 4:
                    print("chongqing 4   ", k)
                    chongqing.append(data)
                elif idx == 5:
                    print("heilongjiang 5   ", k)
                    heilongjiang.append(data)
                elif idx == 6:
                    print("jilin 6   ", k)
                    jilin.append(data)
                elif idx == 7:
                    print("liaoning  7   ", k)
                    liaoning.append(data)
                elif idx == 8:
                    print("hebei 8   ", k)
                    hebei.append(data)
                elif idx == 9:
                    print("shanxi 9   ", k)
                    shanxi.append(data)
                elif idx == 10:
                    print("neimenggu  10   ", k)
                    neimenggu.append(data)
                elif idx == 11:
                    print("shandong  11   ", k)
                    shandong.append(data)
                elif idx == 12:
                    print("jiangshu  12   ", k)
                    jiangshu.append(data)
                elif idx == 13:
                    print("zhejiang 13   ", k)
                    zhejiang.append(data)
                elif idx == 14:
                    print("anhui 14   ", k)
                    anhui.append(data)
                elif idx == 15:
                    print("fujian 15   ", k)
                    fujian.append(data)
                elif idx == 16:
                    print("henan  16   ", k)
                    henan.append(data)
                elif idx == 17:
                    print("hubei  17   ", k)
                    hubei.append(data)
                elif idx == 18:
                    print("hunan 18   ", k)
                    hunan.append(data)
                elif idx == 19:
                    print("jiangxi 19   ", k)
                    jiangxi.append(data)
                elif idx == 20:
                    print("sichuan  20   ", k)
                    sichuan.append(data)
                elif idx == 21:
                    print("yunnan  21   ", k)
                    yunnan.append(data)
                elif idx == 22:
                    print("guizhou  22   ", k)
                    guizhou.append(data)
                elif idx == 23:
                    print("xizhang  23   ", k)
                    xizhang.append(data)
                elif idx == 24:
                    print("ningxia  24   ", k)
                    ningxia.append(data)
                elif idx == 25:
                    print("xijiang 25   ", k)
                    xijiang.append(data)
                elif idx == 26:
                    print("qinhai  26   ", k)
                    qinhai.append(data)
                elif idx == 27:
                    print("sanxi  27   ", k)
                    sanxi.append(data)
                elif idx == 28:
                    print("ganshu  28   ", k)
                    ganshu.append(data)
                elif idx == 29:
                    print("guangdong  29   ", k)
                    guangdong.append(data)
                elif idx == 30:
                    print("guangxi  30   ", k)
                    guangxi.append(data)
                elif idx == 31:
                    print("hunnan  31   ", k)
                    hunnan.append(data)

    if 1 == 1:
        # ioTool.outXlsx(data=beijing, dataFile="F:\\list\\北京.xlsx")
        # ioTool.outXlsx(data=tianjin, dataFile="F:\\list\\天津市.xlsx")
        # ioTool.outXlsx(data=shanghai, dataFile="F:\\list\\上海市.xlsx")
        ioTool.outXlsx(data=chongqing, dataFile="F:\\list\\重庆市.xlsx")
        # ioTool.outXlsx(data=heilongjiang, dataFile="F:\\list\\黑龙江.xlsx")
        # ioTool.outXlsx(data=jilin, dataFile="F:\\list\\吉林.xlsx")
        # ioTool.outXlsx(data=liaoning, dataFile="F:\\list\\辽宁.xlsx")
        # ioTool.outXlsx(data=hebei, dataFile="F:\\list\\河北.xlsx")
        # ioTool.outXlsx(data=shanxi, dataFile="F:\\list\\山西.xlsx")
        # ioTool.outXlsx(data=neimenggu, dataFile="F:\\list\\内蒙古.xlsx")
        # ioTool.outXlsx(data=shandong, dataFile="F:\\list\\山东.xlsx")
        # ioTool.outXlsx(data=jiangshu, dataFile="F:\\list\\江苏.xlsx")
        # ioTool.outXlsx(data=zhejiang, dataFile="F:\\list\\浙江.xlsx")
        # ioTool.outXlsx(data=anhui, dataFile="F:\\list\\安徽.xlsx")
        # ioTool.outXlsx(data=fujian, dataFile="F:\\list\\福建.xlsx")
        # ioTool.outXlsx(data=henan, dataFile="F:\\list\\河南.xlsx")
        # ioTool.outXlsx(data=hubei, dataFile="F:\\list\\湖北.xlsx")
        # ioTool.outXlsx(data=hunan, dataFile="F:\\list\\湖南.xlsx")
        # ioTool.outXlsx(data=jiangxi, dataFile="F:\\list\\江西.xlsx")
        # ioTool.outXlsx(data=sichuan, dataFile="F:\\list\\四川.xlsx")
        # ioTool.outXlsx(data=yunnan, dataFile="F:\\list\\云南.xlsx")
        # ioTool.outXlsx(data=guizhou, dataFile="F:\\list\\贵州.xlsx")
        # ioTool.outXlsx(data=xizhang, dataFile="F:\\list\\西藏.xlsx")
        # ioTool.outXlsx(data=ningxia, dataFile="F:\\list\\宁夏.xlsx")
        # ioTool.outXlsx(data=xijiang, dataFile="F:\\list\\新疆.xlsx")
        # ioTool.outXlsx(data=qinhai, dataFile="F:\\list\\青海.xlsx")
        # ioTool.outXlsx(data=sanxi, dataFile="F:\\list\\陕西.xlsx")
        # ioTool.outXlsx(data=ganshu, dataFile="F:\\list\\甘肃.xlsx")
        # ioTool.outXlsx(data=guangdong, dataFile="F:\\list\\广东.xlsx")
        # ioTool.outXlsx(data=guangxi, dataFile="F:\\list\\广西.xlsx")
        # ioTool.outXlsx(data=hunnan, dataFile="F:\\list\\海南.xlsx")

    # exit()
    # print(zhejiang)
    # exit()
    # id = 31
    # cc = "三亚 海口 琼海 儋州 万宁 文昌 澄迈县 东方 陵水 保亭 定安县 五指山 临高县 乐东 屯昌县 琼中 白沙 昌江 "
    # cc_List = cc.split(" ")
    # # print(cc_List)
    # cccc = {}
    # for d in cc_List:
    #     skv = {d: id}
    #     cccc.update(skv)
    # print(cccc)

    # exit()
    # url = "http://www.xiaomishu.com/citylist/"
    # html_sele = httpTool.getSele_one_none(url=url)
    # # print(html_sele)
    # xpath_sf = "//dl[@class='mb20 fix']/dd[@class='mt20']/span[@class='g6 dib w100 l mr10 tc']/text()"
    # xpath_cs = "//dl[@class='mb20 fix']/dd[@class='mt20']/span[@class='g6 dib w100 l mr10 tc']/text()"
    # exit()
    # data_list = jdbc.get_BD_Data("")


if __name__ == '__main__':
    idx = 0
    sj_data_jg_list = jdbc.get_BD_Data_xims(dataBD="xiaomishu_data")
    sj_data_jg_list2 = jdbc.get_BD_Data_xims(dataBD="xiaomishu_data_copy1")
    print(sj_data_jg_list)
    print(sj_data_jg_list2)
    exit()