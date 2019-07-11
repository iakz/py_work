#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import json
from bs4 import BeautifulSoup

# 电影类型
fl = {}
fl['0'] = '全部类型'
fl['3'] = '电视剧'
fl['43'] = '综艺节目'
fl['46'] = '动画片'
fl['48'] = '电影'
# print fl

# 地区
dq = {}
dq['%B4%F3%C2%BD'] = '大陆'
dq['%CF%E3%B8%DB'] = '香港'
dq['%CC%A8%CD%E5'] = '台湾'
dq['%C5%B7%C3%C0'] = '美国'
dq['%BA%AB%B9%FA'] = '韩国'
dq['%C8%D5%B1%BE'] = '日本'
dq['%D3%A2%B9%FA'] = '英国'
dq['%B7%A8%B9%FA'] = '法国'
dq['%B5%C2%B9%FA'] = '德国'
dq['%CC%A9%B9%FA'] = '泰国'
dq['%C6%E4%CB%FB'] = '其他'
# print dq

# 年份
nf = [2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998]

# 字母
zm = 'A'
# print zm
# 分页
page = '1'
url_xq = 'https://www.k8jdwang.com'

# 地区遍历
for x in dq:
	# 暂时只看韩国地区的
	if x != '%CF%E3%B8%DB':
		continue
	# 链接拼接
	url = 'https://www.k8jdwang.com/wunsian.asp?page=' + page + '&fl=3&dq=' + x + '&zm=' + zm
	print url
	request = urllib2.Request(url=url)
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()

	# 获取html页面内容
	html = BeautifulSoup(result,"lxml")

	# 获取页面中包含影片内容的部分
	li = html.select('div.shannel')[0]
	# print li
	lis = li.select('h2')
	print lis
	# 遍历第一页的影片
	for x in lis:
		# print x
		title = x.select('a')[0]
		# print title
		title = title.get_text()
		print unicode(title)
















