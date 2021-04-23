from xml.dom.minidom import parse


def redztXml():
    # 这个是标准字体库  可以用于匹配  获取name  即是对应的数字
    domTree1 = parse("..\\test\\ztkuBZ.xml")
    domTree2 = parse("..\\test\\ztku02.xml")
    # 文档根元素
    rootNode1 = domTree1.documentElement
    rootNode2 = domTree2.documentElement
    # print(rootNode.nodeName)

    conte = 1
    customers1 = rootNode1.getElementsByTagName("CharString")
    customers2 = rootNode2.getElementsByTagName("CharString")
    for customer1 in customers1[1:]:
        for customer2 in customers2[1:]:
            conte += 1

            # if customer1.hasAttribute("name"):
            data1 = customer1.childNodes[0].data
            data2 = customer2.childNodes[0].data
            # 判断两个的字体长度是否一样  先要消除掉空格
            if len(data1.replace(" ", "")) == len(data2.replace(" ", "")):
                print("data1 == data2------------------------------------------------------------------------------------------------------- ")
                print("对应的数字是：：：:", customer1.getAttribute("name"))
                print(data1)
                print(len(data1))
                print()
                print(data2)
                print(len(data2))
            # print("neirong:", data1)
    print("一共匹配了",conte ,"次")


if __name__ == '__main__':
    redztXml()
