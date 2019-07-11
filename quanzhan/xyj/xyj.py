#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

fr = open("xyj.txt","r")

characters = []
stat = {}

for line in fr:

	line = line.strip()

	if len(line)==0:
		continue

	line = unicode(line)

	for x in xrange(0,len(line)):

		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue

		if not line[x] in characters:
			characters.append(line[x])
	
		if not stat.has_key(line[x]):
			stat[line[x]]=0
		stat[line[x]]+=1
	
# print len(characters)
# print characters
# for key,value in stat.items():
# 	print key,value
stat = sorted(stat.iteritems(),key=lambda d:d[1],reverse=True)

print type(stat),len(stat)

for x in xrange(1,20):
	print characters[x]

for x in xrange(1,20):
	print stat[x][0],stat[x][1]
fr.close()