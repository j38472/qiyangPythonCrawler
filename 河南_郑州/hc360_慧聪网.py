#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> hc360_慧聪网
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-29 14:49
@Desc   ：
=================================================='''
from urllib import parse

import requests

from myJDBC.jdbc import mySqlJdbc
from util.httpTool import MyHttpToolUtil
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

httpTool = MyHttpToolUtil()
tool = MyToolUtil
ioTool = MyIoToolUtil
jdbc = mySqlJdbc()

dataBD = ""


def insSj(href, sjlist):
    set_sj = set(sjlist)
    for sj in set_sj:
        sj_gs = jdbc.getSjGs(sj=sj, dataBD=dataBD)
        if sj_gs < 1:
            jdbc.inHnSJ(url=href, sj=sj, dataBD=dataBD)


def getXQ(url_list):
    urlSet = set(url_list)
    for url in urlSet:
        href = "https:" + url
        hrefGs = jdbc.getUrlGs(url=href, dataBD=dataBD)
        if hrefGs < 1:
            text_html = httpTool.getHtml_one_none(url=href)
            sj_list = tool.getSjAllList(text_html)
            print(sj_list)
            insSj(href, sj_list)


def getLB(kwd):
    url = "https://s.hc360.com/seller/search.html?kwd={}&pnum={}"
    for ym in range(1, 101):
        print(url.format(kwd, ym))
        html_sele = httpTool.getSele_one_none(url=url.format(kwd, ym))
        xpath_gs_url = "//dd[@class='newCname']/p/a/@href"
        gs_url_list = html_sele.xpath(xpath_gs_url)
        if gs_url_list:
            print(gs_url_list)
            getXQ(gs_url_list)
        else:
            break


gjz_list = [
    "花木", "珠宝", "玉石", "机械", "饰品",
    "黄金", "手镯", "首饰", "装饰",
    "项链", "银饰", "家居", "工艺品",
    "树脂", "景观", "陶瓷", "摆件", "礼品",
    "创意", "头饰", "钻石", "蜜蜡", "腰饰",
    "戒指", "耳环", "手链", "吊坠", "纯银",
    "机床", "设备", "仪表", "五金", "钢铁", "冶金", "家电",
    "安防", "照明", "电子", "橡塑",
    "能源", "宠物", "园艺", "数码",
    "通信", "家纺", "男装", "女装",
    "箱包", "鞋", "实业", "智能", "工业",

    "科技", "婚戒", "生活", "股东",
    "果蔬", "酒类", "酒", "罐头",
    "茶叶", "绿茶", "龙井", "碧螺春",
    "黄山毛峰", "庐山云雾",

    "红茶", "茶园", "耳线", "耳坠", "脚链", "耳钉",
    "本命年", "婚庆", "生日", "明牌", "名牌", "奢侈品", "耳夹", "手机链",
    "挂饰", "挂件", "金镶玉", "贵妃",
    "金银", "铂金", "翡翠", "珍珠", "彩宝", "和田玉",
    "人造宝石", "宝石", "玉石", "缅甸", "原石", "毛料", "貔貅", "冰种",
    "帝王", "平安扣", "帝王绿", "珠子", "赌石", "观音吊坠", "玉戒指", "证书",
    "电子科技", "展览", "物业",
    "文化", "软件", "种业", "秸秆", "动物",
    "策划", "网络科技", "生物工程", "美容",
    "医学", "摄影", "网络", "日用品", "医疗",
    "木材", "水站", "家政", "时尚",
    "化妆品", "制药", "信息科技", "量贩",
    "烟酒", "桶装水", "评估", "书店",
    "车辆", "中学", "配件", "认证", "机床", "中药",
    "锦鲤", "孕安", "进出口", "会展",
    "酒", "广告", "娱乐", "起重",
    "药业", "医药", "兽药", "未来科技",
    "电缆", "光学", "光电", "航天", "线缆", "泵",
    "水处理", "电气", "制刷", "生物",
    "环保", "传感器", "净化工程",
    "橡塑", "环境", "仪表", "机电",
    "阀门", "臭氧", "辐射", "照明", "高分子", "注塑", "桑拿",
    "电源", "纺织", "量子", "健身", "建材",
    "船舶", "游乐", "体育", "消防",
    "家具", "钻孔", "漆油", "塑胶",
    "陶瓷", "减震器", "木业", "工艺品", "木檀",
    "公路", "半导体", "热熔胶",
    "保温杯", "节能", "平面设计", "家居",
    "温室", "设计", "木雕", "声学",
    "文化传播", "棚业", "新媒体", "安防", "旅游", "模型",
    "石矿", "汽车", "矿", "化工", "清洁",
    "垂钓", "项链", "手链", "手镯",
    "项坠", "耳钉", "戒指", "水晶",
    "古建", "雕刻", "饰品", "珠宝", "首饰", "玩具",
    "钓鱼", "渔具", "铝业", "吊顶", "充电宝",
    "复合材料", "游泳", "润滑油",
    "机油", "切削液", "车窗膜",
    "车膜", "腻子粉", "涂料", "油漆",
    "砂浆", "焊机", "门窗",

    "建筑材料", "装饰", "女装",
    "男装", "服饰", "教育", "管件",
    "管材", "密封", "墙衣", "砖瓦",
    "香水", "电影", "日用百货",
    "袜业", "母婴", "纸尿裤",
    "云终端", "防爆", "石材",
    "浮雕", "壁画", "景观",
    "灯饰", "石业",
    "工艺制品", "五金",
    "佛像", "法器", "花卉",
    "相框", "硼砂", "通风",
    "电池", "化学",
    "石油", "手袋", "钎具",
    "车", "纳米", "沥青",
    "聚合", "钢管", "混凝土",

    "CPU", "伺服", "电机",
    "双吸泵", "裤", "剃须刀",
    "木屋", "工程", "厕所",

    "瓷", "水管", "衣柜",
    "柜", "钢结构", "GPS",
    "地板", "栏杆", "施工",
    "铁路", "结构胶", "修补",

    "条码", "打印机",
    "扫码", "石笼", "喷码",
    "合金", "药典", "洗头",
    "按摩", "美甲", "资料柜",
    "汗蒸", "牛皮纸",

    "包装纸", "纸业",
    "石墨", "脚垫", "口罩",
    "城堡", "气模", "井盖",
    "孵化", "承板",

    "触摸屏", "显微镜", "钢琴",
    "钢板", "螺杆", "扣件",
    "钢筋", "套筒", "岩棉",
    "钻", "数控", "墙体",

    "胶泥", "凡士林", "宝石",
    "陶粒", "托盘", "声波",
    "尿素", "打捆", "美缝剂",
    "河砂", "海砂", "彩砂",
    "压机", "路障", "童装",
    "电子商务", "球场", "防护",

    "绝缘", "仪式", "链条",
    "清障", "岗亭", "治安",
    "牛仔裤", "T恤", "卫衣",
    "凉鞋", "鞋", "布鞋",
    "隔音", "吸声", "T桖",
    "裙子", "背心", "庆典",
    "金蛋", "白坯", "服装",
    "热缩", "选矿", "破碎",
    "钢模", "纤维板", "面料", "篮球架",
    "滑梯", "水泥", "导航", "镭雕",
    "耳机", "线材", "公交",
    "磁", "手套", "塑料"
    , "荧光", "烤漆", "青石",
    "升旗", "搬家", "螺母",
    "螺栓", "螺钉", "紧固件",
    "疏通", "管道", "雨伞",
    "物流", "运输", "屏风",
    "尼龙", "泳池",

    "防水", "卫浴", "热力",
    "窗", "网带", "煤矿",
    "电路", "渗透",
    "风批", "粘合剂", "激光",
    "试剂", "试验", "检测",
    "假发", "假", "文胸"
    , "塔钟", "秤", "海绵",
    "干燥剂", "阻尼", "缓冲",
    "闸", "物联", "三辊",
    "轴承", "复印", "衬衫",
    "冲锋", "加油站", "扫帚",
    "拖把", "绘本", "标签", "地磅", "礼品",
    "切割", "珍珠", "房产",
    "钮扣", "燃料", "制衣",
    "焊接", "焊锡", "焊条",
    "益智", "婴幼", "宠物",
    "冲压", "墙壁", "节油",
    "培训", "咨询", "离心",

    "车间", "动力", "净化",
    "废水", "皮带", "重工",
    "UV", "纸盒", "大气",
    "静电", "滤芯"
    , "污水", "遮阳", "环卫",
    "吸污车", "垃圾车", "清洗车",
    "科技", "护栏", "控制",
    "电容", "钢化", "粪池",
    "帐篷", "篷布", "升降", "扑克"
    , "卡片", "印刷", "丝印",
    "刮刮卡", "刮刮", "胶",
    "屏幕", "推土", "挖掘",
    "保温", "麦拉", "隔电",
    "泡棉", "贴纸", "洒水车", "岗", "牛仔",
    "毛衣", "木方", "方木",
    "年装", "日用", "风幕",
    "交通", "荷花", "商务",
    "商行", "阿迪", "耐克",
    "头盔", "桥架", "抗震",
    "房屋", "毛绒"
          "雕塑", "搅拌机",
    "饲料", "调节剂", "树脂",
    "百货", "培养箱", "液氮罐",
    "天平", "绒布", "网布",
    "棉布", "布", "水磨",
    "地坪", "抛光", "石英粉",
    "纤维", "换热", "岩",
    "材料", "线板", "新型材料",
    "加盟", "手机", "保护",
    "方管", "异型管", "砂机",
    "涤洗", "洗涤", "洗衣", "钥匙",
    "配饰", "装修", "瓷砖",
    "盐酸", "纸箱", "纸盒",
    "卡包", "卡套", "风机",
    "软管", "风管", "法兰",
    "复合", "净化", "保温", "防火", "节能"
    , "变频", "汗蒸", "汗蒸",
    "钢丝", "化妆", "教学",
    "电解", "鱼缸", "水族箱",
    "景观", "施工", "分析",
    "探测", "救生", "珍宝", "特种"
    , "金属加工", "花舍", "红木",
    "狗粮", "猫粮", "石板",
    "办公", "展厅", "绿植", "花草",
]

if __name__ == '__main__':
    for gjz in gjz_list:
        kwd = parse.quote(gjz)
        getLB(kwd)
        exit()
