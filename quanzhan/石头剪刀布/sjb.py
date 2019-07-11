#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
import random
sys.setdefaultencoding('utf8')

# print '玩家出的是：' + str(player) + ' , 电脑出的是：' + str(computer)
a = 1
while a:
	player = int(input('请输入您要出的拳，石头1/剪刀2/布3：'))
	computer = random.randint(1,3)

	if player ==1:
		player1 = '石头'
	elif player == 2:
		player1 = '剪刀'
	elif player == 3:
		player1 = '布'
	else:
		player1 = '用户输入无效，请输入石头1/剪刀2/布3：'
	
	if computer ==1:
		computer1 = '石头'
	elif computer == 2:
		computer1 = '剪刀'
	elif computer == 3:
		computer1 = '布'
	else:
		computer1 = '电脑输入无效，请输入石头1/剪刀2/布3：'



	if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer ==1):
		print '玩家出的是：' + player1 + ' , 电脑出的是：' + computer1
		print '电脑弱爆了！'
		a = int(input('再来一次请输入1，结束请输入0：'))
	elif player == computer:
		print '玩家出的是：' + player1 + ' , 电脑出的是：' + computer1
		print '真是心有灵犀啊！'
		a = int(input('再来一次请输入1，结束请输入0：'))
	elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer ==2):
		print '玩家出的是：' + player1 + ' , 电脑出的是：' + computer1
		print '我不服！'
		a = int(input('再来一次请输入1，结束请输入0：'))
	else:
		print player1
		a = int(input('再来一次请输入1，结束请输入0：'))