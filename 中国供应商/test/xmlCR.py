import os
import xml.dom.minidom as xmldom

x_path="cs.xml"
nodes=list()
xmlfilepath = os.path.abspath(x_path)
def findNodeIndex(node):
    for i in range(len(nodes)):
        if(nodes[i]==node):
            return str(i) # +":"+nodes[i]
print ("xml文件路径：", xmlfilepath)
# 得到文档对象
domobj = xmldom.parse(xmlfilepath)
print("xmldom.parse:", type(domobj))
# 得到元素对象
elementobj = domobj.documentElement
#print ("domobj.documentElement:", type(elementobj))
subElementObj = elementobj.getElementsByTagName("data")
print(len(subElementObj))
for i in range(len(subElementObj)):
    if(subElementObj[i].getAttribute("type")=='twaver.Node'):
        sub2=subElementObj[i].getElementsByTagName("p")
        for j in range(len(sub2)):
            if(sub2[j].getAttribute("n")=='name'):
                node=sub2[j].firstChild.data.replace('...','')
                print("{name:'",node,"',draggable: true,},")
                nodes.append(node)
print("nodes len:",len(nodes))
for i in range(len(subElementObj)):
    if(subElementObj[i].getAttribute("type")=='twaver.Link'):
        sub3=subElementObj[i].getElementsByTagName("c")
        for j in range(len(sub3)):
            node=sub3[j].firstChild.data.replace('...','')
            iNode=findNodeIndex(node)
            if(sub3[j].getAttribute("n")=='aNode'):
                #print(sub3[j].firstChild.data ,' ',iNode, end='')
                print('{source:',iNode, end='')
            elif(sub3[j].getAttribute("n")=='zNode'):
                #print(sub3[j].firstChild.data,' ',iNode)
                print(",target:",iNode,"},")