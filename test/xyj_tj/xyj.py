#!/usr/bin/env python2.7
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

fr = open('xyj.txt','r')

characers = []
stat = {}

for line in fr:
	line = line.strip()

	if len(line)==0:
		continue
	
	line = unicode(line)

	for x in xrange(0, len(line)):
		if not line[x] in characers:
			characers.append(line[x])

		if not stat.has_key(line[x]):
			stat[line[x]]=0
		stat[line[x]] +=1

characers
print(len(characers))
print(characers)
for key,value in stat.items():
	key=unicode(key)
	print(key,value)
#stat = sorted(stat.iteritems(),key=lambda d:d[1],reverse=True)

#for x in xrange(1,10):
#	print(characers[x])