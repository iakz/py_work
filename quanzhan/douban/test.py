#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import requests

url = 'https://www.k8jdwang.com/wunsian.asp?page=1&fl=48&dq=%C8%D5%B1%BE&zm=A'
# r = requests.get(url)
# demo = r.text  # 服务器返回响应

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()

# 获取html页面内容
html = BeautifulSoup(result,"lxml")

# 获取页面中包含影片内容的部分
h2 = html.select('a')
for x in h2:
	print x.get_text()

# soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
# print(soup)  # 输出响应的html对象
# print(soup.prettify())  # 使用prettify()格式化显示输出
# div = soup.find_all(class_='shannel').children
# print div
# lis = div.find_all('li')
# print lis