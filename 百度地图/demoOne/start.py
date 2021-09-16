#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-06 11:21
@Desc   ：
=================================================='''

"""

https://map.baidu.com/search/%E7%BE%8E%E9%A3%9F/
@12959238.56,4825347.47,12z
?querytype=s&
c=131&wd=%E7%BE%8E%E9%A3%9F&
da_src=shareurl&
on_gel=1&
l=12&
gr=1&
b=(12898878.573899986,4817014.70333334;12972063.35783332,4861671.606666674)&
pl_data_type=cater&
pl_sub_type=%E9%A4%90%E9%A6%86&
pl_price_section=0,%2B&
pl_sort_type=data_type&
pl_sort_rule=0&
pl_discount2_section=0,%2B&
pl_groupon_section=0,%2B&
pl_cater_book_pc_section=0,%2B&
pl_hotel_book_pc_section=0,%2B&
pl_ticket_book_flag_section=0,%2B&
pl_movie_book_section=0,%2B&
pl_business_type=cater&
pn=0&
seckey=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45f6977f64bf9009116ae792b191e500f8f089a7cd2938d534c3080b8679ebba23aa96e5028efcd9e394c5414d455535f9d1fad24f483924e3ee66dd3a89e78edbfdc41e0f098cd641ab1058434339771d98473530461c4022ae6c0a564bca46ec5a8e8bdc6e742f628d61f3aed56b577307faaf023a94f39d57253f5433ead741e1d1958c277dbb5199ed73163e4f90c6faaee2101a55c8af3569d04abff921a1a463852706e93db09fa3f4c805489e32&
device_ratio=2
"""


"""

https://map.baidu.com/?
newmap=1&
reqflag=pcmap&
biz=1&
from=webmap&
da_par=direct&
pcevaname=pc4.1&
qt=spot&
from=webmap&
c=131&
wd=%E7%BE%8E%E9%A3%9F&
wd2=&
pn=0&
nn=0&
db=0&
sug=0&
addr=0&
pl_data_type=cater&
pl_sub_type=%E9%A4%90%E9%A6%86&
pl_price_section=0%2C%2B&
pl_sort_type=data_type&
pl_sort_rule=0&
pl_discount2_section=0%2C%2B&
pl_groupon_section=0%2C%2B&
pl_cater_book_pc_section=0%2C%2B&
pl_hotel_book_pc_section=0%2C%2B&
pl_ticket_book_flag_section=0%2C%2B&
pl_movie_book_section=0%2C%2B&
pl_business_type=cater&
pl_business_id=&
da_src=pcmappg.poi.page&
on_gel=1&
src=7&
gr=3&
l=12&
rn=50&
tn=B_NORMAL_MAP&
auth=IUMeSJgERTfQcKgSVW77vU44IDY48b6zuxLBVRTRHTztCbmUComdB9AvYgP1PcGCgYvjPuVtvYgPMGvgWv%40uVtvYgPPxRYuVtvYgP%40vYZcvWPCuVtvYgP%40ZPcPPuVtvYgPhPPyheuVtvhgMuxVVty1uVtCGYuVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuVtPYIuVtPYIUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVtc3CuVtcvY1SGpuzxtfvyuf0wd0vyMC7SUSIUyuosSSEb1rZZWuV&seckey=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45f6977f64bf9009116ae792b191e500f8f089a7cd2938d534c3080b8679ebba23aa96e5028efcd9e394c5414d455535f9d1fad24f483924e3ee66dd3a89e78edbfdc41e0f098cd641ab1058434339771d98473530461c4022ae6c0a564bca46ec5a8e8bdc6e742f628d61f3aed56b577307faaf023a94f39d57253f5433ead7417b7d1af2ce4f7aa410b79452308ced6351be09853325946fbb1058d5e2a57441807efd335efea9585fe53f2243277364&
ie=utf-8&
b=(12900678.56,4811587.47;13017798.56,4839107.47)&
t=1630898593460

"""