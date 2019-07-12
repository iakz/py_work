#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cards_tools

while True:

	# 显示功能菜单
	cards_tools.show_menu()

	action_str = raw_input("请选择您的操作：")
	print "您的操作是【%s】" %action_str

# 针对名片的操作
	if action_str in ['1','2','3']:
		if action_str == '1':
			cards_tools.new_card()
		elif action_str == '2':
			cards_tools.show_all()
		elif action_str == '3':
			cards_tools.search_card()
		else:
			print '您输入有误，请重新输入：'

			# 退出系统
	elif action_str == '0':
		print '欢迎再次使用本系统！'
		break

		# 其他内容输入错误
	else :
		print '您输入有误，请重新输入：'

