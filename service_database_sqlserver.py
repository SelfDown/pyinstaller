#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
from config import getTemplate
import pymssql
import json
last_database_ip = ""
conn = None
def getData(collection):
	print collection
	# 判断页数是否正确
	page = int(collection['page'])
	limit = int(collection['limit'])
	if page<=0 or limit < 1:
		return {"data":[],"page":page,"total":0,"success":False}
	start = (page-1)*limit
	end = start+limit
	where = " where 1=1 " 
	if collection['search']:
		where +=" and ("
		fields = collection["search_fields"].split(",")
		first = True
		for item in fields:
			if first:
				where  +=' '+item+" like '%"+collection["search"]+"%'"
				first = False
			else:
				where +="or "+item+" like '%"+collection["search"]+"%'"
		where += " ) "
	
	if collection["search5"]:
		where +=" and ("
		fields5 = collection["search5_fields"]
		where += fields5+" in ("
		for item in collection["search5"].split(","):
			where +=" '"+item+"',"
		where +=" '6bb61e3b7bce0931da574d19d1d82c88')"
		where +=" ) "
	first_select_index = collection['sql'].lower().index("select")+6
	sql_row_number = collection['sql'][0:first_select_index]+" row_number() over( ORDER BY "+collection["OrderBy"]+") as row_number," +collection['sql'][first_select_index:]
	sql_table = "select * from ("+sql_row_number+") t "
	sql =sql_table+where+" and row_number> "+str(start)+" and row_number <= "+str(end)
	print sql
	# 查询总数
	countSql="select count(*) as count from ("+sql_table+' '+where+") k"
	#print countSql 
	global conn
	if last_database_ip != collection['host']:
		if conn:
			conn.close()
		conn=pymssql.connect(collection['host'],collection['user'],collection['password'],collection['database'], charset='utf8',as_dict=True)
		last_database_ip == collection["host"]
		   
	c=conn.cursor()
	c.execute(sql)
	data = c.fetchall()
	# 添加位置
	data = getPosition(data,collection['service'],collection['ID'])
	c.execute(countSql)
	count = c.fetchone()
	return {"page":page,"count":count["count"],"data":data,"success":True}


import json
import datetime
class CJsonEncoder(json.JSONEncoder):

	def default(self, obj):
		print "======",obj,"================="
		if isinstance(obj, datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime("%Y-%m-%d")
if __name__ == '__main__':
	collection = {
		"service_type": "service_database_sqlserver",
		"service": "service_jiliang",
		"backup": "剂量率实时数据",
		"host": "192.168.2.99",
		"database": "zhang2",
		"user": "sa",
		"password": "dms@888",
		"sql": "SELECT EM_OMS_DoseRatioInfo.Stamptime ,EM_OMS_DoseRatioInfo.ID,EM_OMS_DoseRatioInfo.CollectTime as c11 FROM EM_OMS_DoseRatioInfo LEFT JOIN EM_OMS_Monitor ON EM_OMS_DoseRatioInfo.MonitorID = EM_OMS_Monitor.ID",
		"ID": "ID",
		"OrderBy": "EM_OMS_DoseRatioInfo.ID",
		"page": "1",
		"limit": "10",
		"search": "",
		"search_fields": "", 
		"search2": "",
		"search2_fields": "",
		"search3": "",
		"search3_fields": "",
		"search4": "",
		"search4_fields": "",
		"search5": "",
		"search5_fields": ""
	}
	data = getData(collection)
	import chardet
	
	str_json=json.dumps(data,encoding="utf8",ensure_ascii=False,cls=CJsonEncoder)
	print str_json