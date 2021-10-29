#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> demo
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-17 10:45
@Desc   ：
=================================================='''
from lxml import etree
from myJDBC.jdbc import mySqlJdbc
import requests

jdbc = mySqlJdbc()


cccall = """
北京
上海
天津
重庆
香港
澳门
石家庄
沧州
承德
秦皇岛
唐山
保定
廊坊
邢台
衡水
张家口
邯郸
任丘
河间
泊头
武安
沙河
南宫
深州
冀州
黄骅
高碑店
安国
涿州
定州
三河
霸州
迁安
遵化
鹿泉
新乐
晋州
藁城
辛集
太原
长治
大同
阳泉
朔州
临汾
晋城
忻州
运城
晋中
吕梁
古交
潞城
高平
原平
孝义
汾阳
介休
侯马
霍州
永济
河津
陵川
沈阳
大连
本溪
阜新
葫芦岛
盘锦
铁岭
丹东
锦州
营口
鞍山
辽阳
抚顺
朝阳
瓦房店
兴城
新民
普兰店
庄河
北票
凌源
调兵山
开原
灯塔
海城
凤城
东港
大石桥
盖州
凌海
北镇
长春
白城
白山
吉林
辽源
四平
通化
松原
延边(延吉)
珲春
龙井
舒兰
临江
公主岭
梅河口
德惠
九台
榆树
磐石
蛟河
桦甸
洮南
大安
双辽
集安
图们
敦化
和龙
哈尔滨
大庆
大兴安岭
鹤岗
黑河
鸡西
佳木斯
牡丹江
七台河
双鸭山
齐齐哈尔
伊春
绥化
虎林
五常
密山
宁安
漠河
海伦
肇东
安达
海林
绥芬河
富锦
同江
铁力
五大连池
北安
讷河
阿城
尚志
双城
南京
苏州
扬州
无锡
南通
常州
连云港
徐州
镇江
淮安
宿迁
泰州
太仓
盐城
高邮
新沂
金坛
溧阳
淮阴
江宁
睢宁
清江
昆山
常熟
江阴
宜兴
邳州
张家港
吴江
如皋
海门
启东
大丰
东台
仪征
扬中
句容
丹阳
兴化
姜堰
泰兴
靖江
杭州
宁波
温州
丽水
奉化
宁海
临海
三门
绍兴
舟山
义乌
北仑
慈溪
象山
余姚
天台
温岭
仙居
台州
嘉兴
湖州
衢州
金华
余杭
德清
海宁
临安
富阳
建德
平湖
桐乡
诸暨
上虞
嵊州
江山
兰溪
永康
东阳
瑞安
乐清
龙泉
合肥
黄山
芜湖
铜陵
安庆
滁州
宣城
阜阳
淮北
蚌埠
池州
青阳
九华山景区
黄山景区
巢湖
亳州
马鞍山
宿州
六安
淮南
绩溪
界首
明光
天长
桐城
宁国
福州
厦门
泉州
漳州
龙岩
三明
南平
永安
宁德
莆田
闽侯
福鼎
罗源
仙游
福清
长乐
云霄
长泰
东山岛
邵武
石狮
晋江
建阳
福安
漳平
龙海
南安
建瓯
武夷山
南昌
九江
赣州
景德镇
萍乡
新余
吉安
宜春
抚州
上饶
鹰潭
瑞金
井冈山
瑞昌
乐平
南康
德兴
丰城
樟树
高安
贵溪
济南
青岛
烟台
威海
潍坊
德州
滨州
东营
聊城
菏泽
济宁
临沂
淄博
泰安
枣庄
日照
莱芜
海阳
平度
莱阳
青州
肥城
章丘
即墨
利津
武城
桓台
沂源
曲阜
龙口
胶州
胶南
莱西
临清
乐陵
禹城
安丘
昌邑
高密
诸城
寿光
栖霞
莱州
蓬莱
招远
文登
荣成
乳山
滕州
兖州
邹城
新泰
郑州
安阳
济源
鹤壁
焦作
开封
濮阳
三门峡
驻马店
商丘
新乡
信阳
许昌
周口
南阳
洛阳
平顶山
漯河
中牟
洛宁
荥阳
登封
项城
灵宝
义马
舞钢
长葛
禹州
林州
辉县
卫辉
沁阳
孟州
偃师
新密
登封
新郑
汝州
永城
邓州
巩义
武汉
十堰
宜昌
鄂州
黄石
襄樊
荆州
荆门
孝感
黄冈
咸宁
随州
恩施
仙桃
天门
潜江
神农架
沙市
老河口
利川
当阳
枝江
宜都
松滋
洪湖
石首
赤壁
大冶
麻城
武穴
广水
安陆
应城
汉川
钟祥
宜城
枣阳
丹江口
长沙
张家界
株洲
韶山
衡阳
郴州
冷水江
娄底
耒阳
永州
湘乡
湘潭
常德
益阳
怀化
邵阳
岳阳
吉首
大庸
韶山
常宁
浏阳
津市
沅江
汨罗
临湘
醴陵
资兴
武冈
洪江
广州
深圳
珠海
东莞
佛山
潮州
汕头
湛江
中山
惠州
河源
揭阳
梅州
肇庆
茂名
云浮
阳江
江门
韶关
乐昌
化州
从化
鹤山
汕尾
清远
顺德
雷州
廉江
吴川
高州
信宜
阳春
罗定
四会
高要
开平
台山
恩平
陆丰
普宁
兴宁
南雄
连州
英德
增城
南宁
柳州
北海
百色
梧州
贺州
玉林
河池
桂林
钦州
防城港
来宾
崇左
贵港
北流
宜州
桂平
岑溪
东兴
凭祥
合山
海口
三亚
琼海
儋州
文昌
万宁
东方
五指山
成都
内江
峨眉山
绵阳
宜宾
泸州
攀枝花
自贡
资阳
崇州
西昌
都江堰
遂宁
乐山
达州
江油
大邑
金堂
德阳
南充
广安
广元
巴中
雅安
眉山
阿坝(马尔康)
甘孜(康定)
三台
丹棱
梁平
万县
广汉
汶川县
什邡
彭州
绵竹
邛崃
阆中
华蓥
万源
简阳
贵阳
安顺
铜仁
六盘水
遵义
毕节
兴义
凯里
都匀
福泉
仁怀
赤水
清镇
昆明
西双版纳
大理
德宏(芒市)
思茅
玉溪
曲靖
保山
昭通
临沧
丽江
文山
个旧
楚雄
迪庆(香格里拉)
宜良
沅江
安宁
宣威
瑞丽
开远
景洪
拉萨
那曲
昌都
山南
日喀则
阿里(噶尔)
林芝
西安
宝鸡
延安
兴平
咸阳
铜川
渭南
汉中
榆林
安康
商洛
周至
韩城
华阴
兰州
嘉峪关
酒泉
临夏
白银
天水
武威
张掖
平凉
庆阳
定西
陇南(成县)
甘南(合作)
敦煌
金昌
玉门
西宁
海东(平安)
海北(海晏)
黄南(同仁)
海南(共和)
果洛(玛沁)
海西(德令哈)
玉树
格尔木
呼和浩特
呼伦贝尔(海拉尔)
包头
赤峰
鄂尔多斯
巴彦淖尔盟(临河)
阿拉善盟(阿拉善左旗)
兴安盟(乌兰浩特)
通辽
乌海
乌兰察布盟(集宁)
锡林郭勒盟(锡林浩特)
满洲里
扎兰屯
牙克石
根河
额尔古纳
阿尔山
霍林郭勒
二连浩特
丰镇
银川
石嘴山
吴忠
固原
中卫
灵武
青铜峡
乌鲁木齐
克拉玛依
哈密
喀什
吐鲁番
石河子
图木舒克
和田
昌吉
阿图什
库尔勒
博乐
伊宁
阿拉尔
阿克苏
五家渠
北屯
阜康
米泉
奎屯
塔城
乌苏
阿勒泰
台北
台中
台南
高雄
基隆
新竹
嘉义
宜兰
桃园
彰化
苗栗
云林
屏东
彭湖
花莲
"""

csNameAll = ['北京', '上海', '天津', '重庆', '香港', '澳门', '石家庄', '沧州', '承德', '秦皇岛', '唐山', '保定', '廊坊', '邢台', '衡水', '张家口', '邯郸',
             '任丘', '河间', '泊头', '武安', '沙河', '南宫', '深州', '冀州', '黄骅', '高碑店', '安国', '涿州', '定州', '三河', '霸州', '迁安', '遵化',
             '鹿泉', '新乐', '晋州', '藁城', '辛集', '太原', '长治', '大同', '阳泉', '朔州', '临汾', '晋城', '忻州', '运城', '晋中', '吕梁', '古交', '潞城',
             '高平', '原平', '孝义', '汾阳', '介休', '侯马', '霍州', '永济', '河津', '陵川', '沈阳', '大连', '本溪', '阜新', '葫芦岛', '盘锦', '铁岭',
             '丹东', '锦州', '营口', '鞍山', '辽阳', '抚顺', '朝阳', '瓦房店', '兴城', '新民', '普兰店', '庄河', '北票', '凌源', '调兵山', '开原', '灯塔',
             '海城', '凤城', '东港', '大石桥', '盖州', '凌海', '北镇', '长春', '白城', '白山', '吉林', '辽源', '四平', '通化', '松原', '延边(延吉)', '珲春',
             '龙井', '舒兰', '临江', '公主岭', '梅河口', '德惠', '九台', '榆树', '磐石', '蛟河', '桦甸', '洮南', '大安', '双辽', '集安', '图们', '敦化',
             '和龙', '哈尔滨', '大庆', '大兴安岭', '鹤岗', '黑河', '鸡西', '佳木斯', '牡丹江', '七台河', '双鸭山', '齐齐哈尔', '伊春', '绥化', '虎林', '五常',
             '密山', '宁安', '漠河', '海伦', '肇东', '安达', '海林', '绥芬河', '富锦', '同江', '铁力', '五大连池', '北安', '讷河', '阿城', '尚志', '双城',
             '南京', '苏州', '扬州', '无锡', '南通', '常州', '连云港', '徐州', '镇江', '淮安', '宿迁', '泰州', '太仓', '盐城', '高邮', '新沂', '金坛',
             '溧阳', '淮阴', '江宁', '睢宁', '清江', '昆山', '常熟', '江阴', '宜兴', '邳州', '张家港', '吴江', '如皋', '海门', '启东', '大丰', '东台',
             '仪征', '扬中', '句容', '丹阳', '兴化', '姜堰', '泰兴', '靖江', '杭州', '宁波', '温州', '丽水', '奉化', '宁海', '临海', '三门', '绍兴', '舟山',
             '义乌', '北仑', '慈溪', '象山', '余姚', '天台', '温岭', '仙居', '台州', '嘉兴', '湖州', '衢州', '金华', '余杭', '德清', '海宁', '临安', '富阳',
             '建德', '平湖', '桐乡', '诸暨', '上虞', '嵊州', '江山', '兰溪', '永康', '东阳', '瑞安', '乐清', '龙泉', '合肥', '黄山', '芜湖', '铜陵', '安庆',
             '滁州', '宣城', '阜阳', '淮北', '蚌埠', '池州', '青阳', '九华山景区', '黄山景区', '巢湖', '亳州', '马鞍山', '宿州', '六安', '淮南', '绩溪', '界首',
             '明光', '天长', '桐城', '宁国', '福州', '厦门', '泉州', '漳州', '龙岩', '三明', '南平', '永安', '宁德', '莆田', '闽侯', '福鼎', '罗源', '仙游',
             '福清', '长乐', '云霄', '长泰', '东山岛', '邵武', '石狮', '晋江', '建阳', '福安', '漳平', '龙海', '南安', '建瓯', '武夷山', '南昌', '九江',
             '赣州', '景德镇', '萍乡', '新余', '吉安', '宜春', '抚州', '上饶', '鹰潭', '瑞金', '井冈山', '瑞昌', '乐平', '南康', '德兴', '丰城', '樟树',
             '高安', '贵溪', '济南', '青岛', '烟台', '威海', '潍坊', '德州', '滨州', '东营', '聊城', '菏泽', '济宁', '临沂', '淄博', '泰安', '枣庄', '日照',
             '莱芜', '海阳', '平度', '莱阳', '青州', '肥城', '章丘', '即墨', '利津', '武城', '桓台', '沂源', '曲阜', '龙口', '胶州', '胶南', '莱西', '临清',
             '乐陵', '禹城', '安丘', '昌邑', '高密', '诸城', '寿光', '栖霞', '莱州', '蓬莱', '招远', '文登', '荣成', '乳山', '滕州', '兖州', '邹城', '新泰',
             '郑州', '安阳', '济源', '鹤壁', '焦作', '开封', '濮阳', '三门峡', '驻马店', '商丘', '新乡', '信阳', '许昌', '周口', '南阳', '洛阳', '平顶山',
             '漯河', '中牟', '洛宁', '荥阳', '登封', '项城', '灵宝', '义马', '舞钢', '长葛', '禹州', '林州', '辉县', '卫辉', '沁阳', '孟州', '偃师', '新密',
             '登封', '新郑', '汝州', '永城', '邓州', '巩义', '武汉', '十堰', '宜昌', '鄂州', '黄石', '襄樊', '荆州', '荆门', '孝感', '黄冈', '咸宁', '随州',
             '恩施', '仙桃', '天门', '潜江', '神农架', '沙市', '老河口', '利川', '当阳', '枝江', '宜都', '松滋', '洪湖', '石首', '赤壁', '大冶', '麻城',
             '武穴', '广水', '安陆', '应城', '汉川', '钟祥', '宜城', '枣阳', '丹江口', '长沙', '张家界', '株洲', '韶山', '衡阳', '郴州', '冷水江', '娄底',
             '耒阳', '永州', '湘乡', '湘潭', '常德', '益阳', '怀化', '邵阳', '岳阳', '吉首', '大庸', '韶山', '常宁', '浏阳', '津市', '沅江', '汨罗', '临湘',
             '醴陵', '资兴', '武冈', '洪江', '广州', '深圳', '珠海', '东莞', '佛山', '潮州', '汕头', '湛江', '中山', '惠州', '河源', '揭阳', '梅州', '肇庆',
             '茂名', '云浮', '阳江', '江门', '韶关', '乐昌', '化州', '从化', '鹤山', '汕尾', '清远', '顺德', '雷州', '廉江', '吴川', '高州', '信宜', '阳春',
             '罗定', '四会', '高要', '开平', '台山', '恩平', '陆丰', '普宁', '兴宁', '南雄', '连州', '英德', '增城', '南宁', '柳州', '北海', '百色', '梧州',
             '贺州', '玉林', '河池', '桂林', '钦州', '防城港', '来宾', '崇左', '贵港', '北流', '宜州', '桂平', '岑溪', '东兴', '凭祥', '合山', '海口',
             '三亚', '琼海', '儋州', '文昌', '万宁', '东方', '五指山', '成都', '内江', '峨眉山', '绵阳', '宜宾', '泸州', '攀枝花', '自贡', '资阳', '崇州',
             '西昌', '都江堰', '遂宁', '乐山', '达州', '江油', '大邑', '金堂', '德阳', '南充', '广安', '广元', '巴中', '雅安', '眉山', '阿坝(马尔康)',
             '甘孜(康定)', '三台', '丹棱', '梁平', '万县', '广汉', '汶川县', '什邡', '彭州', '绵竹', '邛崃', '阆中', '华蓥', '万源', '简阳', '贵阳', '安顺',
             '铜仁', '六盘水', '遵义', '毕节', '兴义', '凯里', '都匀', '福泉', '仁怀', '赤水', '清镇', '昆明', '西双版纳', '大理', '德宏(芒市)', '思茅',
             '玉溪', '曲靖', '保山', '昭通', '临沧', '丽江', '文山', '个旧', '楚雄', '迪庆(香格里拉)', '宜良', '沅江', '安宁', '宣威', '瑞丽', '开远', '景洪',
             '拉萨', '那曲', '昌都', '山南', '日喀则', '阿里(噶尔)', '林芝', '西安', '宝鸡', '延安', '兴平', '咸阳', '铜川', '渭南', '汉中', '榆林', '安康',
             '商洛', '周至', '韩城', '华阴', '兰州', '嘉峪关', '酒泉', '临夏', '白银', '天水', '武威', '张掖', '平凉', '庆阳', '定西', '陇南(成县)',
             '甘南(合作)', '敦煌', '金昌', '玉门', '西宁', '海东(平安)', '海北(海晏)', '黄南(同仁)', '海南(共和)', '果洛(玛沁)', '海西(德令哈)', '玉树', '格尔木',
             '呼和浩特', '呼伦贝尔(海拉尔)', '包头', '赤峰', '鄂尔多斯', '巴彦淖尔盟(临河)', '阿拉善盟(阿拉善左旗)', '兴安盟(乌兰浩特)', '通辽', '乌海', '乌兰察布盟(集宁)',
             '锡林郭勒盟(锡林浩特)', '满洲里', '扎兰屯', '牙克石', '根河', '额尔古纳', '阿尔山', '霍林郭勒', '二连浩特', '丰镇', '银川', '石嘴山', '吴忠', '固原',
             '中卫', '灵武', '青铜峡', '乌鲁木齐', '克拉玛依', '哈密', '喀什', '吐鲁番', '石河子', '图木舒克', '和田', '昌吉', '阿图什', '库尔勒', '博乐', '伊宁',
             '阿拉尔', '阿克苏', '五家渠', '北屯', '阜康', '米泉', '奎屯', '塔城', '乌苏', '阿勒泰', '台北', '台中', '台南', '高雄', '基隆', '新竹', '嘉义',
             '宜兰', '桃园', '彰化', '苗栗', '云林', '屏东', '彭湖', '花莲']



# text_req = requests.get(url="https://poi.mapbar.com/").text

# selector = etree.HTML(text_req)

# name_list = selector.xpath("//dl[@id='city_list']/dd/a/text()")
# href_list = selector.xpath("//dl[@id='city_list']/dd/a/@href")

# print(len(name_list))
# print(name_list)
# print(len(href_list))
# print(href_list)

name___ = ['阿拉善盟', '安阳市', '鞍山市', '阿坝藏族羌族自治州', '安顺市', '阿里地区', '阿勒泰地区', '阿克苏地区', '阿拉尔市', '安康市', '安庆市', '北京市', '保定市',
           '包头市', '巴彦淖尔市', '白城市', '白山市', '本溪市', '巴中市', '保山市', '毕节市', '巴音郭楞蒙古自治州', '博尔塔拉蒙古自治州', '北屯市', '宝鸡市', '白银市',
           '百色市', '北海市', '白沙黎族自治县', '保亭黎族苗族自治县', '滨州市', '蚌埠市', '亳州市', '承德市', '沧州市', '长治市', '赤峰市', '长沙市', '常德市', '郴州市',
           '长春市', '朝阳市', '成都市', '楚雄彝族自治州', '重庆市', '昌都市', '昌吉回族自治州', '潮州市', '崇左市', '昌江黎族自治县', '澄迈县', '常州市', '池州市', '滁州市',
           '大同市', '大庆市', '大兴安岭地区', '丹东市', '大连市', '德阳市', '达州市', '德宏傣族景颇族自治州', '迪庆藏族自治州', '大理白族自治州', '定西市', '东莞市', '儋州市',
           '东方市', '定安县', '德州市', '东营市', '鄂尔多斯市', '鄂州市', '恩施土家族苗族自治州', '阜新市', '抚顺市', '佛山市', '防城港市', '福州市', '抚州市', '阜阳市',
           '广元市', '广安市', '甘孜藏族自治州', '贵阳市', '甘南藏族自治州', '固原市', '果洛藏族自治州', '广州市', '桂林市', '贵港市', '赣州市', '衡水市', '邯郸市',
           '呼和浩特市', '呼伦贝尔市', '鹤壁市', '衡阳市', '怀化市', '黄石市', '黄冈市', '哈尔滨市', '黑河市', '鹤岗市', '葫芦岛市', '红河哈尼族彝族自治州', '哈密市',
           '和田地区', '汉中市', '海北藏族自治州', '海东市', '海南藏族自治州', '海西蒙古族藏族自治州', '黄南藏族自治州', '香港特别行政区', '河源市', '惠州市', '河池市', '贺州市',
           '海口市', '淮安市', '杭州市', '湖州市', '菏泽市', '合肥市', '黄山市', '淮北市', '淮南市', '晋城市', '晋中市', '焦作市', '济源市', '荆门市', '荆州市',
           '佳木斯市', '鸡西市', '吉林市', '锦州市', '酒泉市', '嘉峪关市', '金昌市', '揭阳市', '江门市', '嘉兴市', '金华市', '济南市', '济宁市', '九江市', '景德镇市',
           '吉安市', '开封市', '昆明市', '克拉玛依市', '克孜勒苏柯尔克孜自治州', '喀什地区', '可克达拉市', '昆玉市', '廊坊市', '临汾市', '吕梁市', '洛阳市', '漯河市',
           '娄底市', '辽源市', '辽阳市', '乐山市', '泸州市', '凉山彝族自治州', '丽江市', '临沧市', '六盘水市', '拉萨市', '林芝市', '兰州市', '临夏回族自治州', '陇南市',
           '柳州市', '来宾市', '乐东黎族自治县', '临高县', '陵水黎族自治县', '连云港市', '丽水市', '龙岩市', '聊城市', '临沂市', '六安市', '牡丹江市', '绵阳市', '眉山市',
           '澳门特别行政区', '梅州市', '茂名市', '马鞍山市', '南阳市', '南充市', '内江市', '怒江傈僳族自治州', '那曲市', '南宁市', '南京市', '南通市', '宁波市', '南平市',
           '宁德市', '南昌市', '濮阳市', '平顶山市', '盘锦市', '攀枝花市', '普洱市', '平凉市', '莆田市', '萍乡市', '秦皇岛市', '潜江市', '齐齐哈尔市', '七台河市',
           '曲靖市', '黔东南苗族侗族自治州', '黔南布依族苗族自治州', '黔西南布依族苗族自治州', '庆阳市', '清远市', '钦州市', '琼海市', '琼中黎族苗族自治县', '衢州市', '泉州市',
           '青岛市', '日喀则市', '日照市', '石家庄市', '朔州市', '三门峡市', '商丘市', '邵阳市', '十堰市', '随州市', '神农架林区', '双鸭山市', '绥化市', '松原市',
           '四平市', '沈阳市', '遂宁市', '山南市', '石河子市', '双河市', '商洛市', '石嘴山市', '韶关市', '汕头市', '汕尾市', '深圳市', '三亚市', '三沙市', '上海市',
           '苏州市', '宿迁市', '绍兴市', '三明市', '上饶市', '宿州市', '天津市', '唐山市', '太原市', '通辽市', '天门市', '通化市', '铁岭市', '铜仁市', '吐鲁番市',
           '塔城地区', '图木舒克市', '铁门关市', '铜川市', '天水市', '屯昌县', '泰州市', '台州市', '泰安市', '铜陵市', '乌海市', '乌兰察布市', '武汉市', '文山壮族苗族自治州',
           '乌鲁木齐市', '五家渠市', '渭南市', '武威市', '吴忠市', '梧州市', '万宁市', '文昌市', '五指山市', '无锡市', '温州市', '威海市', '潍坊市', '芜湖市', '邢台市',
           '忻州市', '兴安盟', '锡林郭勒盟', '新乡市', '许昌市', '信阳市', '湘潭市', '湘西土家族苗族自治州', '襄阳市', '孝感市', '咸宁市', '仙桃市', '西双版纳傣族自治州',
           '西安市', '咸阳市', '西宁市', '徐州市', '厦门市', '新余市', '宣城市', '阳泉市', '运城市', '益阳市', '岳阳市', '永州市', '宜昌市', '伊春市', '延边朝鲜族自治州',
           '营口市', '宜宾市', '雅安市', '玉溪市', '伊犁哈萨克自治州', '延安市', '榆林市', '银川市', '玉树藏族自治州', '云浮市', '阳江市', '玉林市', '盐城市', '扬州市',
           '烟台市', '鹰潭市', '宜春市', '张家口市', '郑州市', '周口市', '驻马店市', '张家界市', '株洲市', '自贡市', '资阳市', '昭通市', '遵义市', '张掖市', '中卫市',
           '珠海市', '中山市', '肇庆市', '湛江市', '镇江市', '舟山市', '漳州市', '淄博市', '枣庄市']
url___ = ['http://poi.mapbar.com/alashanmeng/', 'http://poi.mapbar.com/anyang/', 'http://poi.mapbar.com/anshan/',
          'http://poi.mapbar.com/aba/', 'http://poi.mapbar.com/anshun/', 'http://poi.mapbar.com/ali/',
          'http://poi.mapbar.com/aletai/', 'http://poi.mapbar.com/akesu/', 'http://poi.mapbar.com/alaer/',
          'http://poi.mapbar.com/ankang/', 'http://poi.mapbar.com/anqing/', 'http://poi.mapbar.com/beijing/',
          'http://poi.mapbar.com/baoding/', 'http://poi.mapbar.com/baotou/', 'http://poi.mapbar.com/bayannaoer/',
          'http://poi.mapbar.com/baicheng/', 'http://poi.mapbar.com/baishan/', 'http://poi.mapbar.com/benxi/',
          'http://poi.mapbar.com/bazhong/', 'http://poi.mapbar.com/baoshan/', 'http://poi.mapbar.com/bijie/',
          'http://poi.mapbar.com/bayinguole/', 'http://poi.mapbar.com/boertala/', 'http://poi.mapbar.com/beitun/',
          'http://poi.mapbar.com/baoji/', 'http://poi.mapbar.com/baiyin/', 'http://poi.mapbar.com/baise/',
          'http://poi.mapbar.com/beihai/', 'http://poi.mapbar.com/baisha/', 'http://poi.mapbar.com/baoting/',
          'http://poi.mapbar.com/binzhou/', 'http://poi.mapbar.com/bengbu/', 'http://poi.mapbar.com/bozhou/',
          'http://poi.mapbar.com/chengde/', 'http://poi.mapbar.com/cangzhou/', 'http://poi.mapbar.com/changzhi/',
          'http://poi.mapbar.com/chifeng/', 'http://poi.mapbar.com/changsha/', 'http://poi.mapbar.com/changde/',
          'http://poi.mapbar.com/chenzhou/', 'http://poi.mapbar.com/changchun/', 'http://poi.mapbar.com/chaoyang/',
          'http://poi.mapbar.com/chengdu/', 'http://poi.mapbar.com/chuxiong/', 'http://poi.mapbar.com/chongqing/',
          'http://poi.mapbar.com/changdu/', 'http://poi.mapbar.com/changji/', 'http://poi.mapbar.com/chaozhou/',
          'http://poi.mapbar.com/chongzuo/', 'http://poi.mapbar.com/changjiang/', 'http://poi.mapbar.com/chengmai/',
          'http://poi.mapbar.com/changzhou/', 'http://poi.mapbar.com/chizhou/', 'http://poi.mapbar.com/chuzhou/',
          'http://poi.mapbar.com/datong/', 'http://poi.mapbar.com/daqing/', 'http://poi.mapbar.com/daxinganling/',
          'http://poi.mapbar.com/dandong/', 'http://poi.mapbar.com/dalian/', 'http://poi.mapbar.com/deyang/',
          'http://poi.mapbar.com/dazhou/', 'http://poi.mapbar.com/dehong/', 'http://poi.mapbar.com/diqing/',
          'http://poi.mapbar.com/dali/', 'http://poi.mapbar.com/dingxi/', 'http://poi.mapbar.com/dongguan/',
          'http://poi.mapbar.com/danzhou/', 'http://poi.mapbar.com/dongfang/', 'http://poi.mapbar.com/dingan/',
          'http://poi.mapbar.com/dezhou/', 'http://poi.mapbar.com/dongying/', 'http://poi.mapbar.com/eerduosi/',
          'http://poi.mapbar.com/ezhou/', 'http://poi.mapbar.com/enshi/', 'http://poi.mapbar.com/fuxin/',
          'http://poi.mapbar.com/fushun/', 'http://poi.mapbar.com/foshan/', 'http://poi.mapbar.com/fangchenggang/',
          'http://poi.mapbar.com/fuzhou1/', 'http://poi.mapbar.com/fuzhou2/', 'http://poi.mapbar.com/fuyang/',
          'http://poi.mapbar.com/guangyuan/', 'http://poi.mapbar.com/guangan/', 'http://poi.mapbar.com/ganzi/',
          'http://poi.mapbar.com/guiyang/', 'http://poi.mapbar.com/gannan/', 'http://poi.mapbar.com/guyuan/',
          'http://poi.mapbar.com/guoluo/', 'http://poi.mapbar.com/guangzhou/', 'http://poi.mapbar.com/guilin/',
          'http://poi.mapbar.com/guigang/', 'http://poi.mapbar.com/ganzhou/', 'http://poi.mapbar.com/hengshui/',
          'http://poi.mapbar.com/handan/', 'http://poi.mapbar.com/huhehaote/', 'http://poi.mapbar.com/hulunbeier/',
          'http://poi.mapbar.com/hebi/', 'http://poi.mapbar.com/hengyang/', 'http://poi.mapbar.com/huaihua/',
          'http://poi.mapbar.com/huangshi/', 'http://poi.mapbar.com/huanggang/', 'http://poi.mapbar.com/haerbin/',
          'http://poi.mapbar.com/heihe/', 'http://poi.mapbar.com/hegang/', 'http://poi.mapbar.com/huludao/',
          'http://poi.mapbar.com/honghe/', 'http://poi.mapbar.com/hami/', 'http://poi.mapbar.com/hetian/',
          'http://poi.mapbar.com/hanzhong/', 'http://poi.mapbar.com/haibei/', 'http://poi.mapbar.com/haidong/',
          'http://poi.mapbar.com/hainan/', 'http://poi.mapbar.com/haixi/', 'http://poi.mapbar.com/huangnan/',
          'http://poi.mapbar.com/hongkong/', 'http://poi.mapbar.com/heyuan/', 'http://poi.mapbar.com/huizhou/',
          'http://poi.mapbar.com/hechi/', 'http://poi.mapbar.com/hezhou/', 'http://poi.mapbar.com/haikou/',
          'http://poi.mapbar.com/huaian/', 'http://poi.mapbar.com/hangzhou/', 'http://poi.mapbar.com/huzhou/',
          'http://poi.mapbar.com/heze/', 'http://poi.mapbar.com/hefei/', 'http://poi.mapbar.com/huangshan/',
          'http://poi.mapbar.com/huaibei/', 'http://poi.mapbar.com/huainan/', 'http://poi.mapbar.com/jincheng/',
          'http://poi.mapbar.com/jinzhong/', 'http://poi.mapbar.com/jiaozuo/', 'http://poi.mapbar.com/jiyuan/',
          'http://poi.mapbar.com/jingmen/', 'http://poi.mapbar.com/jingzhou/', 'http://poi.mapbar.com/jiamusi/',
          'http://poi.mapbar.com/jixi/', 'http://poi.mapbar.com/jilin/', 'http://poi.mapbar.com/jinzhou/',
          'http://poi.mapbar.com/jiuquan/', 'http://poi.mapbar.com/jiayuguan/', 'http://poi.mapbar.com/jinchang/',
          'http://poi.mapbar.com/jieyang/', 'http://poi.mapbar.com/jiangmen/', 'http://poi.mapbar.com/jiaxing/',
          'http://poi.mapbar.com/jinhua/', 'http://poi.mapbar.com/jinan/', 'http://poi.mapbar.com/jining/',
          'http://poi.mapbar.com/jiujiang/', 'http://poi.mapbar.com/jingdezhen/', 'http://poi.mapbar.com/jian/',
          'http://poi.mapbar.com/kaifeng/', 'http://poi.mapbar.com/kunming/', 'http://poi.mapbar.com/kelamayi/',
          'http://poi.mapbar.com/kezilesu/', 'http://poi.mapbar.com/kashen/', 'http://poi.mapbar.com/kekedala/',
          'http://poi.mapbar.com/kunyu/', 'http://poi.mapbar.com/langfang/', 'http://poi.mapbar.com/linfen/',
          'http://poi.mapbar.com/lvliang/', 'http://poi.mapbar.com/luoyang/', 'http://poi.mapbar.com/luohe/',
          'http://poi.mapbar.com/loudi/', 'http://poi.mapbar.com/liaoyuan/', 'http://poi.mapbar.com/liaoyang/',
          'http://poi.mapbar.com/leshan/', 'http://poi.mapbar.com/luzhou/', 'http://poi.mapbar.com/liangshan/',
          'http://poi.mapbar.com/lijiang/', 'http://poi.mapbar.com/lincang/', 'http://poi.mapbar.com/liupanshui/',
          'http://poi.mapbar.com/lasa/', 'http://poi.mapbar.com/linzhi/', 'http://poi.mapbar.com/lanzhou/',
          'http://poi.mapbar.com/linxia/', 'http://poi.mapbar.com/longnan/', 'http://poi.mapbar.com/liuzhou/',
          'http://poi.mapbar.com/laibin/', 'http://poi.mapbar.com/ledong/', 'http://poi.mapbar.com/lingao/',
          'http://poi.mapbar.com/lingshui/', 'http://poi.mapbar.com/lianyungang/', 'http://poi.mapbar.com/lishui/',
          'http://poi.mapbar.com/longyan/', 'http://poi.mapbar.com/liaocheng/', 'http://poi.mapbar.com/linyi/',
          'http://poi.mapbar.com/liuan/', 'http://poi.mapbar.com/mudanjiang/', 'http://poi.mapbar.com/mianyang/',
          'http://poi.mapbar.com/meishan/', 'http://poi.mapbar.com/macau/', 'http://poi.mapbar.com/meizhou/',
          'http://poi.mapbar.com/maoming/', 'http://poi.mapbar.com/maanshan/', 'http://poi.mapbar.com/nanyang/',
          'http://poi.mapbar.com/nanchong/', 'http://poi.mapbar.com/neijiang/', 'http://poi.mapbar.com/nujiang/',
          'http://poi.mapbar.com/naqu/', 'http://poi.mapbar.com/nanning/', 'http://poi.mapbar.com/nanjing/',
          'http://poi.mapbar.com/nantong/', 'http://poi.mapbar.com/ningbo/', 'http://poi.mapbar.com/nanping/',
          'http://poi.mapbar.com/ningde/', 'http://poi.mapbar.com/nanchang/', 'http://poi.mapbar.com/puyang/',
          'http://poi.mapbar.com/pingdingshan/', 'http://poi.mapbar.com/panjin/', 'http://poi.mapbar.com/panzhihua/',
          'http://poi.mapbar.com/puer/', 'http://poi.mapbar.com/pingliang/', 'http://poi.mapbar.com/putian/',
          'http://poi.mapbar.com/pingxiang/', 'http://poi.mapbar.com/qinhuangdao/', 'http://poi.mapbar.com/qianjiang/',
          'http://poi.mapbar.com/qiqihaer/', 'http://poi.mapbar.com/qitaihe/', 'http://poi.mapbar.com/qujing/',
          'http://poi.mapbar.com/qiandongnan/', 'http://poi.mapbar.com/qiannan/', 'http://poi.mapbar.com/qianxinan/',
          'http://poi.mapbar.com/qingyang/', 'http://poi.mapbar.com/qingyuan/', 'http://poi.mapbar.com/qinzhou/',
          'http://poi.mapbar.com/qionghai/', 'http://poi.mapbar.com/qiongzhong/', 'http://poi.mapbar.com/quzhou/',
          'http://poi.mapbar.com/quanzhou/', 'http://poi.mapbar.com/qingdao/', 'http://poi.mapbar.com/rikaze/',
          'http://poi.mapbar.com/rizhao/', 'http://poi.mapbar.com/shijiazhuang/', 'http://poi.mapbar.com/shuozhou/',
          'http://poi.mapbar.com/sanmenxia/', 'http://poi.mapbar.com/shangqiu/', 'http://poi.mapbar.com/shaoyang/',
          'http://poi.mapbar.com/shiyan/', 'http://poi.mapbar.com/suizhou/', 'http://poi.mapbar.com/shennongjia/',
          'http://poi.mapbar.com/shuangyashan/', 'http://poi.mapbar.com/suihua/', 'http://poi.mapbar.com/songyuan/',
          'http://poi.mapbar.com/siping/', 'http://poi.mapbar.com/shenyang/', 'http://poi.mapbar.com/suining/',
          'http://poi.mapbar.com/shannan/', 'http://poi.mapbar.com/shihezi/', 'http://poi.mapbar.com/shuanghe/',
          'http://poi.mapbar.com/shangluo/', 'http://poi.mapbar.com/shizuishan/', 'http://poi.mapbar.com/shaoguan/',
          'http://poi.mapbar.com/shantou/', 'http://poi.mapbar.com/shanwei/', 'http://poi.mapbar.com/shenzhen/',
          'http://poi.mapbar.com/sanya/', 'http://poi.mapbar.com/sansha/', 'http://poi.mapbar.com/shanghai/',
          'http://poi.mapbar.com/suzhou1/', 'http://poi.mapbar.com/suqian/', 'http://poi.mapbar.com/shaoxing/',
          'http://poi.mapbar.com/sanming/', 'http://poi.mapbar.com/shangrao/', 'http://poi.mapbar.com/suzhou2/',
          'http://poi.mapbar.com/tianjin/', 'http://poi.mapbar.com/tangshan/', 'http://poi.mapbar.com/taiyuan/',
          'http://poi.mapbar.com/tongliao/', 'http://poi.mapbar.com/tianmen/', 'http://poi.mapbar.com/tonghua/',
          'http://poi.mapbar.com/tieling/', 'http://poi.mapbar.com/tongren/', 'http://poi.mapbar.com/tulufan/',
          'http://poi.mapbar.com/tacheng/', 'http://poi.mapbar.com/tumushuke/', 'http://poi.mapbar.com/tiemenguan/',
          'http://poi.mapbar.com/tongchuan/', 'http://poi.mapbar.com/tianshui/', 'http://poi.mapbar.com/tunchang/',
          'http://poi.mapbar.com/taizhou1/', 'http://poi.mapbar.com/taizhou2/', 'http://poi.mapbar.com/taian/',
          'http://poi.mapbar.com/tongling/', 'http://poi.mapbar.com/wuhai/', 'http://poi.mapbar.com/wulanchabu/',
          'http://poi.mapbar.com/wuhan/', 'http://poi.mapbar.com/wenshan/', 'http://poi.mapbar.com/wulumuqi/',
          'http://poi.mapbar.com/wujiaqu/', 'http://poi.mapbar.com/weinan/', 'http://poi.mapbar.com/wuwei/',
          'http://poi.mapbar.com/wuzhong/', 'http://poi.mapbar.com/wuzhou/', 'http://poi.mapbar.com/wanning/',
          'http://poi.mapbar.com/wenchang/', 'http://poi.mapbar.com/wuzhishan/', 'http://poi.mapbar.com/wuxi/',
          'http://poi.mapbar.com/wenzhou/', 'http://poi.mapbar.com/weihai/', 'http://poi.mapbar.com/weifang/',
          'http://poi.mapbar.com/wuhu/', 'http://poi.mapbar.com/xingtai/', 'http://poi.mapbar.com/xinzhou/',
          'http://poi.mapbar.com/xinganmeng/', 'http://poi.mapbar.com/xilinguolemeng/',
          'http://poi.mapbar.com/xinxiang/', 'http://poi.mapbar.com/xuchang/', 'http://poi.mapbar.com/xinyang/',
          'http://poi.mapbar.com/xiangtan/', 'http://poi.mapbar.com/xiangxi/', 'http://poi.mapbar.com/xiangyang/',
          'http://poi.mapbar.com/xiaogan/', 'http://poi.mapbar.com/xianning/', 'http://poi.mapbar.com/xiantao/',
          'http://poi.mapbar.com/xishuangbanna/', 'http://poi.mapbar.com/xian/', 'http://poi.mapbar.com/xianyang/',
          'http://poi.mapbar.com/xining/', 'http://poi.mapbar.com/xuzhou/', 'http://poi.mapbar.com/xiamen/',
          'http://poi.mapbar.com/xinyu/', 'http://poi.mapbar.com/xuancheng/', 'http://poi.mapbar.com/yangquan/',
          'http://poi.mapbar.com/yuncheng/', 'http://poi.mapbar.com/yiyang/', 'http://poi.mapbar.com/yueyang/',
          'http://poi.mapbar.com/yongzhou/', 'http://poi.mapbar.com/yichang/', 'http://poi.mapbar.com/yichun1/',
          'http://poi.mapbar.com/yanbian/', 'http://poi.mapbar.com/yingkou/', 'http://poi.mapbar.com/yibin/',
          'http://poi.mapbar.com/yaan/', 'http://poi.mapbar.com/yuxi/', 'http://poi.mapbar.com/yili/',
          'http://poi.mapbar.com/yanan/', 'http://poi.mapbar.com/yulin1/', 'http://poi.mapbar.com/yinchuan/',
          'http://poi.mapbar.com/yushu/', 'http://poi.mapbar.com/yunfu/', 'http://poi.mapbar.com/yangjiang/',
          'http://poi.mapbar.com/yulin2/', 'http://poi.mapbar.com/yancheng/', 'http://poi.mapbar.com/yangzhou/',
          'http://poi.mapbar.com/yantai/', 'http://poi.mapbar.com/yingtan/', 'http://poi.mapbar.com/yichun2/',
          'http://poi.mapbar.com/zhangjiakou/', 'http://poi.mapbar.com/zhengzhou/', 'http://poi.mapbar.com/zhoukou/',
          'http://poi.mapbar.com/zhumadian/', 'http://poi.mapbar.com/zhangjiajie/', 'http://poi.mapbar.com/zhuzhou/',
          'http://poi.mapbar.com/zigong/', 'http://poi.mapbar.com/ziyang/', 'http://poi.mapbar.com/zhaotong/',
          'http://poi.mapbar.com/zunyi/', 'http://poi.mapbar.com/zhangye/', 'http://poi.mapbar.com/zhongwei/',
          'http://poi.mapbar.com/zhuhai/', 'http://poi.mapbar.com/zhongshan/', 'http://poi.mapbar.com/zhaoqing/',
          'http://poi.mapbar.com/zhanjiang/', 'http://poi.mapbar.com/zhenjiang/', 'http://poi.mapbar.com/zhoushan/',
          'http://poi.mapbar.com/zhangzhou/', 'http://poi.mapbar.com/zibo/', 'http://poi.mapbar.com/zaozhuang/']


ttbloo = False

for name, href in zip(name___, url___):
    print(name, href + "G70/")
    if name =="杭州市":
        ttbloo = True
    if ttbloo:
        text_req = requests.get(url=href + "G70/").text
        selector = etree.HTML(text_req)
        list_addrs = selector.xpath("//div[@class='sortC']/dl/dd/a/text()")
        for addr in list_addrs:
            print(name+addr)
            jdbc.in_dqname("zz_dqname",name+addr)
        print(list_addrs)
