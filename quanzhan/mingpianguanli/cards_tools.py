#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import input
# 记录所有名片字典
card_list = []

def show_menu():
	print "*" * 50
	print "欢迎使用【名片管理系统】V1.0\n"
	print "\t1、新建名片\n\t2、显示全部\n\t3、查询名片\n\n\t0、退出系统"
	print "*" *50

def new_card():
	# 新增名片
	print "-" * 50
	# print "新增名片"
	name = raw_input("请输入姓名： ")
	phone = raw_input("请您输入电话： ")
	qq = raw_input("请输入QQ： ")
	email = raw_input("请输入邮箱： ")

	card_dict = {"name" : name,
					"phone" : phone,
					"qq" : qq,
					"email" : email}

	card_list.append(card_dict)
	# print card_list
	print "恭喜您，添加" + name + "成功！"

def show_all():
	# 显示所有名片
	print "-" * 50
	print "显示所有名片"

	# 判断是否有名片记录
	if len(card_list) == 0:
		print "当前没有任何名片记录，请先添加名片吧！"
		return

	# 打印表头
	# for name in ["姓名","电话","QQ","邮箱"]:
		# print(name , end = ("\t\t"))
	print "姓名\t\t电话\t\tQQ\t\t邮箱"

	# 打印分隔线
	print "=" * 50

	# 处理字典显示
	for card_dict in card_list:
		print "%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
										card_dict["phone"],
										card_dict["qq"],
										card_dict["email"])

def search_card():
	# 搜索名片
	print "-" * 50
	print "搜索名片"

	find_name = raw_input("请输入要搜索的姓名： ")

	for card_dict in card_list:
		if card_dict["name"] == find_name:
			#print("找到了")
			
			print "姓名\t\t电话\t\tQQ\t\t邮箱"

			# 打印分隔线
			print "=" * 50

			# 处理字典显示
			print "%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
										card_dict["phone"],
										card_dict["qq"],
										card_dict["email"])
			deal_card(card_dict)
			break

	else:
		print "未找到%s的名片！" % find_name

def deal_card(find_dict):

	#print find_dict
	action_str = raw_input("请选择要进行的操作：【1】、修改 【2】、删除 【0】、返回主菜单： ")
	if action_str == "1":
		find_dict["name"] = input_card_info(find_dict["name"],"姓名：【回车不修改】 ")
		find_dict["phone"] = input_card_info(find_dict["phone"],"手机：【回车不修改】 ")
		find_dict["qq"] = input_card_info(find_dict["qq"],"QQ：【回车不修改】 ")
		find_dict["email"] = input_card_info(find_dict["email"],"邮箱：【回车不修改】 ")
		print "修改名片成功"
	elif action_str == "2":
		card_list.remove(find_dict)
		print "名片已被删除！"

	elif action_str == "0":
		print "您选择了%s，将返回主菜单" % action_str
		return
	else:
		print "您输入有误，将返回主菜单！"

def input_card_info(dict_value,tip_message):
	result_str = raw_input(tip_message)
	if len(result_str) > 0:
		return result_str
	else :
		return dict_value
	
