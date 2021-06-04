#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> ocrText
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-02 14:10
@Desc   ：
=================================================='''
from PIL import Image
import pytesseract

img = Image.open("image\sj.jpg")
text = pytesseract.image_to_string(img)

print(text)
print(int(text))
print(type(text))