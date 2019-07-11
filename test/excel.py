#https://www.jb51.net/article/60510.htm
import requests
import json
import xlrd
import xlwt
#from xlrd import copy
#from xlwt import *
from xlutils.copy import copy


###########
#1、删除桌面r1.xlsx文件
#2、修改接口日期
#3、修改最新导出的报表文件名
#4、修改C端和B端报表数量，在循环条件中


#def read_excel():
#读取报表文件格式
workbook = xlrd.open_workbook("‪C:\Users\24508\Desktop\r.xlsx")
print(workbook.sheet_names())
sheet1_name = workbook.sheet_names()[0]
sheet1 = workbook.sheet_by_index(0)
sheet1 = workbook.sheet_by_name("Sheet1")

print(sheet1.cell(1,1))

new_excel = copy(workbook)
ws = new_excel.get_sheet(0)

#89调度量返回数据接口
url ="https://work-zds.yhulian.cn/api/reports/case-static?startdate=2019-01-20&enddate=2019-01-20"
r = requests.get(url)

#print('get请求获取的响应结果json类型',r.text)
#print("get请求获取响应状态码",r.status_code)
#print("get请求获取响应头",r.headers['Content-Type'])

json_r = r.json()
#print(json_r)
summ = json_r["summary"]
#print(summ)
#xra = ["上海","广东","湖北","安徽","江西","江苏","深圳","苏州","福建","山东","青岛","宁波","浙江","黑龙江","四川","陕西","天津"]

# def foo(var):
#     return {
#             "上海":ws.write(70,3,region.get("dispatchCount")),
# 			"安徽":ws.write(71,2,region.get("dispatchCount")),
# 			"浙江":ws.write(70,2,region.get("dispatchCount")),
# 			"四川":ws.write(71,2,region.get("dispatchCount")),
# 			"陕西":ws.write(70,2,region.get("dispatchCount")),
# 			"湖南":ws.write(71,2,region.get("dispatchCount")),
# 			"宁波":ws.write(70,2,region.get("dispatchCount")),
# 			"深圳":ws.write(71,2,region.get("dispatchCount")),
# 			"江苏":ws.write(70,2,region.get("dispatchCount")),
# 			"山东":ws.write(71,2,region.get("dispatchCount")),
# 			"重庆":ws.write(70,2,region.get("dispatchCount")),
# 			"山西":ws.write(71,2,region.get("dispatchCount")),
# 			"内蒙古":ws.write(70,2,region.get("dispatchCount")),
# 			"广东":ws.write(71,2,region.get("dispatchCount")),
# 			"福建":ws.write(70,2,region.get("dispatchCount")),
# 			"河南":ws.write(71,2,region.get("dispatchCount")),
# 			"云南":ws.write(70,2,region.get("dispatchCount")),
# 			"北京":ws.write(71,2,region.get("dispatchCount")),
# 			"黑龙江":ws.write(71,2,region.get("dispatchCount")),
# 			"湖北":ws.write(71,2,region.get("dispatchCount")),
# 			"青岛":ws.write(71,2,region.get("dispatchCount")),
# 			"辽宁":ws.write(71,2,region.get("dispatchCount")),
# 			"贵州":ws.write(71,2,region.get("dispatchCount")),
# 			"天津":ws.write(71,2,region.get("dispatchCount")),
# 			"吉林":ws.write(71,2,region.get("dispatchCount")),
# 			"厦门":ws.write(71,2,region.get("dispatchCount")),
# 			"大连":ws.write(71,2,region.get("dispatchCount")),
# 			"苏州":ws.write(71,2,region.get("dispatchCount")),
# 			"河北":ws.write(71,2,region.get("dispatchCount")),
# 			"江西":ws.write(71,2,region.get("dispatchCount")),
# 			"广西":ws.write(71,2,region.get("dispatchCount")),
#     }.get(var,'error')

#获取各分公司C端89调度量和接通量并写入文件
for region in summ :
	#print(region)
	#print("地区：	"+region.get("region"))
	reg = region.get("region")
	reg = reg[:-3]
	print(reg)
	#foo(reg)
	if "上海"==reg:
		ws.write(71,2,region.get("dispatchCount"))
		ws.write(71,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(92,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "广东"==reg:
		ws.write(72,2,region.get("dispatchCount"))
		ws.write(72,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(93,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "湖北"==reg:
		ws.write(73,2,region.get("dispatchCount"))
		ws.write(73,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(94,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "安徽"==reg:
		ws.write(74,2,region.get("dispatchCount"))
		ws.write(74,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(95,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "江西"==reg:
		ws.write(75,2,region.get("dispatchCount"))
		ws.write(75,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(96,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "江苏"==reg:
		ws.write(76,2,region.get("dispatchCount"))
		ws.write(76,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(97,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "深圳"==reg:
		ws.write(77,2,region.get("dispatchCount"))
		ws.write(77,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(98,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "苏州"==reg:
		ws.write(78,2,region.get("dispatchCount"))
		ws.write(78,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(99,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "福建"==reg:
		ws.write(79,2,region.get("dispatchCount"))
		ws.write(79,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(100,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "山东"==reg:
		ws.write(80,2,region.get("dispatchCount"))
		ws.write(80,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(101,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "青岛"==reg:
		ws.write(81,2,region.get("dispatchCount"))
		ws.write(81,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(102,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "宁波"==reg:
		ws.write(82,2,region.get("dispatchCount"))
		ws.write(82,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(103,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "浙江"==reg:
		ws.write(83,2,region.get("dispatchCount"))
		ws.write(83,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(104,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "黑龙江"==reg:
		ws.write(84,2,region.get("dispatchCount"))
		ws.write(84,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(105,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "四川"==reg:
		ws.write(85,2,region.get("dispatchCount"))
		ws.write(85,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(106,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "陕西"==reg:
		ws.write(86,2,region.get("dispatchCount"))
		ws.write(86,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(107,2,region.get("connectedCount")+region.get("connectedCountB"))
	if "天津"==reg:
		ws.write(87,2,region.get("dispatchCount"))
		ws.write(87,3,region.get("connectedCount")+region.get("connectedCountB"))
		ws.write(108,2,region.get("connectedCount")+region.get("connectedCountB"))

	print("89调度量：	"+str(region.get("dispatchCount")))
	print("C端接通量：	"+str(region.get("connectedCount")+region.get("connectedCountB")))
#ws.write(4,0,"11111")


#统计C端报表信息：处理完成量、
workbook2 = xlrd.open_workbook("C:\Users\24508\Desktop/2019-01-20-2019-01-20-20190120185524843.xlsx")
print(workbook2.sheet_names())
sheet1_name = workbook2.sheet_names()[0]
sheet1 = workbook2.sheet_by_index(0)
sheet1 = workbook2.sheet_by_name("C端")
sheet2 = workbook2.sheet_by_name("B端")
#print(sheet1.cell(1,1))
#print(sheet2.cell(1,1))

region="地区"
num = 1



#print(sheet1.cell(1,5))
#print(type(sheet1.cell(1,5)))
#tr = str(sheet1.cell(num,5))
# tr = sheet1.cell_value(1,5)
# print(tr)
# tu = "是"
# if tr ==tu:
# 	print("是")
# elif tr == "否":
# 	print("否")
# else:
# 	print("=======================")

shds = gdds=hbds=ahds=jxds=jsds=szds=suzds=fjds=sdds=qdds=nbds=zjds=hljds=scds=sxds=tjds=0
shzxx = gdzxx=hbzxx=ahzxx=jxzxx=jszxx=szzxx=suzzxx=fjzxx=sdzxx=qdzxx=nbzxx=zjzxx=hljzxx=sczxx=sxzxx=tjzxx=0
#while region!="":
while num<63:
	region = sheet1.cell_value(num,1)
	region = str(region)
	reg = str(region[:-3])
	if "上海" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				shds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				shzxx+=1
	if "广东" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				gdds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				gdzxx+=1
	if "湖北" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				hbds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				hbzxx+=1
	if "安徽" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				ahds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				ahzxx+=1
	if "江西" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				jxds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				jxzxx+=1
	if "江苏" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				jsds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				jszxx+=1
	if "深圳" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				szds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				szzxx+=1
	if "苏州" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				suzds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				suzzxx+=1
	if "福建" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				fjds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				fjzxx+=1
	if "山东" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				sdds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				sdzxx+=1
	if "青岛" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				qdds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				qdzxx+=1
	if "宁波" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				nbds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				nbzxx+=1
	if "浙江" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				zjds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				zjzxx+=1
	if "黑龙江" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				hljds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				hljzxx+=1
	if "四川" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				scds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				sczxx+=1
	if "陕西" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				sxds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				sxzxx+=1
	if "天津" == reg:
		if "是" == sheet1.cell_value(num,5):
			if ("部分定损"== sheet1.cell_value(num,12) or "全部定损" == sheet1.cell_value(num,12)):
				tjds+=1
			elif "转线下" == sheet1.cell_value(num,12):
				tjzxx+=1

	#print(region)
	#print(reg)
	num+=1

#print(shds , gdds,hbds,ahds,jxds,jsds,szds,suzds,fjds,sdds,qdds,nbds,zjds,hljds,scds,sxds,tjds)
ws.write(92,3,shds)
ws.write(93,3,gdds)
ws.write(94,3,hbds)
ws.write(95,3,ahds)
ws.write(96,3,jxds)
ws.write(97,3,jsds)
ws.write(98,3,szds)
ws.write(99,3,suzds)
ws.write(100,3,fjds)
ws.write(101,3,sdds)
ws.write(102,3,qdds)
ws.write(103,3,nbds)
ws.write(104,3,zjds)
ws.write(105,3,hljds)
ws.write(106,3,scds)
ws.write(107,3,sxds)
ws.write(108,3,tjds)

#print(shzxx , gdzxx,hbzxx,ahzxx,jxzxx,jszxx,szzxx,suzzxx,fjzxx,sdzxx,qdzxx,nbzxx,zjzxx,hljzxx,sczxx,sxzxx,tjzxx)
ws.write(92,4,shzxx)
ws.write(93,4,gdzxx)
ws.write(94,4,hbzxx)
ws.write(95,4,ahzxx)
ws.write(96,4,jxzxx)
ws.write(97,4,jszxx)
ws.write(98,4,szzxx)
ws.write(99,4,suzzxx)
ws.write(100,4,fjzxx)
ws.write(101,4,sdzxx)
ws.write(102,4,qdzxx)
ws.write(103,4,nbzxx)
ws.write(104,4,zjzxx)
ws.write(105,4,hljzxx)
ws.write(106,4,sczxx)
ws.write(107,4,sxzxx)
ws.write(108,4,tjzxx)



#==================================================================================
#B端统计

region_b="地区"
num_b=1

shfq = gdfq=hbfq=ahfq=jxfq=jsfq=szfq=suzfq=fjfq=sdfq=qdfq=nbfq=zjfq=hljfq=scfq=sxfq=tjfq=0
shjt = gdjt=hbjt=ahjt=jxjt=jsjt=szjt=suzjt=fjjt=sdjt=qdjt=nbjt=zjjt=hljjt=scjt=sxjt=tjjt=0
sh_bds = gd_bds=hb_bds=ah_bds=jx_bds=js_bds=sz_bds=suz_bds=fj_bds=sd_bds=qd_bds=nb_bds=zj_bds=hlj_bds=sc_bds=sx_bds=tj_bds=0
sh_bzxx = gd_bzxx=hb_bzxx=ah_bzxx=jx_bzxx=js_bzxx=sz_bzxx=suz_bzxx=fj_bzxx=sd_bzxx=qd_bzxx=nb_bzxx=zj_bzxx=hlj_bzxx=sc_bzxx=sx_bzxx=tj_bzxx=0
#while region_b!="":
while num_b<241:
	region_b = sheet2.cell_value(num_b,1)
	region_b = str(region_b)
	reg_b = str(region_b[:-3])
	if "上海" == reg_b:
		shfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			shjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				sh_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				sh_bzxx+=1
	if "广东" == reg_b:
		gdfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			gdjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				gd_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				gd_bzxx+=1
	if "湖北" == reg_b:
		hbfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			hbjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				hb_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				hb_bzxx+=1
	if "安徽" == reg_b:
		ahfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			ahjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				ah_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				ah_bzxx+=1
	if "江西" == reg_b:
		jxfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			jxjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				jx_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				jx_bzxx+=1
	if "江苏" == reg_b:
		jsfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			jsjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				js_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				js_bzxx+=1
	if "深圳" == reg_b:
		szfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			szjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				sz_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				sz_bzxx+=1
	if "苏州" == reg_b:
		suzfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			suzjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				suz_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				suz_bzxx+=1
	if "福建" == reg_b:
		fjfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			fjjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				fj_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				fj_bzxx+=1
	if "山东" == reg_b:
		sdfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			sdjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				sd_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				sd_bzxx+=1
	if "青岛" == reg_b:
		qdfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			qdjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				qd_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				qd_bzxx+=1
	if "宁波" == reg_b:
		nbfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			nbjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				nb_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				nb_bzxx+=1
	if "浙江" == reg_b:
		zjfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			zjjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				zj_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				zj_bzxx+=1
	if "黑龙江" == reg_b:
		hljfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			hljjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				hlj_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				hlj_bzxx+=1
	if "四川" == reg_b:
		scfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			scjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				sc_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				sc_bzxx+=1
	if "陕西" == reg_b:
		sxfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			sxjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				sx_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				sx_bzxx+=1
	if "天津" == reg_b:
		tjfq+=1
		if "是" == sheet2.cell_value(num_b,5):
			tjjt+=1
			if ("部分定损"== sheet2.cell_value(num_b,12) or "全部定损" == sheet2.cell_value(num_b,12)):
				tj_bds+=1
			elif "转线下" == sheet2.cell_value(num_b,12):
				tj_bzxx+=1
	num_b+=1





#B端发起任务量写入
#shfq = gdfq=hbfq=ahfq=jxfq=jsfq=szfq=suzfq=fjfq=sdfq=qdfq=nbfq=zjfq=hljfq=scfq=sxfq=tjfq=0
ws.write(71,7,shfq)
ws.write(72,7,gdfq)
ws.write(73,7,hbfq)
ws.write(74,7,ahfq)
ws.write(75,7,jxfq)
ws.write(76,7,jsfq)
ws.write(77,7,szfq)
ws.write(78,7,suzfq)
ws.write(79,7,fjfq)
ws.write(80,7,sdfq)
ws.write(81,7,qdfq)
ws.write(82,7,nbfq)
ws.write(83,7,zjfq)
ws.write(84,7,hljfq)
ws.write(85,7,scfq)
ws.write(86,7,sxfq)
ws.write(87,7,tjfq)
#B端接通任务量写入
#shjt = gdjt=hbjt=ahjt=jxjt=jsjt=szjt=suzjt=fjjt=sdjt=qdjt=nbjt=zjjt=hljjt=scjt=sxjt=tjjt=0
ws.write(71,8,shjt)
ws.write(72,8,gdjt)
ws.write(73,8,hbjt)
ws.write(74,8,ahjt)
ws.write(75,8,jxjt)
ws.write(76,8,jsjt)
ws.write(77,8,szjt)
ws.write(78,8,suzjt)
ws.write(79,8,fjjt)
ws.write(80,8,sdjt)
ws.write(81,8,qdjt)
ws.write(82,8,nbjt)
ws.write(83,8,zjjt)
ws.write(84,8,hljjt)
ws.write(85,8,scjt)
ws.write(86,8,sxjt)
ws.write(87,8,tjjt)
#B端接通任务量写入二
ws.write(92,7,shjt)
ws.write(93,7,gdjt)
ws.write(94,7,hbjt)
ws.write(95,7,ahjt)
ws.write(96,7,jxjt)
ws.write(97,7,jsjt)
ws.write(98,7,szjt)
ws.write(99,7,suzjt)
ws.write(100,7,fjjt)
ws.write(101,7,sdjt)
ws.write(102,7,qdjt)
ws.write(103,7,nbjt)
ws.write(104,7,zjjt)
ws.write(105,7,hljjt)
ws.write(106,7,scjt)
ws.write(107,7,sxjt)
ws.write(108,7,tjjt)
#B端处理完成量写入表格
ws.write(92,8,sh_bds)
ws.write(93,8,gd_bds)
ws.write(94,8,hb_bds)
ws.write(95,8,ah_bds)
ws.write(96,8,jx_bds)
ws.write(97,8,js_bds)
ws.write(98,8,sz_bds)
ws.write(99,8,suz_bds)
ws.write(100,8,fj_bds)
ws.write(101,8,sd_bds)
ws.write(102,8,qd_bds)
ws.write(103,8,nb_bds)
ws.write(104,8,zj_bds)
ws.write(105,8,hlj_bds)
ws.write(106,8,sc_bds)
ws.write(107,8,sx_bds)
ws.write(108,8,tj_bds)
#B端转线下处理量
ws.write(92,9,sh_bzxx)
ws.write(93,9,gd_bzxx)
ws.write(94,9,hb_bzxx)
ws.write(95,9,ah_bzxx)
ws.write(96,9,jx_bzxx)
ws.write(97,9,js_bzxx)
ws.write(98,9,sz_bzxx)
ws.write(99,9,suz_bzxx)
ws.write(100,9,fj_bzxx)
ws.write(101,9,sd_bzxx)
ws.write(102,9,qd_bzxx)
ws.write(103,9,nb_bzxx)
ws.write(104,9,zj_bzxx)
ws.write(105,9,hlj_bzxx)
ws.write(106,9,sc_bzxx)
ws.write(107,9,sx_bzxx)
ws.write(108,9,tj_bzxx)





new_excel.save("C:/Users/Administrator/Desktop/r1.xlsx")