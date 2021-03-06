#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> xj_addrs_cl
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-24 14:37
@Desc   ：
=================================================='''

"""
1. 北京市
东城区 西城区 崇文区 宣武区 朝阳区 海淀区 丰台区 房山区 通州区
顺义区 昌平区 大兴区 怀柔区 平谷区 密云县 延庆县
门头沟区 石景山区

2. 天津市
和平区 河东区 河西区 南开区 河北区 红桥区 塘沽区 汉沽区 大港区
东丽区 西青区 北辰区 津南区 武清区 宝坻区 静海县 宁河县 蓟 县

3. 河北省
辛集市 藁城市 晋州市 新乐市 鹿泉市 平山县 井陉县 栾城县 正定县行唐县 灵寿县 高邑县 赵 县 赞皇县 深泽县 无极县 元氏县 唐山市遵化市 迁安市 迁西县 滦南县 玉田县 唐海县 乐亭县 滦 县 昌黎县卢龙县 抚宁县 邯郸市 武安市 邯郸县 永年县 曲周县 馆陶县 魏 县成安县 大名县 涉 县 鸡泽县 邱 县 广平县 肥乡县 临漳县 磁 县邢台市 南宫市 沙河市 邢台县 柏乡县 任 县 清河县 宁晋县 威 县隆尧县 临城县 广宗县 临西县 内丘县 平乡县 巨鹿县 新河县 南和县保定市 涿州市 定州市 安国市 满城县 清苑县 涞水县 阜平县 徐水县定兴县 唐 县 高阳县 容城县 涞源县 望都县 安新县 易 县 曲阳县蠡 县 顺平县 博野县 雄 县 宣化县 康保县 张北县 阳原县 赤城县沽源县 怀安县 怀来县 崇礼县 尚义县 蔚 县 涿鹿县 万全县 承德市承德县 兴隆县 隆化县 平泉县 滦平县 沧州市 泊头市 任丘市 黄骅市河间市 沧 县 青 县 献 县 东光县 海兴县 盐山县 肃宁县 南皮县吴桥县 廊坊市 霸州市 三河市 固安县 永清县 香河县 大城县 文安县衡水市 冀州市 深州市 饶阳县 枣强县 故城县 阜城县 安平县 武邑县景 县 武强县 石家庄市 张家口市 高碑店市 秦皇岛市 大厂回族自治县青龙满族自治县 丰宁满族自治县 宽城满族自治县 孟村回族自治县围场满族蒙古族自治县

4. 山西省 
太原市 古交市 阳曲县 清徐县 娄烦县 大同市 大同县 天镇县 灵丘县阳高县 左云县 广灵县 浑源县 阳泉市 平定县 盂 县 长治市 潞城市长治县 长子县 平顺县 襄垣县 沁源县 屯留县 黎城县 武乡县 沁 县壶关县 晋城市 高平市 泽州县 陵川县 阳城县 沁水县 朔州市 山阴县右玉县 应 县 怀仁县 晋中市 介休市 昔阳县 灵石县 祁 县 左权县寿阳县 太谷县 和顺县 平遥县 榆社县 运城市 河津市 永济市 闻喜县新绛县 平陆县 垣曲县 绛 县 稷山县 芮城县 夏 县 万荣县 临猗县忻州市 原平市 代 县 神池县 五寨县 五台县 偏关县 宁武县 静乐县繁峙县 河曲县 保德县 定襄县 岢岚县 临汾市 侯马市 霍州市 汾西县吉 县 安泽县 大宁县 浮山县 古 县 隰 县 襄汾县 翼城县 永和县乡宁县 曲沃县 洪洞县 蒲 县 吕梁市 孝义市 汾阳市 文水县 中阳县兴 县 临 县 方山县 柳林县 岚 县 交口县 交城县 石楼县

5. 内蒙古自治区
武川县 包头市 固阳县 乌海市 赤峰市 宁城县 林西县 敖汉旗 开鲁县通辽市 库伦旗 奈曼旗 乌审旗 杭锦旗 根河市 阿荣旗 五原县 磴口县丰镇市 兴和县 卓资县 商都县 凉城县 化德县 多伦县 正蓝旗 镶黄旗兴安盟 突泉县
托克托县 清水河县 喀喇沁旗 巴林左旗 翁牛特旗 巴林右旗 扎鲁特旗准格尔旗 鄂托克旗 达拉特旗 满洲里市 牙克石市 扎兰屯市 杭锦后旗四子王旗 阿巴嘎旗 太仆寺旗 正镶白旗 阿尔山市 扎赉特旗 阿拉善盟额济纳旗
呼和浩特市 和林格尔县 土默特左旗 土默特右旗 克什克腾旗 霍林郭勒市鄂尔多斯市 伊金霍洛旗 鄂托克前旗 呼伦贝尔市 额尔古纳市 陈巴尔虎旗巴彦淖尔市 乌拉特中旗 乌拉特前旗 乌拉特后旗 乌兰察布市 锡林浩特市二连浩特市 苏尼特左旗 苏尼特右旗 锡林郭勒盟 乌兰浩特市 阿拉善左旗阿拉善右旗
阿鲁科尔沁旗 新巴尔虎左旗 新巴尔虎右旗 鄂伦春自治旗 西乌珠穆沁旗东乌珠穆沁旗 科尔沁左翼中旗 科尔沁左翼后旗 鄂温克族自治旗察哈尔右翼前旗 察哈尔右翼中旗 察哈尔右翼后旗 科尔沁右翼前旗科尔沁右翼中旗 达尔罕茂明安联合旗 莫力达瓦达斡尔族自治旗

6. 辽宁省
沈阳市 新民市 法库县 辽中县 康平县 大连市 庄河市 长海县 鞍山市海城市 台安县 抚顺市 抚顺县 本溪市 丹东市 东港市 凤城市 锦州市凌海市 北宁市 黑山县 义 县 营口市 盖州市 阜新市 彰武县 辽阳市灯塔市 辽阳县 盘锦市 盘山县 大洼县 铁岭市 开原市 铁岭县 昌图县西丰县 朝阳市 凌源市 北票市 朝阳县 建平县 兴城市 绥中县 建昌县大石桥市 瓦房店市 普兰店市 调兵山市 葫芦岛市岫岩满族自治县 清原满族自治县 新宾满族自治县 阜新蒙古族自治县宽甸满族自治县 桓仁满族自治县 本溪满族自治县 喀喇沁左翼蒙古族自治县

7. 吉林省
长春市 九台市 榆树市 德惠市 农安县 吉林市 舒兰市 桦甸市 蛟河市磐石市 永吉县 四平市 双辽市 梨树县 辽源市 东辽县 东丰县 通化市集安市 通化县 辉南县 柳河县 白山市 临江市 靖宇县 抚松县 江源县松原市 乾安县 长岭县 扶余县 白城市 大安市 洮南市 镇赉县 通榆县延吉市 图们市 敦化市 龙井市 珲春市 和龙市 安图县 汪清县公主岭市 梅河口市 伊通满族自治县 长白朝鲜族自治县 延边朝鲜族自治州前郭尔罗斯蒙古族自治县

8. 黑龙江省
阿城市 尚志市 双城市 五常市 方正县 宾 县 依兰县 巴彦县 通河县木兰县 延寿县 讷河市 富裕县 拜泉县 甘南县 依安县 克山县 泰来县克东县 龙江县 鹤岗市 萝北县 绥滨县 集贤县 宝清县 友谊县 饶河县鸡西市 密山市 虎林市 鸡东县 大庆市 林甸县 肇州县 肇源县 漠河县伊春市 铁力市 嘉荫县 宁安市 海林市 穆棱市 林口县 东宁县 同江市富锦市 桦川县 抚远县 桦南县 汤原县 勃利县 黑河市 北安市 逊克县嫩江县 孙吴县 绥化市 安达市 肇东市 海伦市 绥棱县 兰西县 明水县青冈县 庆安县 望奎县 呼玛县 塔河县七台河市 双鸭山市 牡丹江市 佳木斯市 绥芬河市 哈尔滨市 齐齐哈尔市五大连池市 杜尔伯特蒙古族自治县

9. 上海市
黄浦区 卢湾区 徐汇区 长宁区 静安区 普陀区 闸北区 虹口区 杨浦区
宝山区 闵行区 嘉定区 松江区 金山区 青浦区 南汇区 奉贤区 崇明县浦东新区

10. 江苏省
南京市 溧水县 高淳县 无锡市 江阴市 宜兴市 徐州市 邳州市 新沂市铜山县 睢宁县 沛 县 丰 县 常州市 金坛市 溧阳市 苏州市 常熟市太仓市 昆山市 吴江市 南通市 如皋市 通州市 海门市 启东市 海安县如东县 东海县 灌云县 赣榆县 灌南县 淮安市 涟水县 洪泽县 金湖县盱眙县 盐城市 东台市 大丰市 建湖县 响水县 阜宁县 射阳县 滨海县扬州市 高邮市 江都市 仪征市 宝应县 镇江市 丹阳市 扬中市 句容市泰州市 泰兴市 姜堰市 靖江市 兴化市 宿迁市 沭阳县 泗阳县 泗洪县连云港市 张家港市

11. 浙江省
杭州市 建德市 富阳市 临安市 桐庐县 淳安县 宁波市 余姚市 慈溪市奉化市 宁海县 象山县 温州市 瑞安市 乐清市 永嘉县 洞头县 平阳县苍南县 文成县 泰顺县 嘉兴市 海宁市 平湖市 桐乡市 嘉善县 海盐县湖州市 长兴县 德清县 安吉县 绍兴市 诸暨市 上虞市 嵊州市 绍兴县新昌县 金华市 兰溪市 义乌市 东阳市 永康市 武义县 浦江县 磐安县衢州市 江山市 龙游县 常山县 开化县 舟山市 岱山县 嵊泗县 台州市临海市 玉环县 天台县 仙居县 三门县 丽水市 龙泉市 缙云县 青田县云和县 遂昌县 松阳县 庆元县 景宁畲族自治县

12. 安徽省
合肥市 长丰县 肥东县 肥西县 芜湖市 芜湖县 南陵县 繁昌县 蚌埠市怀远县 固镇县 五河县 淮南市 凤台县 当涂县 淮北市 濉溪县 铜陵市安庆市 桐城市 宿松县 枞阳县 太湖县 怀宁县 岳西县 望江县 潜山县黄山市 休宁县 歙 县 祁门县 黟 县 滁州市 天长市 明光市 全椒县来安县 定远县 凤阳县 阜阳市 界首市 临泉县 颍上县 阜南县 太和县宿州市 萧 县 泗 县 砀山县 灵璧县 巢湖市 含山县 无为县 庐江县和 县 六安市 寿 县 霍山县 霍邱县 舒城县 金寨县 亳州市 利辛县涡阳县 蒙城县 池州市 东至县 石台县 青阳县 宣城市 宁国市 广德县郎溪县 泾 县 旌德县 绩溪县 马鞍山市

13. 福建省
福州市 福清市 长乐市 闽侯县 闽清县 永泰县 连江县 罗源县 平潭县厦门市 莆田市 仙游县 三明市 永安市 明溪县 将乐县 大田县 宁化县建宁县 沙 县 尤溪县 清流县 泰宁县 泉州市 石狮市 晋江市 南安市惠安县 永春县 安溪县 德化县 金门县 漳州市 龙海市 平和县 南靖县诏安县 漳浦县 华安县 东山县 长泰县 云霄县 南平市 建瓯市 邵武市建阳市 松溪县 光泽县 顺昌县 浦城县 政和县 龙岩市 漳平市 长汀县武平县 上杭县 永定县 连城县 宁德市 福安市 福鼎市 寿宁县 霞浦县柘荣县 屏南县 古田县 周宁县 武夷山市

14. 江西省
南昌市 新建县 南昌县 进贤县 安义县 乐平市 浮梁县 萍乡市 莲花县上栗县 芦溪县 九江市 瑞昌市 九江县 星子县 武宁县 彭泽县 永修县修水县 湖口县 德安县 都昌县 新余市 分宜县 鹰潭市 贵溪市 余江县赣州市 瑞金市 南康市 石城县 安远县 赣 县 宁都县 寻乌县 兴国县定南县 上犹县 于都县 龙南县 崇义县 信丰县 全南县 大余县 会昌县吉安市 吉安县 永丰县 永新县 新干县 泰和县 峡江县 遂川县 安福县吉水县 万安县 宜春市 丰城市 樟树市 高安市 铜鼓县 靖安县 宜丰县奉新县 万载县 上高县 抚州市 南丰县 乐安县 金溪县 南城县 东乡县资溪县 宜黄县 广昌县 黎川县 崇仁县 上饶市 德兴市 上饶县 广丰县鄱阳县 婺源县 铅山县 余干县 横峰县 弋阳县 玉山县 万年县井冈山市 景德镇市

15. 山东省
济南市 章丘市 平阴县 济阳县 商河县 青岛市 胶南市 胶州市 平度市莱西市 即墨市 淄博市 桓台县 高青县 沂源县 枣庄市 滕州市 垦利县广饶县 利津县 烟台市 龙口市 莱阳市 莱州市 招远市 蓬莱市 栖霞市海阳市 长岛县 潍坊市 青州市 诸城市 寿光市 安丘市 高密市 昌邑市昌乐县 临朐县 济宁市 曲阜市 兖州市 邹城市 鱼台县 金乡县 嘉祥县微山县 汶上县 泗水县 梁山县 泰安市 新泰市 肥城市 宁阳县 东平县威海市 乳山市 文登市 荣成市 日照市 五莲县 莒 县 莱芜市 临沂市沂南县 郯城县 沂水县 苍山县 费 县 平邑县 莒南县 蒙阴县 临沭县德州市 乐陵市 禹城市 陵 县 宁津县 齐河县 武城县 庆云县 平原县夏津县 临邑县 聊城市 临清市 高唐县 阳谷县 茌平县 莘 县 东阿县冠 县 滨州市 邹平县 沾化县 惠民县 博兴县 阳信县 无棣县 菏泽市鄄城县 单 县 郓城县 曹 县 定陶县 巨野县 东明县 成武县

16. 河南省
郑州市 巩义市 新郑市 新密市 登封市 荥阳市 中牟县 开封市 开封县尉氏县 兰考县 杞 县 通许县 洛阳市 偃师市 孟津县 汝阳县 伊川县洛宁县 嵩 县 宜阳县 新安县 栾川县 汝州市 舞钢市 宝丰县 叶 县郏 县 鲁山县 安阳市 林州市 安阳县 滑 县 内黄县 汤阴县 鹤壁市浚 县 淇 县 新乡市 卫辉市 辉县市 新乡县 获嘉县 原阳县 长垣县封丘县 延津县 焦作市 沁阳市 孟州市 修武县 温 县 武陟县 博爱县濮阳市 濮阳县 南乐县 台前县 清丰县 范 县 许昌市 禹州市 长葛市许昌县 鄢陵县 襄城县 漯河市 临颍县 舞阳县 义马市 灵宝市 渑池县卢氏县 陕 县 南阳市 邓州市 桐柏县 方城县 淅川县 镇平县 唐河县南召县 内乡县 新野县 社旗县 西峡县 商丘市 永城市 宁陵县 虞城县民权县 夏邑县 柘城县 睢 县 信阳市 潢川县 淮滨县 息 县 新 县商城县 固始县 罗山县 光山县 周口市 项城市 商水县 淮阳县 太康县鹿邑县 西华县 扶沟县 沈丘县 郸城县 确山县 新蔡县 上蔡县 西平县泌阳县 平舆县 汝南县 遂平县 正阳县 济源市三门峡市 平顶山市 驻马店市

17. 湖北省
武汉市 黄石市 大冶市 阳新县 十堰市 郧 县 竹山县 房 县 郧西县竹溪县 荆州市 洪湖市 石首市 松滋市 监利县 公安县 江陵县 宜昌市宜都市 当阳市 枝江市 秭归县 远安县 兴山县 襄樊市 枣阳市 宜城市南漳县 谷城县 保康县 鄂州市 荆门市 钟祥市 京山县 沙洋县 孝感市应城市 安陆市 汉川市 云梦县 大悟县 孝昌县 黄冈市 麻城市 武穴市红安县 罗田县 浠水县 蕲春县 黄梅县 英山县 团风县 咸宁市 赤壁市嘉鱼县 通山县 崇阳县 通城县 随州市 广水市 仙桃市 天门市 潜江市恩施市 利川市 建始县 来凤县 巴东县 鹤峰县 宣恩县 咸丰县丹江口市 老河口市 神农架林区 五峰土家族自治县 长阳土家族自治县

18. 湖南省
长沙市 浏阳市 长沙县 望城县 宁乡县 株洲市 醴陵市 株洲县 炎陵县茶陵县 攸 县 湘潭市 湘乡市 韶山市 湘潭县 衡阳市 耒阳市 常宁市衡阳县 衡东县 衡山县 衡南县 祁东县 邵阳市 武冈市 邵东县 洞口县新邵县 绥宁县 新宁县 邵阳县 隆回县 城步苗族自治县 岳阳市 临湘市汨罗市 岳阳县 湘阴县 平江县 华容县 常德市 津市市 澧 县 临澧县桃源县 汉寿县 安乡县 石门县 慈利县 桑植县 益阳市 沅江市 桃江县南 县 安化县 郴州市 资兴市 宜章县 汝城县 安仁县 嘉禾县 临武县桂东县 永兴县 桂阳县 永州市 祁阳县 蓝山县 宁远县 新田县 东安县江永县 道 县 双牌县 怀化市 洪江市 会同县 沅陵县 辰溪县 溆浦县中方县 娄底市 涟源市 新化县 双峰县 吉首市 古丈县 龙山县 永顺县凤凰县 泸溪县 保靖县 花垣县 冷水江市 张家界市江华瑶族自治县 芷江侗族自治县 新晃侗族自治县 通道侗族自治县靖州苗族侗族自治县 麻阳苗族自治县 湘西土家族苗族自治州

19. 广东省
广州市 从化市 增城市 深圳市 珠海市 汕头市 南澳县 韶关市 乐昌市南雄市 仁化县 始兴县 翁源县 新丰县 佛山市 江门市 台山市 开平市鹤山市 恩平市 湛江市 廉江市 雷州市 吴川市 遂溪县 徐闻县 茂名市高州市 化州市 信宜市 电白县 肇庆市 高要市 四会市 广宁县 德庆县封开县 怀集县 惠州市 惠东县 博罗县 龙门县 梅州市 兴宁市 梅 县蕉岭县 大埔县 丰顺县 五华县 平远县 汕尾市 陆丰市 海丰县 陆河县河源市 和平县 龙川县 紫金县 连平县 东源县 阳江市 阳春市 阳西县阳东县 清远市 英德市 连州市 佛冈县 阳山县 清新县 东莞市 中山市潮州市 潮安县 饶平县 揭阳市 普宁市 揭东县 揭西县 惠来县 云浮市罗定市 云安县 新兴县 郁南县乳源瑶族自治县 连山壮族瑶族自治县 连南瑶族自治县

20. 广西壮族自治区
南宁市 武鸣县 隆安县 马山县 上林县 宾阳县 横 县 柳州市 柳江县桂林市 阳朔县 临桂县 灵川县 全州县 平乐县 兴安县 灌阳县 荔浦县资源县 永福县 梧州市 岑溪市 苍梧县 藤 县 蒙山县 北海市 合浦县东兴市 上思县 钦州市 灵山县 浦北县 贵港市 桂平市 平南县 玉林市北流市 容 县 陆川县 博白县 兴业县 百色市 凌云县 平果县 西林县乐业县 德保县 田林县 田阳县 靖西县 田东县 那坡县 贺州市 钟山县昭平县 河池市 宜州市 天峨县 凤山县 南丹县 东兰县 来宾市 合山市象州县 武宣县 忻城县 崇左市 凭祥市 宁明县 扶绥县 龙州县 大新县天等县 防城港市
三江侗族自治县 大化瑶族自治县 巴马瑶族自治县 龙胜各族自治县金秀瑶族自治县 融水苗族自治县 隆林各族自治县 恭城瑶族自治县都安瑶族自治县 富川瑶族自治县 环江毛南族自治县 罗城仫佬族自治县

21. 海南省
海口市 琼海市 儋州市 文昌市 万宁市 东方市 澄迈县 定安县 屯昌县临高县 三亚市 五指山市白沙黎族自治县 昌江黎族自治县 乐东黎族自治县 陵水黎族自治县保亭黎族苗族自治县 琼中黎族苗族自治县

22. 重庆市
渝中区 江北区 南岸区 北碚区 万盛区 双桥区 渝北区 巴南区 万州区涪陵区 黔江区 长寿区 九龙坡区 大渡口区 沙坪坝区永川市 合川市 江津市 南川市 綦江县 潼南县 荣昌县 璧山县 大足县铜梁县 梁平县 城口县 垫江县 武隆县 丰都县 奉节县 开 县 云阳县忠 县 巫溪县 巫山县石柱土家族自治县 秀山土家族苗族自治县 酉阳土家族苗族自治县彭水苗族土家族自治县

23. 四川省
成都市 彭州市 邛崃市 崇州市 金堂县 郫 县 新津县 双流县 蒲江县大邑县 自贡市 荣 县 富顺县 米易县 盐边县 泸州市 泸 县 合江县叙永县 古蔺县 德阳市 广汉市 什邡市 绵竹市 罗江县 中江县 绵阳市江油市 盐亭县 三台县 平武县 安 县 梓潼县 广元市 青川县 旺苍县剑阁县 苍溪县 遂宁市 射洪县 蓬溪县 大英县 内江市 资中县 隆昌县威远县 乐山市 夹江县 井研县 犍为县 沐川县 南充市 阆中市 营山县蓬安县 仪陇县 南部县 西充县 眉山市 仁寿县 彭山县 洪雅县 丹棱县青神县 宜宾市 宜宾县 兴文县 南溪县 珙 县 长宁县 高 县 江安县筠连县 屏山县 广安市 华蓥市 岳池县 邻水县 武胜县 达州市 万源市达 县 渠 县 宣汉县 开江县 大竹县 雅安市 芦山县 石棉县 名山县天全县 荥经县 宝兴县 汉源县 巴中市 南江县 平昌县 通江县 资阳市简阳市 安岳县 乐至县 红原县 汶川县 阿坝县 理 县 小金县 黑水县金川县 松潘县 壤塘县 茂 县 康定县 丹巴县 炉霍县 九龙县 甘孜县雅江县 新龙县 道孚县 白玉县 理塘县 德格县 乡城县 石渠县 稻城县色达县 巴塘县 泸定县 得荣县 西昌市 美姑县 昭觉县 金阳县 甘洛县布拖县 雷波县 普格县 宁南县 喜德县 会东县 越西县 会理县 盐源县德昌县 冕宁县马尔康县 九寨沟县 峨眉山市 都江堰市 攀枝花市 若尔盖县北川羌族自治县 木里藏族自治县 马边彝族自治县 峨边彝族自治县甘孜藏族自治州 凉山彝族自治州 阿坝藏族羌族自治州

24. 贵州省
贵阳市 清镇市 开阳县 修文县 息烽县 水城县 盘 县 遵义市 赤水市仁怀市 遵义县 绥阳县 桐梓县 习水县 凤冈县 正安县 余庆县 湄潭县安顺市 普定县 德江县 江口县 思南县 石阡县 毕节市 黔西县 大方县织金县 金沙县 赫章县 纳雍县 兴义市 望谟县 兴仁县 普安县 册亨县晴隆县 贞丰县 安龙县 凯里市 施秉县 从江县 锦屏县 镇远县 麻江县台江县 天柱县 黄平县 榕江县 剑河县 三穗县 雷山县 黎平县 岑巩县丹寨县 都匀市 福泉市 贵定县 惠水县 罗甸县 瓮安县 荔波县 龙里县
平塘县 长顺县 独山县 六盘水市 六枝特区 万山特区三都水族自治县 松桃苗族自治县 玉屏侗族自治县 沿河土家族自治县道真仡佬族苗族自治县 务川仡佬族苗族自治县平坝县 镇宁布依族苗族自治县紫云苗族布依族自治县 关岭布依族苗族自治县铜仁市 印江土家族苗族自治县黔东南苗族侗族自治州 黔西南布依族苗族自治州 威宁彝族回族苗族自治县黔南布依族苗族自治州

25. 云南省
昆明市 安宁市 富民县 嵩明县 呈贡县 晋宁县 宜良县 曲靖市 宣威市陆良县 会泽县 富源县 罗平县 马龙县 师宗县 沾益县 玉溪市 华宁县澄江县 易门县 通海县 江川县 保山市 施甸县 昌宁县 龙陵县 腾冲县昭通市 永善县 绥江县 镇雄县 大关县 盐津县 巧家县 彝良县 威信县水富县 鲁甸县 丽江市 华坪县 永胜县 思茅市 临沧市 镇康县 凤庆县
云 县 永德县 文山县 砚山县 广南县 马关县 富宁县 西畴县 丘北县蒙自县 个旧市 开远市 弥勒县 红河县 绿春县 泸西县 建水县 元阳县石屏县 景洪市 勐海县 楚雄市 元谋县 南华县 牟定县 武定县 大姚县双柏县 禄丰县 永仁县 姚安县 大理市 剑川县 弥渡县 云龙县 洱源县鹤庆县 祥云县 宾川县 永平县 潞西市 瑞丽市 盈江县 梁河县 陇川县泸水县 福贡县 德钦县 麻栗坡县 香格里拉县
宁蒗彝族自治县 河口瑶族自治县 玉龙纳西族自治县 普洱哈尼族彝族自治县漾濞彝族自治县 寻甸回族自治县 墨江哈尼族自治县 江城哈尼族彝族自治县峨山彝族自治县 屏边苗族自治县 澜沧拉祜族自治县 兰坪白族普米族自治县石林彝族自治县 西盟佤族自治县 维西傈僳族自治县 贡山独龙族怒族自治县景东彝族自治县 沧源佤族自治县 巍山彝族回族自治县 景谷彝族傣族自治县
南涧彝族自治县 新平彝族傣族自治县 禄劝彝族苗族自治县孟连傣族拉祜族佤族自治县 金平苗族瑶族傣族自治县元江哈尼族彝族傣族自治县 镇沅彝族哈尼族拉祜族自治县双江拉祜族佤族布朗族傣族自治县 耿马傣族佤族自治县

26. 西藏自治区
拉萨市 林周县 达孜县 尼木县 当雄县 曲水县 那曲县 嘉黎县 申扎县巴青县 聂荣县 尼玛县 比如县 索 县 班戈县 安多县 昌都县 芒康县贡觉县 八宿县 左贡县 边坝县 洛隆县 江达县 丁青县 察雅县 乃东县琼结县 措美县 加查县 贡嘎县 洛扎县 曲松县 桑日县 扎囊县 错那县
隆子县 定结县 萨迦县 江孜县 拉孜县 定日县 康马县 吉隆县 亚东县昂仁县 岗巴县 仲巴县 萨嘎县 仁布县 白朗县 噶尔县 措勤县 普兰县革吉县 日土县 札达县 改则县 林芝县 墨脱县 朗 县 米林县 察隅县波密县 日喀则市 类乌齐县 浪卡子县 聂拉木县 谢通门县 南木林县工布江达县 墨竹工卡县 堆龙德庆县

27. 陕西省
西安市 高陵县 蓝田县 户 县 周至县 铜川市 宜君县 宝鸡市 岐山县凤翔县 陇 县 太白县 麟游县 扶风县 千阳县 眉 县 凤 县 咸阳市礼泉县 泾阳县 永寿县 三原县 彬 县 旬邑县 长武县 乾 县 武功县淳化县 渭南市 韩城市 华阴市 蒲城县 潼关县 白水县 澄城县 华 县合阳县 富平县 大荔县 延安市 安塞县 洛川县 子长县 黄陵县 延川县富 县 延长县 甘泉县 宜川县 志丹县 黄龙县 吴旗县 汉中市 留坝县
镇巴县 城固县 南郑县 洋 县 宁强县 佛坪县 勉 县 西乡县 略阳县榆林市 清涧县 绥德县 神木县 佳 县 府谷县 子洲县 靖边县 横山县米脂县 吴堡县 定边县 安康市 紫阳县 岚皋县 旬阳县 镇坪县 平利县石泉县 宁陕县 白河县 汉阴县 商洛市 镇安县 山阳县 洛南县 商南县丹凤县 柞水县

28. 甘肃省
兰州市 永登县 榆中县 皋兰县 金昌市 永昌县 白银市 靖远县 景泰县会宁县 天水市 武山县 甘谷县 清水县 秦安县 武威市 民勤县 古浪县张掖市 民乐县 山丹县 临泽县 高台县 平凉市 灵台县 静宁县 崇信县华亭县 泾川县 庄浪县 酒泉市 玉门市 敦煌市 安西县 金塔县 庆阳市庆城县 镇原县 合水县 华池县 环 县 宁 县 正宁县 定西市 岷 县
渭源县 陇西县 通渭县 漳 县 临洮县 陇南市 成 县 礼 县 康 县<文 县 两当县 徽 县 宕昌县 西和县 临夏市 临夏县 康乐县 永靖县广河县 和政县 合作市 临潭县 卓尼县 舟曲县 迭部县 玛曲县 碌曲县夏河县 嘉峪关市 东乡族自治县 阿克塞哈萨克族自治县 肃北蒙古族自治县张家川回族自治县 天祝藏族自治县 肃南裕固族自治县积石山保安族东乡族撒拉族自治县

29. 青海省
西宁市 湟源县 湟中县 平安县 乐都县 海晏县 祁连县 刚察县 同仁县泽库县 尖扎县 共和县 同德县 贵德县 兴海县 贵南县 玛沁县 班玛县甘德县 达日县 久治县 玛多县 玉树县 杂多县 称多县 治多县 囊谦县乌兰县 天峻县 都兰县 曲麻莱县 德令哈市 格尔木市门源回族自治县 大通回族土族自治县 河南蒙古族自治县 化隆回族自治县互助土族自治县 民和回族土族自治县 循化撒拉族自治县

30. 宁夏回族自治区
银川市 灵武市 永宁县 贺兰县 平罗县 吴忠市 同心县 盐池县 固原市
西吉县 隆德县 泾源县 彭阳县 中卫市 中宁县 海原县 石嘴山市 青铜峡市

31. 新疆维吾尔自治区
鄯善县 哈密市 伊吾县 和田市 和田县 洛浦县 民丰县 皮山县 策勒县于田县 墨玉县 温宿县 沙雅县 拜城县 库车县 柯坪县 新和县 乌什县喀什市 巴楚县 泽普县 伽师县 叶城县 疏勒县 莎车县 疏附县 乌恰县和静县 尉犁县 和硕县 且末县 博湖县 轮台县 若羌县 昌吉市 阜康市米泉市 奇台县 博乐市 精河县 温泉县 伊宁市 奎屯市 伊宁县 昭苏县新源县 霍城县 巩留县 塔城市 乌苏市 额敏县 裕民县 沙湾县 托里县青河县 富蕴县 福海县
石河子市 阿拉尔市 五家渠市 吐鲁番市 托克逊县 阿克苏市 阿瓦提县岳普湖县 麦盖提县 英吉沙县 阿图什市 阿合奇县 阿克陶县 库尔勒市玛纳斯县 呼图壁县 特克斯县 尼勒克县 吉木乃县 布尔津县 哈巴河县阿勒泰市 乌鲁木齐市 乌鲁木齐县 克拉玛依市 图木舒克市 吉木萨尔县巴里坤哈萨克自治县 塔什库尔干塔吉克自治县 焉耆回族自治县察布查尔锡伯自治县 木垒哈萨克自治县 和布克赛尔蒙古自治县

32. 香港特别行政区
中西区 东 区 观塘区 南 区 湾仔区 离岛区 葵青区 北 区 西贡区 沙田区 屯门区 大埔区 荃湾区 元朗区 九龙城区 油尖旺区 深水埗区 黄大仙区

33. 澳门特别行政区
花地玛堂区（俗称北区，包括青州、台山、黑沙环、筷子基和水塘） 圣安多尼堂区（即花王堂区，在澳门西部，包括新桥和沙梨头；著名的大三巴牌坊一带也属本堂区之内） 大堂区（中区、新马路以北部分、南湾、水坑尾、整个新口岸填海地段、东至新口岸港澳码头，整条环岛公路至妈阁南端，包括澳门旅游塔和立法会） 望德堂区（包括荷兰园、东望洋山、塔石一带） 风顺堂区（亦称圣老愣佐堂区，包括八十年代未进行南湾湖填海的整个妈阁半岛，包括妈阁山、西望洋山、新马路以南部分）

34. 台湾省
台北市  高雄市  基隆市  台中市  台南市  新竹市  嘉义市  台北县  板桥市  宜兰县  宜兰市  新竹县  竹北市  桃园县  桃园市  苗栗县  苗栗市  台中县  丰原市  彰化县  彰化市  南投县  南投市  嘉义县  太保市  云林县  斗六市   台南县  新营市  高雄县  凤山市  屏东县  屏东市  台东县  台东市  花莲县  花莲市  澎湖县  马公市
"""