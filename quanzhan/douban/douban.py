#!/usr/bin/env python
# coding:utf8


'''
本方法已失效，豆瓣网站已封IP地址
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import json
from bs4 import BeautifulSoup

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request,timeout=20)
result = json.loads(response.read())
# result = response.read()
tags = result["tags"]
print result
# movies = []
# for x in xrange(0,1):

# for tag in tags:
	# start = 0
	# while start<300:
	# 	url = 'https://movie.douban.com/explore#!type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)

	# 	# print url

	# 	request = urllib2.Request(url=url, headers=headers)
	# 	response = urllib2.urlopen(request,timeout=20)
		
	# 	result = response.read()
	# 	print result
		
	# 	start +=20


		# r = response.read()
		# r = r.decode("utf-8-sig")
		# result = json.loads(r)

		# result = result["subjects"]

		# if len(result) == 0:
		# 	break

		# for item in result:
		# 	movies.append(item)


